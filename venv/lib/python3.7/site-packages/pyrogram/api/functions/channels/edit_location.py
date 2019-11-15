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


class EditLocation(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x58e63f6d``

    Parameters:
        channel: Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`
        geo_point: Either :obj:`InputGeoPointEmpty <pyrogram.api.types.InputGeoPointEmpty>` or :obj:`InputGeoPoint <pyrogram.api.types.InputGeoPoint>`
        address: ``str``

    Returns:
        ``bool``
    """

    __slots__ = ["channel", "geo_point", "address"]

    ID = 0x58e63f6d
    QUALNAME = "functions.channels.EditLocation"

    def __init__(self, *, channel, geo_point, address: str):
        self.channel = channel  # InputChannel
        self.geo_point = geo_point  # InputGeoPoint
        self.address = address  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "EditLocation":
        # No flags
        
        channel = TLObject.read(b)
        
        geo_point = TLObject.read(b)
        
        address = String.read(b)
        
        return EditLocation(channel=channel, geo_point=geo_point, address=address)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.geo_point.write())
        
        b.write(String(self.address))
        
        return b.getvalue()
