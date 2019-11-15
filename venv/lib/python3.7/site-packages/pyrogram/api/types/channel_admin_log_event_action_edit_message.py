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


class ChannelAdminLogEventActionEditMessage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x709b2405``

    Parameters:
        prev_message: Either :obj:`MessageEmpty <pyrogram.api.types.MessageEmpty>`, :obj:`Message <pyrogram.api.types.Message>` or :obj:`MessageService <pyrogram.api.types.MessageService>`
        new_message: Either :obj:`MessageEmpty <pyrogram.api.types.MessageEmpty>`, :obj:`Message <pyrogram.api.types.Message>` or :obj:`MessageService <pyrogram.api.types.MessageService>`
    """

    __slots__ = ["prev_message", "new_message"]

    ID = 0x709b2405
    QUALNAME = "types.ChannelAdminLogEventActionEditMessage"

    def __init__(self, *, prev_message, new_message):
        self.prev_message = prev_message  # Message
        self.new_message = new_message  # Message

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEventActionEditMessage":
        # No flags
        
        prev_message = TLObject.read(b)
        
        new_message = TLObject.read(b)
        
        return ChannelAdminLogEventActionEditMessage(prev_message=prev_message, new_message=new_message)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_message.write())
        
        b.write(self.new_message.write())
        
        return b.getvalue()
