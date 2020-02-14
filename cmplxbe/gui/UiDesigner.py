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

from PyQt5 import QtCore, QtGui, QtWidgets
import cmplxbe.gui.resources_rc  # noqa


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1450, 946)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.imageCanvas = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.imageCanvas.sizePolicy().hasHeightForWidth()
        )
        self.imageCanvas.setSizePolicy(sizePolicy)
        self.imageCanvas.setMinimumSize(QtCore.QSize(20, 20))
        self.imageCanvas.setText("")
        self.imageCanvas.setPixmap(QtGui.QPixmap(":/images/icons/logo_PS.png"))
        self.imageCanvas.setScaledContents(False)
        self.imageCanvas.setAlignment(QtCore.Qt.AlignCenter)
        self.imageCanvas.setObjectName("imageCanvas")
        self.gridLayout.addWidget(self.imageCanvas, 4, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1450, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockGrid = QtWidgets.QDockWidget(MainWindow)
        self.dockGrid.setObjectName("dockGrid")
        self.dockGridContent = QtWidgets.QWidget()
        self.dockGridContent.setObjectName("dockGridContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockGridContent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupGrid = QtWidgets.QGroupBox(self.dockGridContent)
        self.groupGrid.setFlat(False)
        self.groupGrid.setCheckable(True)
        self.groupGrid.setObjectName("groupGrid")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupGrid)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_5.addLayout(self.gridLayout_6)
        self.verticalLayout.addWidget(self.groupGrid)
        self.dockGrid.setWidget(self.dockGridContent)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockGrid)
        self.dockIsochromaticLines = QtWidgets.QDockWidget(MainWindow)
        self.dockIsochromaticLines.setEnabled(True)
        self.dockIsochromaticLines.setFloating(False)
        self.dockIsochromaticLines.setObjectName("dockIsochromaticLines")
        self.dockIsochromaticLinesContent = QtWidgets.QWidget()
        self.dockIsochromaticLinesContent.setObjectName(
            "dockIsochromaticLinesContent"
        )
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.dockIsochromaticLinesContent
        )
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.dockIsochromaticLinesContent)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.dockIsochromaticLines.setWidget(self.dockIsochromaticLinesContent)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(2), self.dockIsochromaticLines
        )
        self.dockNav = QtWidgets.QDockWidget(MainWindow)
        self.dockNav.setObjectName("dockNav")
        self.dockNavContents = QtWidgets.QWidget()
        self.dockNavContents.setObjectName("dockNavContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockNavContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupNav = QtWidgets.QGroupBox(self.dockNavContents)
        self.groupNav.setAlignment(QtCore.Qt.AlignCenter)
        self.groupNav.setFlat(False)
        self.groupNav.setObjectName("groupNav")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupNav)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnLeft = QtWidgets.QToolButton(self.groupNav)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/images/icons/left.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnLeft.setIcon(icon)
        self.btnLeft.setIconSize(QtCore.QSize(40, 40))
        self.btnLeft.setObjectName("btnLeft")
        self.gridLayout_2.addWidget(self.btnLeft, 3, 2, 1, 1)
        self.btnRight = QtWidgets.QToolButton(self.groupNav)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/images/icons/right.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnRight.setIcon(icon1)
        self.btnRight.setIconSize(QtCore.QSize(40, 40))
        self.btnRight.setObjectName("btnRight")
        self.gridLayout_2.addWidget(self.btnRight, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.gridLayout_2.addItem(spacerItem, 3, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.gridLayout_2.addItem(spacerItem1, 7, 1, 1, 1)
        self.btnRightt = QtWidgets.QToolButton(self.groupNav)
        self.btnRightt.setMaximumSize(QtCore.QSize(50, 50))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/images/icons/rright.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnRightt.setIcon(icon2)
        self.btnRightt.setObjectName("btnRightt")
        self.gridLayout_2.addWidget(self.btnRightt, 3, 5, 1, 1)
        self.btnLeftt = QtWidgets.QToolButton(self.groupNav)
        self.btnLeftt.setMaximumSize(QtCore.QSize(50, 50))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/images/icons/lleft.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnLeftt.setIcon(icon3)
        self.btnLeftt.setObjectName("btnLeftt")
        self.gridLayout_2.addWidget(self.btnLeftt, 3, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnCenter = QtWidgets.QToolButton(self.groupNav)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/images/icons/refresh.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnCenter.setIcon(icon4)
        self.btnCenter.setIconSize(QtCore.QSize(31, 31))
        self.btnCenter.setObjectName("btnCenter")
        self.horizontalLayout_4.addWidget(self.btnCenter)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 3, 3, 1, 1)
        self.btnDownLeft = QtWidgets.QToolButton(self.groupNav)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/images/icons/down_left.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnDownLeft.setIcon(icon5)
        self.btnDownLeft.setIconSize(QtCore.QSize(40, 40))
        self.btnDownLeft.setObjectName("btnDownLeft")
        self.gridLayout_2.addWidget(self.btnDownLeft, 4, 2, 1, 1)
        self.btnUp = QtWidgets.QToolButton(self.groupNav)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/images/icons/up.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnUp.setIcon(icon6)
        self.btnUp.setIconSize(QtCore.QSize(40, 40))
        self.btnUp.setObjectName("btnUp")
        self.gridLayout_2.addWidget(self.btnUp, 2, 3, 1, 1)
        self.btnUpLeft = QtWidgets.QToolButton(self.groupNav)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/images/icons/up_left.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnUpLeft.setIcon(icon7)
        self.btnUpLeft.setIconSize(QtCore.QSize(40, 40))
        self.btnUpLeft.setObjectName("btnUpLeft")
        self.gridLayout_2.addWidget(self.btnUpLeft, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnZZoomOut = QtWidgets.QToolButton(self.groupNav)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/images/icons/zoomout.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnZZoomOut.setIcon(icon8)
        self.btnZZoomOut.setIconSize(QtCore.QSize(40, 40))
        self.btnZZoomOut.setObjectName("btnZZoomOut")
        self.horizontalLayout_7.addWidget(self.btnZZoomOut)
        self.btnZoomOut = QtWidgets.QToolButton(self.groupNav)
        self.btnZoomOut.setMaximumSize(QtCore.QSize(40, 40))
        self.btnZoomOut.setIcon(icon8)
        self.btnZoomOut.setIconSize(QtCore.QSize(30, 30))
        self.btnZoomOut.setObjectName("btnZoomOut")
        self.horizontalLayout_7.addWidget(self.btnZoomOut)
        self.btnZoomIn = QtWidgets.QToolButton(self.groupNav)
        self.btnZoomIn.setMaximumSize(QtCore.QSize(40, 40))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/images/icons/zoomin.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnZoomIn.setIcon(icon9)
        self.btnZoomIn.setIconSize(QtCore.QSize(30, 30))
        self.btnZoomIn.setObjectName("btnZoomIn")
        self.horizontalLayout_7.addWidget(self.btnZoomIn)
        self.btnZZoomIn = QtWidgets.QToolButton(self.groupNav)
        self.btnZZoomIn.setIcon(icon9)
        self.btnZZoomIn.setIconSize(QtCore.QSize(40, 40))
        self.btnZZoomIn.setObjectName("btnZZoomIn")
        self.horizontalLayout_7.addWidget(self.btnZZoomIn)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 6, 1, 1, 5)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.gridLayout_2.addItem(spacerItem3, 0, 3, 1, 1)
        self.btnDownRight = QtWidgets.QToolButton(self.groupNav)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/images/icons/down_right.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnDownRight.setIcon(icon10)
        self.btnDownRight.setIconSize(QtCore.QSize(40, 40))
        self.btnDownRight.setObjectName("btnDownRight")
        self.gridLayout_2.addWidget(self.btnDownRight, 4, 4, 1, 1)
        self.btnDown = QtWidgets.QToolButton(self.groupNav)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/images/icons/down.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnDown.setIcon(icon11)
        self.btnDown.setIconSize(QtCore.QSize(40, 40))
        self.btnDown.setObjectName("btnDown")
        self.gridLayout_2.addWidget(self.btnDown, 4, 3, 1, 1)
        self.btnDownn = QtWidgets.QToolButton(self.groupNav)
        self.btnDownn.setMaximumSize(QtCore.QSize(50, 50))
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/images/icons/downn.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnDownn.setIcon(icon12)
        self.btnDownn.setObjectName("btnDownn")
        self.gridLayout_2.addWidget(self.btnDownn, 5, 3, 1, 1)
        self.btnUpp = QtWidgets.QToolButton(self.groupNav)
        self.btnUpp.setMaximumSize(QtCore.QSize(50, 50))
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(":/images/icons/upp.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnUpp.setIcon(icon13)
        self.btnUpp.setObjectName("btnUpp")
        self.gridLayout_2.addWidget(self.btnUpp, 1, 3, 1, 1)
        self.btnUpRight = QtWidgets.QToolButton(self.groupNav)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap(":/images/icons/up_right.svg"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.btnUpRight.setIcon(icon14)
        self.btnUpRight.setIconSize(QtCore.QSize(40, 40))
        self.btnUpRight.setObjectName("btnUpRight")
        self.gridLayout_2.addWidget(self.btnUpRight, 2, 4, 1, 1)
        self.verticalLayout_4.addWidget(self.groupNav)
        self.dockNav.setWidget(self.dockNavContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockNav)
        self.dockFunction = QtWidgets.QDockWidget(MainWindow)
        self.dockFunction.setObjectName("dockFunction")
        self.dockFunctionContents = QtWidgets.QWidget()
        self.dockFunctionContents.setObjectName("dockFunctionContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.dockFunctionContents
        )
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupFunction = QtWidgets.QGroupBox(self.dockFunctionContents)
        self.groupFunction.setObjectName("groupFunction")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupFunction)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labelImag = QtWidgets.QLabel(self.groupFunction)
        self.labelImag.setMaximumSize(QtCore.QSize(40, 16777215))
        self.labelImag.setObjectName("labelImag")
        self.gridLayout_4.addWidget(self.labelImag, 8, 2, 1, 1)
        self.labelQuickSelect = QtWidgets.QLabel(self.groupFunction)
        self.labelQuickSelect.setObjectName("labelQuickSelect")
        self.gridLayout_4.addWidget(self.labelQuickSelect, 20, 2, 1, 4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnUpdate = QtWidgets.QPushButton(self.groupFunction)
        self.btnUpdate.setEnabled(False)
        self.btnUpdate.setChecked(False)
        self.btnUpdate.setObjectName("btnUpdate")
        self.horizontalLayout_2.addWidget(self.btnUpdate)
        self.btnAuto = QtWidgets.QPushButton(self.groupFunction)
        self.btnAuto.setCheckable(True)
        self.btnAuto.setChecked(True)
        self.btnAuto.setObjectName("btnAuto")
        self.horizontalLayout_2.addWidget(self.btnAuto)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 26, 2, 1, 4)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.gridLayout_4.addItem(spacerItem4, 11, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.gridLayout_4.addItem(spacerItem5, 8, 1, 1, 1)
        self.labelFz = QtWidgets.QLabel(self.groupFunction)
        self.labelFz.setObjectName("labelFz")
        self.gridLayout_4.addWidget(self.labelFz, 4, 2, 1, 1)
        self.labelWidth = QtWidgets.QLabel(self.groupFunction)
        self.labelWidth.setMaximumSize(QtCore.QSize(50, 16777215))
        self.labelWidth.setObjectName("labelWidth")
        self.gridLayout_4.addWidget(self.labelWidth, 17, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.gridLayout_4.addItem(spacerItem6, 14, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        self.gridLayout_4.addItem(spacerItem7, 8, 6, 1, 1)
        self.labelTo2 = QtWidgets.QLabel(self.groupFunction)
        self.labelTo2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelTo2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTo2.setObjectName("labelTo2")
        self.gridLayout_4.addWidget(self.labelTo2, 8, 4, 1, 1)
        self.labelReal = QtWidgets.QLabel(self.groupFunction)
        self.labelReal.setMaximumSize(QtCore.QSize(40, 16777215))
        self.labelReal.setObjectName("labelReal")
        self.gridLayout_4.addWidget(self.labelReal, 7, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.groupFunction)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 13, 2, 1, 4)
        self.labelFunction = QtWidgets.QLabel(self.groupFunction)
        self.labelFunction.setObjectName("labelFunction")
        self.gridLayout_4.addWidget(self.labelFunction, 0, 2, 1, 4)
        self.sboxWidth = QtWidgets.QSpinBox(self.groupFunction)
        self.sboxWidth.setMinimum(10)
        self.sboxWidth.setMaximum(99999)
        self.sboxWidth.setSingleStep(100)
        self.sboxWidth.setStepType(
            QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType
        )
        self.sboxWidth.setProperty("value", 1000)
        self.sboxWidth.setObjectName("sboxWidth")
        self.gridLayout_4.addWidget(self.sboxWidth, 17, 3, 1, 3)
        self.cboxEqualAxes = QtWidgets.QCheckBox(self.groupFunction)
        self.cboxEqualAxes.setChecked(True)
        self.cboxEqualAxes.setObjectName("cboxEqualAxes")
        self.gridLayout_4.addWidget(self.cboxEqualAxes, 10, 3, 1, 3)
        self.labelTo1 = QtWidgets.QLabel(self.groupFunction)
        self.labelTo1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.labelTo1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTo1.setObjectName("labelTo1")
        self.gridLayout_4.addWidget(self.labelTo1, 7, 4, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnWidth500 = QtWidgets.QToolButton(self.groupFunction)
        self.btnWidth500.setObjectName("btnWidth500")
        self.horizontalLayout_3.addWidget(self.btnWidth500)
        self.btnWidth1000 = QtWidgets.QToolButton(self.groupFunction)
        self.btnWidth1000.setObjectName("btnWidth1000")
        self.horizontalLayout_3.addWidget(self.btnWidth1000)
        self.btnWidth2500 = QtWidgets.QToolButton(self.groupFunction)
        self.btnWidth2500.setObjectName("btnWidth2500")
        self.horizontalLayout_3.addWidget(self.btnWidth2500)
        self.btnWidth5000 = QtWidgets.QToolButton(self.groupFunction)
        self.btnWidth5000.setObjectName("btnWidth5000")
        self.horizontalLayout_3.addWidget(self.btnWidth5000)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 21, 2, 1, 4)
        self.labelHeight = QtWidgets.QLabel(self.groupFunction)
        self.labelHeight.setObjectName("labelHeight")
        self.gridLayout_4.addWidget(self.labelHeight, 18, 2, 1, 1)
        self.sboxHeight = QtWidgets.QSpinBox(self.groupFunction)
        self.sboxHeight.setEnabled(False)
        self.sboxHeight.setMinimum(10)
        self.sboxHeight.setMaximum(99999)
        self.sboxHeight.setSingleStep(100)
        self.sboxHeight.setStepType(
            QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType
        )
        self.sboxHeight.setProperty("value", 1000)
        self.sboxHeight.setObjectName("sboxHeight")
        self.gridLayout_4.addWidget(self.sboxHeight, 18, 3, 1, 3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cboxAspectRatio = QtWidgets.QCheckBox(self.groupFunction)
        self.cboxAspectRatio.setChecked(True)
        self.cboxAspectRatio.setObjectName("cboxAspectRatio")
        self.horizontalLayout_5.addWidget(self.cboxAspectRatio)
        self.cboxOneToOne = QtWidgets.QCheckBox(self.groupFunction)
        self.cboxOneToOne.setChecked(False)
        self.cboxOneToOne.setObjectName("cboxOneToOne")
        self.horizontalLayout_5.addWidget(self.cboxOneToOne)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 16, 3, 1, 3)
        self.leFunc = QtWidgets.QLineEdit(self.groupFunction)
        self.leFunc.setObjectName("leFunc")
        self.gridLayout_4.addWidget(self.leFunc, 4, 3, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.gridLayout_4.addItem(spacerItem8, 27, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding,
        )
        self.gridLayout_4.addItem(spacerItem9, 23, 3, 1, 1)
        self.leRealMin = QtWidgets.QLineEdit(self.groupFunction)
        self.leRealMin.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leRealMin.setObjectName("leRealMin")
        self.gridLayout_4.addWidget(self.leRealMin, 7, 3, 1, 1)
        self.leRealMax = QtWidgets.QLineEdit(self.groupFunction)
        self.leRealMax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leRealMax.setObjectName("leRealMax")
        self.gridLayout_4.addWidget(self.leRealMax, 7, 5, 1, 1)
        self.leImagMin = QtWidgets.QLineEdit(self.groupFunction)
        self.leImagMin.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leImagMin.setObjectName("leImagMin")
        self.gridLayout_4.addWidget(self.leImagMin, 8, 3, 1, 1)
        self.leImagMax = QtWidgets.QLineEdit(self.groupFunction)
        self.leImagMax.setMaximumSize(QtCore.QSize(80, 16777215))
        self.leImagMax.setObjectName("leImagMax")
        self.gridLayout_4.addWidget(self.leImagMax, 8, 5, 1, 1)
        self.horizontalLayout.addWidget(self.groupFunction)
        self.dockFunction.setWidget(self.dockFunctionContents)
        MainWindow.addDockWidget(
            QtCore.Qt.DockWidgetArea(1), self.dockFunction
        )
        self.dockDomain = QtWidgets.QDockWidget(MainWindow)
        self.dockDomain.setObjectName("dockDomain")
        self.dockDomainContents = QtWidgets.QWidget()
        self.dockDomainContents.setObjectName("dockDomainContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockDomainContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupDomain = QtWidgets.QGroupBox(self.dockDomainContents)
        self.groupDomain.setObjectName("groupDomain")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupDomain)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.domainCanvas = QtWidgets.QLabel(self.groupDomain)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.domainCanvas.sizePolicy().hasHeightForWidth()
        )
        self.domainCanvas.setSizePolicy(sizePolicy)
        self.domainCanvas.setMinimumSize(QtCore.QSize(220, 220))
        self.domainCanvas.setText("")
        self.domainCanvas.setScaledContents(False)
        self.domainCanvas.setAlignment(QtCore.Qt.AlignCenter)
        self.domainCanvas.setObjectName("domainCanvas")
        self.gridLayout_5.addWidget(self.domainCanvas, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupDomain)
        self.dockDomain.setWidget(self.dockDomainContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockDomain)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.btnAuto.toggled["bool"].connect(self.btnUpdate.setDisabled)
        self.cboxOneToOne.toggled["bool"].connect(
            self.cboxAspectRatio.setDisabled
        )
        self.cboxAspectRatio.toggled["bool"].connect(
            self.sboxHeight.setDisabled
        )
        self.cboxOneToOne.toggled["bool"].connect(
            self.cboxAspectRatio.setChecked
        )
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Complex Beauties Explorer")
        )
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Tools"))
        self.groupGrid.setTitle(_translate("MainWindow", "Grid"))
        self.groupBox.setTitle(_translate("MainWindow", "Isochromatic Lines"))
        self.groupNav.setTitle(_translate("MainWindow", "Navigation"))
        self.btnLeft.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.btnRight.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.btnCenter.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.btnUp.setShortcut(_translate("MainWindow", "Ctrl+Up"))
        self.btnDown.setShortcut(_translate("MainWindow", "Ctrl+Down"))
        self.groupFunction.setTitle(
            _translate("MainWindow", "Function and Dimensions")
        )
        self.labelImag.setText(_translate("MainWindow", "imag"))
        self.labelQuickSelect.setText(
            _translate("MainWindow", "Quick Select (width)")
        )
        self.btnUpdate.setText(_translate("MainWindow", "update"))
        self.btnAuto.setText(_translate("MainWindow", "auto"))
        self.labelFz.setText(_translate("MainWindow", "f(z) = "))
        self.labelWidth.setText(_translate("MainWindow", "width"))
        self.labelTo2.setText(_translate("MainWindow", "to"))
        self.labelReal.setText(_translate("MainWindow", "real"))
        self.labelFunction.setText(
            _translate("MainWindow", "Complex Function")
        )
        self.sboxWidth.setSuffix(_translate("MainWindow", " px"))
        self.cboxEqualAxes.setText(
            _translate("MainWindow", "keep axes scaling")
        )
        self.labelTo1.setText(_translate("MainWindow", "to"))
        self.btnWidth500.setText(_translate("MainWindow", "500"))
        self.btnWidth1000.setText(_translate("MainWindow", "1000"))
        self.btnWidth2500.setText(_translate("MainWindow", "2500"))
        self.btnWidth5000.setText(_translate("MainWindow", "5000"))
        self.labelHeight.setText(_translate("MainWindow", "height"))
        self.sboxHeight.setSuffix(_translate("MainWindow", " px"))
        self.cboxAspectRatio.setText(_translate("MainWindow", "keep ratio"))
        self.cboxOneToOne.setText(_translate("MainWindow", "1:1"))
        self.leFunc.setText(
            _translate("MainWindow", "(z - 1) / (z**2 + z + 1)")
        )
        self.leRealMin.setText(_translate("MainWindow", "-2.0"))
        self.leRealMax.setText(_translate("MainWindow", "2.0"))
        self.leImagMin.setText(_translate("MainWindow", "-2.0"))
        self.leImagMax.setText(_translate("MainWindow", "2.0"))
        self.groupDomain.setTitle(_translate("MainWindow", "Domain"))
