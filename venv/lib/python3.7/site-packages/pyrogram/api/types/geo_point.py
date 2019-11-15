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


class GeoPoint(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x0296f104``

    Parameters:
        long: ``float`` ``64-bit``
        lat: ``float`` ``64-bit``
        access_hash: ``int`` ``64-bit``
    """

    __slots__ = ["long", "lat", "access_hash"]

    ID = 0x0296f104
    QUALNAME = "types.GeoPoint"

    def __init__(self, *, long: float, lat: float, access_hash: int):
        self.long = long  # double
        self.lat = lat  # double
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "GeoPoint":
        # No flags
        
        long = Double.read(b)
        
        lat = Double.read(b)
        
        access_hash = Long.read(b)
        
        return GeoPoint(long=long, lat=lat, access_hash=access_hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Double(self.long))
        
        b.write(Double(self.lat))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()
