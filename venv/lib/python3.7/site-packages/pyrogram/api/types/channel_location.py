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


class ChannelLocation(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x209b82db``

    Parameters:
        geo_point: Either :obj:`GeoPointEmpty <pyrogram.api.types.GeoPointEmpty>` or :obj:`GeoPoint <pyrogram.api.types.GeoPoint>`
        address: ``str``
    """

    __slots__ = ["geo_point", "address"]

    ID = 0x209b82db
    QUALNAME = "types.ChannelLocation"

    def __init__(self, *, geo_point, address: str):
        self.geo_point = geo_point  # GeoPoint
        self.address = address  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelLocation":
        # No flags
        
        geo_point = TLObject.read(b)
        
        address = String.read(b)
        
        return ChannelLocation(geo_point=geo_point, address=address)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.geo_point.write())
        
        b.write(String(self.address))
        
        return b.getvalue()
