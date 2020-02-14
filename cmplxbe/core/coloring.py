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

import numpy as np
import numexpr as ne
from PIL import Image


def createPixels(w, h, xlim, ylim, function):
    real = np.linspace(*xlim, w)
    imag = np.linspace(*ylim[::-1], h)
    z = np.add(*np.meshgrid(real, imag * 1j, copy=False))
    fz = ne.evaluate(function)
    # fz = (z ** 2 - 1) * (z - 2 - 1j) ** 2 / (z ** 2 + 2 + 2 * 1j)
    phase = np.arctan2(fz.imag, fz.real)
    mag = abs(fz)
    # move phase interval from [-pi,+pi] to [0, 2pi]
    phase = np.where(phase < 0, phase + 2 * np.pi, phase)
    # normalize array to [0, 1]
    phase /= 2 * np.pi
    return phase, mag, fz, z


def hsv(phase, mag, a=0.1, b=0.25):
    hight, width = phase.shape
    # lightness = 1 - 0.6 ** (mag ** (1 / 4))
    lightness = -np.expm1(np.log(a) * np.power(mag, b))
    pixels = hsl2hsv(phase, 1, lightness)
    # NOTE: return RGB w/o A to prevent alpha lacks after pasting
    img = Image.fromarray(pixels, "HSV").convert("RGB")
    return img


def hsl2hsv(h, s, l):
    """Converts HSL [0, 1] to HSV [0, 255] color mode."""
    V = l + s * np.minimum(l, 1 - l)
    S = np.where(V < 1e-10, 0, 2 - 2 * l / V)
    HSV = np.dstack((h, S, V)) * 255
    # return HSV.round().astype(np.uint8)
    np.round(HSV, 0, HSV)
    return HSV.astype(np.uint8)


# EOF - coloring.py
