##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2017 Karl Palsson <karlp@etactica.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
##

'''
This decoder stacks on top of the 'spi' PD and decodes Analog Devices
ADE7758 command/responses.

The ADE7758 is a "Poly Phase Multifunction Energy Metering IC with Per Phase
Information".
'''

from .pd import Decoder
