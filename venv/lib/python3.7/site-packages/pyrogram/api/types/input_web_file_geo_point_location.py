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


class InputWebFileGeoPointLocation(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x9f2221c9``

    Parameters:
        geo_point: Either :obj:`InputGeoPointEmpty <pyrogram.api.types.InputGeoPointEmpty>` or :obj:`InputGeoPoint <pyrogram.api.types.InputGeoPoint>`
        access_hash: ``int`` ``64-bit``
        w: ``int`` ``32-bit``
        h: ``int`` ``32-bit``
        zoom: ``int`` ``32-bit``
        scale: ``int`` ``32-bit``
    """

    __slots__ = ["geo_point", "access_hash", "w", "h", "zoom", "scale"]

    ID = 0x9f2221c9
    QUALNAME = "types.InputWebFileGeoPointLocation"

    def __init__(self, *, geo_point, access_hash: int, w: int, h: int, zoom: int, scale: int):
        self.geo_point = geo_point  # InputGeoPoint
        self.access_hash = access_hash  # long
        self.w = w  # int
        self.h = h  # int
        self.zoom = zoom  # int
        self.scale = scale  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "InputWebFileGeoPointLocation":
        # No flags
        
        geo_point = TLObject.read(b)
        
        access_hash = Long.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        zoom = Int.read(b)
        
        scale = Int.read(b)
        
        return InputWebFileGeoPointLocation(geo_point=geo_point, access_hash=access_hash, w=w, h=h, zoom=zoom, scale=scale)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.geo_point.write())
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(Int(self.zoom))
        
        b.write(Int(self.scale))
        
        return b.getvalue()
