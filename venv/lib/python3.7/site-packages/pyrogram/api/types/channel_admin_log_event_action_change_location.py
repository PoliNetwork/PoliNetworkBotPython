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


class ChannelAdminLogEventActionChangeLocation(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x0e6b76ae``

    Parameters:
        prev_value: Either :obj:`ChannelLocationEmpty <pyrogram.api.types.ChannelLocationEmpty>` or :obj:`ChannelLocation <pyrogram.api.types.ChannelLocation>`
        new_value: Either :obj:`ChannelLocationEmpty <pyrogram.api.types.ChannelLocationEmpty>` or :obj:`ChannelLocation <pyrogram.api.types.ChannelLocation>`
    """

    __slots__ = ["prev_value", "new_value"]

    ID = 0x0e6b76ae
    QUALNAME = "types.ChannelAdminLogEventActionChangeLocation"

    def __init__(self, *, prev_value, new_value):
        self.prev_value = prev_value  # ChannelLocation
        self.new_value = new_value  # ChannelLocation

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEventActionChangeLocation":
        # No flags
        
        prev_value = TLObject.read(b)
        
        new_value = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangeLocation(prev_value=prev_value, new_value=new_value)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()
