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


class ChannelAdminLogEventActionDeleteMessage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x42e047bb``

    Parameters:
        message: Either :obj:`MessageEmpty <pyrogram.api.types.MessageEmpty>`, :obj:`Message <pyrogram.api.types.Message>` or :obj:`MessageService <pyrogram.api.types.MessageService>`
    """

    __slots__ = ["message"]

    ID = 0x42e047bb
    QUALNAME = "types.ChannelAdminLogEventActionDeleteMessage"

    def __init__(self, *, message):
        self.message = message  # Message

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEventActionDeleteMessage":
        # No flags
        
        message = TLObject.read(b)
        
        return ChannelAdminLogEventActionDeleteMessage(message=message)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.message.write())
        
        return b.getvalue()
