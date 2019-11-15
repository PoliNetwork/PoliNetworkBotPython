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


class GetFullChannel(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x08736a09``

    Parameters:
        channel: Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`

    Returns:
        :obj:`messages.ChatFull <pyrogram.api.types.messages.ChatFull>`
    """

    __slots__ = ["channel"]

    ID = 0x08736a09
    QUALNAME = "functions.channels.GetFullChannel"

    def __init__(self, *, channel):
        self.channel = channel  # InputChannel

    @staticmethod
    def read(b: BytesIO, *args) -> "GetFullChannel":
        # No flags
        
        channel = TLObject.read(b)
        
        return GetFullChannel(channel=channel)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        return b.getvalue()
