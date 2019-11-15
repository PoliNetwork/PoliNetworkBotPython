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


class GetParticipant(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x546dd7a6``

    Parameters:
        channel: Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`
        user_id: Either :obj:`InputUserEmpty <pyrogram.api.types.InputUserEmpty>`, :obj:`InputUserSelf <pyrogram.api.types.InputUserSelf>`, :obj:`InputUser <pyrogram.api.types.InputUser>` or :obj:`InputUserFromMessage <pyrogram.api.types.InputUserFromMessage>`

    Returns:
        :obj:`channels.ChannelParticipant <pyrogram.api.types.channels.ChannelParticipant>`
    """

    __slots__ = ["channel", "user_id"]

    ID = 0x546dd7a6
    QUALNAME = "functions.channels.GetParticipant"

    def __init__(self, *, channel, user_id):
        self.channel = channel  # InputChannel
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args) -> "GetParticipant":
        # No flags
        
        channel = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return GetParticipant(channel=channel, user_id=user_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
