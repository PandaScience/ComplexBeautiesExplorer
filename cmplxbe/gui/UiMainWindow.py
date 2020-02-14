# coding: utf-8
# vim: set ai ts=4 sw=4 sts=0 noet pi ci

# Copyright © 2020 René Wirnata.
# This file is part of Complex Beauties Explorer (CmplxBE).
#
# CmplxBE is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# CmplxBE is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# CmplxBE. If not, see <http://www.gnu.org/licenses/>.

import numexpr as ne
import numpy as np
from scipy import ndimage

from PIL import Image, ImageQt

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox

import cmplxbe
from cmplxbe.gui import UiDesigner
from cmplxbe.core import coloring  # postproc

import wrapt


@wrapt.decorator
def handleDialogErrors(wrapped, instance, args, kwargs):
    error = wrapped(*args, **kwargs)
    # return or notify user which selection is not valid
    if error is None:
        instance.redraw()
    else:
        QMessageBox.critical(instance, "Error!", error)


@wrapt.decorator
def blockMultipleUpdates(wrapped, instance, args, kwargs):
    instance.blockRedraw = True
    wrapped(*args, **kwargs)
    instance.blockRedraw = False
    if instance.btnAuto.isChecked():
        instance.redraw()


class MainWindow(QtWidgets.QMainWindow, UiDesigner.Ui_MainWindow):
    def __init__(self, cwd=None):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # force some dock widgets to minimum width
        self.dockNavContents.setFixedWidth(280)
        self.dockFunctionContents.setFixedWidth(280)

        # add version number permanently to far right end of status bar
        self.version = cmplxbe.__version__
        versionLabel = QtWidgets.QLabel("v{}".format(self.version), self)
        self.statusbar.addPermanentWidget(versionLabel)
        self.setStyleSheet("QStatusBar::item {border: 2px;}")

        # print license information in terminal
        self.printAbout()

        # read deault values for atrributes from GUI
        self.blockRedraw = False
        self.pxWidth = self.sboxWidth.value()
        self.pxHeight = self.sboxHeight.value()
        self.aspectRatio = self.pxWidth / self.pxHeight
        self.realmin = float(self.leRealMin.text())
        self.realmax = float(self.leRealMax.text())
        self.imagmin = float(self.leImagMin.text())
        self.imagmax = float(self.leImagMax.text())
        self.function = self.leFunc.text()
        self.imageImgPre = None
        self.imageImgPost = None
        self.domainImgPre = None
        self.domainImgPost = None

        self.imageCanvas.resizeEvent = lambda event: self.resizePixmapToLabel(
            self.imageImgPost, self.imageCanvas
        )
        self.domainCanvas.resizeEvent = lambda event: self.resizePixmapToLabel(
            self.domainImgPost, self.domainCanvas
        )

        # apply signal/slot settings
        self.connectSignals()

        # populate labels with plots
        self.redraw("image")
        self.redraw("domain")

    # def resizeEvent(self, event):
    #     QtWidgets.QMainWindow.resizeEvent(self, event)
    #     self.resizeImageToLabel()

    def connectSignals(self):
        self.btnUpdate.clicked.connect(lambda: self.redraw)

        # NOTE: typing new px when auto update is enabled leads to multiple
        # unneccesary updating and even segfaults for 'height'.
        self.sboxWidth.editingFinished.connect(
            lambda: changed(self.sboxWidth.value(), "pxWidth")
        )
        self.sboxHeight.editingFinished.connect(
            lambda: changed(self.sboxHeight.value(), "pxHeight")
        )

        changed = self.onDomainControlChanged
        self.leRealMin.textChanged.connect(lambda v: changed(v, "realmin"))
        self.leRealMax.textChanged.connect(lambda v: changed(v, "realmax"))
        self.leImagMin.textChanged.connect(lambda v: changed(v, "imagmin"))
        self.leImagMax.textChanged.connect(lambda v: changed(v, "imagmax"))

        self.leFunc.editingFinished.connect(self.onNewFunction)
        self.cboxAspectRatio.stateChanged.connect(self.onAspectRatioToggled)
        self.cboxOneToOne.stateChanged.connect(self.onOneToOneToggled)

        nav = self.onNavigation
        self.btnUp.clicked.connect(lambda: nav("up"))
        self.btnDown.clicked.connect(lambda: nav("down"))
        self.btnLeft.clicked.connect(lambda: nav("left"))
        self.btnRight.clicked.connect(lambda: nav("right"))
        self.btnUpLeft.clicked.connect(lambda: nav("upleft"))
        self.btnUpRight.clicked.connect(lambda: nav("upright"))
        self.btnDownLeft.clicked.connect(lambda: nav("downleft"))
        self.btnDownRight.clicked.connect(lambda: nav("downright"))

        self.btnUpp.clicked.connect(lambda: nav("up", 3))
        self.btnDownn.clicked.connect(lambda: nav("down", 3))
        self.btnLeftt.clicked.connect(lambda: nav("left", 3))
        self.btnRightt.clicked.connect(lambda: nav("right", 3))

        self.btnZoomIn.clicked.connect(lambda: nav("zoomin"))
        self.btnZoomOut.clicked.connect(lambda: nav("zoomout"))
        self.btnZZoomIn.clicked.connect(lambda: nav("zoomin", 5))
        self.btnZZoomOut.clicked.connect(lambda: nav("zoomout", 5))

        self.btnCenter.clicked.connect(self.centerImage)

        self.btnWidth500.clicked.connect(lambda: self.setWidth(500))
        self.btnWidth1000.clicked.connect(lambda: self.setWidth(1000))
        self.btnWidth2500.clicked.connect(lambda: self.setWidth(2500))
        self.btnWidth5000.clicked.connect(lambda: self.setWidth(5000))

    # TODO: workarounds for editingFinished not being emitted by setValue;
    #   --> better subclass spinbox and use promote widget in designer
    def setWidth(self, value):
        self.sboxWidth.setValue(value)
        self.sboxWidth.editingFinished.emit()

    def setHeight(self, value):
        self.sboxHeight.setValue(value)
        self.sboxHeight.editingFinished.emit()

    @blockMultipleUpdates
    def centerImage(self, *args):
        self.leRealMin.setText("-2")
        self.leRealMax.setText("2")
        self.leImagMin.setText("-2")
        self.leImagMax.setText("2")

    def adaptDomain(self):
        # change relative to width / real part
        ratio = self.pxWidth / self.pxHeight
        wrange_new = self.realmax - self.realmin
        hrange_old = self.imagmax - self.imagmin
        hrange_new = wrange_new / ratio
        diff = hrange_new - hrange_old
        self.sboxImagMin.setValue(self.imagmin - diff / 2)
        self.sboxImagMax.setValue(self.imagmax + diff / 2)

    @blockMultipleUpdates
    def onNavigation(self, direction, factor=1):
        # TODO: fix zoom and crash at diff = 0
        diffr = abs(self.realmax - self.realmin)
        diffi = abs(self.imagmax - self.imagmin)
        # make sure zoom distance is same for in/out when e.g. diff/2 = 0.1
        if direction == "zoomout":
            diffr += 1E-10
            diffi += 1E-10
        expr = int(np.log10(diffr / 2)) - 1
        expi = int(np.log10(diffi / 2)) - 1
        zstepr = factor * 10 ** expr
        zstepi = factor * 10 ** expi
        # prevent sign flipping
        if direction == "zoomin":
            while 2 * zstepr >= diffr or 2 * zstepi >= diffi:
                zstepr /= 2
                zstepi /= 2
        # navigate
        if "up" in direction:
            self.leImagMin.setText("{:3.2g}".format(self.imagmin + zstepi))
            self.leImagMax.setText("{:3.2g}".format(self.imagmax + zstepi))
        if "down" in direction:
            self.leImagMin.setText("{:3.2g}".format(self.imagmin - zstepi))
            self.leImagMax.setText("{:3.2g}".format(self.imagmax - zstepi))
        if "left" in direction:
            self.leRealMin.setText("{:3.2g}".format(self.realmin - zstepi))
            self.leRealMax.setText("{:3.2g}".format(self.realmax - zstepi))
        if "right" in direction:
            self.leRealMin.setText("{:3.2g}".format(self.realmin + zstepi))
            self.leRealMax.setText("{:3.2g}".format(self.realmax + zstepi))
        if direction == "zoomin":
            self.leRealMin.setText("{:3.2g}".format(self.realmin + zstepr))
            self.leRealMax.setText("{:3.2g}".format(self.realmax - zstepr))
            self.leImagMin.setText("{:3.2g}".format(self.imagmin + zstepi))
            self.leImagMax.setText("{:3.2g}".format(self.imagmax - zstepi))
        if direction == "zoomout":
            self.leRealMin.setText("{:3.2g}".format(self.realmin - zstepr))
            self.leRealMax.setText("{:3.2g}".format(self.realmax + zstepr))
            self.leImagMin.setText("{:3.2g}".format(self.imagmin - zstepi))
            self.leImagMax.setText("{:3.2g}".format(self.imagmax + zstepi))

    def onAspectRatioToggled(self, state):
        checked = state == Qt.Checked
        self.sboxHeight.setEnabled(not checked)
        self.aspectRatio = self.pxWidth / self.pxHeight
        for width in [500, 1000, 2500, 5000]:
            self.__getattribute__("btnWidth" + str(width)).setEnabled(state)

    def onOneToOneToggled(self, state):
        # NOTE: some logic already set via designer signal/slot editor
        if state == Qt.Checked:
            self.setHeight(self.pxWidth)

    def onDomainControlChanged(self, value, attr):
        self.__setattr__(attr, float(value))

    def onPixelsChanged(self, value, attr):
        self.__setattr__(attr, value)
        # NOTE: watch order!
        if attr == "pxWidth":
            if self.cboxOneToOne.isChecked():
                self.setHeight(value)
                # NOTE: this will call onControlChanged, so do not update twice
                return
            elif self.cboxAspectRatio.isChecked():
                self.setHeight(value / self.aspectRatio)
                return

        if self.cboxEqualAxes.isChecked():
            self.adaptDomain()

        if self.btnAuto.isChecked() and not self.blockRedraw:
            self.redraw()

    @handleDialogErrors
    def onNewFunction(self):
        error = None
        try:
            # use 2D array of complex floats to raise all NotImplementedErrors
            testArray = np.array([1.1, 2.2, 3.3] * 3).reshape(3, 3) + 0.5j
            ne.evaluate(self.lineEdit.text(), local_dict={"z": testArray})
            # if no errors until now, assume valid input
            self.function = self.lineEdit.text()
        except KeyError:
            error = (
                "In the formula field, you may only use "
                "<ul style='margin-left: -20px;'>"
                "<li> &nbsp; the symbol 'y' (for field values in a.u.)</li>"
                "<li> &nbsp; the symbol 'x' (for corresponding frequencies "
                "in eV)</li>"
                "<li> &nbsp; operators and functions supported by the numexpr "
                "<br> &nbsp; module and compatible with complex ndarrrays."
                "</li></ul>"
            )
        except TypeError:
            error = "Seems like you misspelled one of your math functions."
        except SyntaxError:
            error = (
                "There are syntax errors in your expression for f(z). You "
                "need to explicitly use * between factors and may not use "
                "invalid operators like =."
            )
        except NotImplementedError:
            error = (
                "<p>Sorry, seems like an operator you used in your expression "
                "is not implemented (with good reason) in numexpr.<p/>"
                "<p>Remember that you act operators on (in general) complex "
                "multi-dimensional arrays of floats. Typically, this error "
                "is raised when you try to use"
                "<ul style='margin-left: -20px;'>"
                "<li> &nbsp;logical operators &amp;, |, ~ </li>"
                "<li> &nbsp;comparison operators &lt;, &lt;=, &gt;=, &gt;</li>"
                "<li> &nbsp;a bitshift operator &lt;&lt; or &gt;&gt;</li>"
                "<li> &nbsp;the modulo operator %</li>"
                "</ul> on such a field - which does not really make sense.</p>"
            )
        return error

    def redraw(self, label="image"):
        self.computeData(label)
        # self.postprocess()
        if label == "image":
            self.resizePixmapToLabel(self.imageImgPost, self.imageCanvas)
        else:
            self.resizePixmapToLabel(self.domainImgPost, self.domainCanvas)

    def resizePixmapToLabel(self, img, canvas):
        """Resizes image to match current label dimensions."""
        # skip if image not available yet (startup)
        if img is None:
            return
        # width / height
        cratio = img.size[1] / img.size[0]
        imgratio = self.pxWidth / self.pxHeight
        if canvas.width() > canvas.height():
            height = canvas.height()
            width = round(height * imgratio)
            # cap at canvas width if too large
            if width > canvas.width():
                width = canvas.width()
                height = round(width / imgratio)
        else:
            width = canvas.width()
            height = round(width / imgratio)
            # cap at canvas height if too large
            if height > canvas.height():
                height = canvas.height()
                width = round(height * imgratio)
        # TODO check other algorithms for up/downscaling
        resized = img.resize((width, height), Image.NEAREST)
        # draw image to label
        qtImg = ImageQt.ImageQt(resized)
        pixmap = QtGui.QPixmap.fromImage(qtImg)
        canvas.setPixmap(pixmap)

    def computeData(self, label="image"):
        # default to image canvas
        if label == "image":
            function = self.function
        elif label == "domain":
            function = "z"

        # NOTE: must use numpy array for numba.njit to work!
        xlim = np.array([self.realmin, self.realmax])
        ylim = np.array([self.imagmin, self.imagmax])
        # create function data
        phase, mag, fz, z = coloring.createPixels(
            self.pxWidth, self.pxHeight, xlim, ylim, function
        )
        # color according to phase and magnitude
        img = coloring.hsv(phase, mag, a=0.6, b=0.25)
        self.__setattr__(label + "ImgPre", img.copy())

        # add post-processing
        grid = self.createGrid(fz, mode="edge", alpha=100, step=1)
        img.paste(grid, (0, 0), grid)
        self.__setattr__(label + "ImgPost", img)

    def createGrid(
        self, fz, tol=0.03, step=1, alpha=150, gray=100, mode="simple"
    ):
        blur = addAlpha = False
        if mode == "simple":
            gr = (abs(fz.real) + tol) % step
            gi = (abs(fz.imag) + tol) % step
            grid = np.where((gr <= 2 * tol) | (gi <= 2 * tol), gray, 255)
            blur = addAlpha = True
        elif mode == "checkerboard" or mode == "edge":
            gr = (fz.real // step).astype(int)
            gi = (fz.imag // step).astype(int)
            grid = np.where((gr + gi) % 2 == 0, gray, 255)
        if mode == "edge":
            gx = np.array([[1, 0], [0, -1]])
            gy = np.array([[0, 1], [-1, 0]])
            gridx = ndimage.convolve(grid, gx)
            gridy = ndimage.convolve(grid, gy)
            # NOTE: DO NOT approximate with grid = abs(gridx) + abs(gridy) !!
            grid = np.sqrt(np.square(gridx) + np.square(gridy))
            # grid = ndimage.grey_closing(grid, size=(2, 2))
            grid = ndimage.grey_dilation(grid, size=(3, 3))
            # round and invert
            grid = np.where(grid < 100, 255, 0)
            addAlpha = True

        grid = grid.astype(np.uint8)
        img = Image.fromarray(grid, "L")

        if blur:
            img = img.filter(ImageFilter.SMOOTH)
        # NOTE: must come last!
        if addAlpha:
            # add alpha channel via mask: white --> alpha=0, black -->alpha=alpha
            mask = np.where(grid == 255, 0, alpha).astype(np.uint8)
            mask = Image.fromarray(mask, "L")
            img.putalpha(mask)

        return img.convert("RGBA")

    def showAbout(self):
        """Opens GUI window with copyright and license information."""
        about = QtWidgets.QMessageBox(self)
        about.setWindowTitle("About...")
        # make links work
        about.setTextFormat(Qt.RichText)
        about.setText(
            "<div align='center'>"
            "Complex Beauties Explorer (CmplxBE) v{} <br>".format(self.version)
            + "- Easily plot and analyze Elk optics output data -</div>"
            "<p>Copyright © 2020 René Wirnata</p>"
            "<p>This program is free software: you can redistribute it and/or "
            "modify it under the terms of the GNU General Public License as "
            "published by the Free Software Foundation, either version 3 of "
            "the License, or (at your option) any later version. </p>"
            "<p>This program is distributed in the hope that it will be "
            "useful, but WITHOUT ANY WARRANTY; without even the implied "
            "warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. "
            "See the GNU General Public License for more details. </p>"
            "<p>You should have received a copy of the GNU General Public "
            "License along with this program. If not, see "
            "<a href='https://www.gnu.org/licenses/'>"
            "https://www.gnu.org/licenses/</a>.</p>"
            "<p style='line-height:1.4'>See also:<br>"
            "<a href='http://elk.sourceforge.net'> The Elk Code</a><br>"
            "<a href='https://github.com/PandaScience/ElkOpticsAnalyzer'> "
            "ElkOA Github Page</a><br>"
            "<a href='https://www.researchgate.net/project/"
            "Functional-Approach-to-electrodynamics-in-media'> Research Gate "
            "Project</a><br>"
            "<a href='https://tu-freiberg.de/fakultaet2/thph'> Institute for "
            "Theoretical Physics @ TU BA Freiberg</a>"
        )
        about.exec()

    def printAbout(self):
        """Prints copyright and license information to terminal."""
        txt = (
            "\n============================================================\n"
            ">>>         Complex Beauties Explorer (CmplxBE)          <<<\n"
            ">>>           Copyright (C) 2020 René Wirnata            <<<\n"
            "============================================================\n\n"
            "This program is free software and comes with ABSOLUTELY NO \n"
            "WARRANTY. You are welcome to redistribute it under certain \n"
            "conditions. See Help->About in GUI for details.\n\n"
            "Running version {} \n".format(self.version)
        )
        print(txt)

    def quitGui(self):
        """Quits QT application."""
        print("\n/-------------------------------------------\\")
        print("|            quitting application           |")
        print("\\-------------------------------------------/")
        self.close()


# EOF - UiMainWindow.py
