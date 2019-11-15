# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2019 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.api.core import *


class InputGeoPoint(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf3b7acc9``

    Parameters:
        lat: ``float`` ``64-bit``
        long: ``float`` ``64-bit``
    """

    __slots__ = ["lat", "long"]

    ID = 0xf3b7acc9
    QUALNAME = "types.InputGeoPoint"

    def __init__(self, *, lat: float, long: float):
        self.lat = lat  # double
        self.long = long  # double

    @staticmethod
    def read(b: BytesIO, *args) -> "InputGeoPoint":
        # No flags
        
        lat = Double.read(b)
        
        long = Double.read(b)
        
        return InputGeoPoint(lat=lat, long=long)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.lat))
        
        b.write(Double(self.long))
        
        return b.getvalue()
