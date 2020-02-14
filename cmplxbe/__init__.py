#!/usr/bin/env python3
# coding: utf-8
# vim: set ai ts=4 sw=4 sts=0 noet pi ci

# Copyright © 2020 René Wirnata.
# This file is part of Complex Beauties Explorer (CmplxBE).
#
# Complex Beauties Explorer (CmplxBE) is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Complex Beauties Explorer (CmplxBE) is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Complex Beauties Explorer (CmplxBE). If not, see
# <http://www.gnu.org/licenses/>.

import pbr.version

__all__ = ["core"]
__version__ = pbr.version.VersionInfo("cmplxbe").release_string()
