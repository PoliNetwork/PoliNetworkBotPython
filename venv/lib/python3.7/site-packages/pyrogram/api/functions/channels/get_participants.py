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


class GetParticipants(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x123e05e9``

    Parameters:
        channel: Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`
        filter: Either :obj:`ChannelParticipantsRecent <pyrogram.api.types.ChannelParticipantsRecent>`, :obj:`ChannelParticipantsAdmins <pyrogram.api.types.ChannelParticipantsAdmins>`, :obj:`ChannelParticipantsKicked <pyrogram.api.types.ChannelParticipantsKicked>`, :obj:`ChannelParticipantsBots <pyrogram.api.types.ChannelParticipantsBots>`, :obj:`ChannelParticipantsBanned <pyrogram.api.types.ChannelParticipantsBanned>`, :obj:`ChannelParticipantsSearch <pyrogram.api.types.ChannelParticipantsSearch>` or :obj:`ChannelParticipantsContacts <pyrogram.api.types.ChannelParticipantsContacts>`
        offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``

    Returns:
        Either :obj:`channels.ChannelParticipants <pyrogram.api.types.channels.ChannelParticipants>` or :obj:`channels.ChannelParticipantsNotModified <pyrogram.api.types.channels.ChannelParticipantsNotModified>`
    """

    __slots__ = ["channel", "filter", "offset", "limit", "hash"]

    ID = 0x123e05e9
    QUALNAME = "functions.channels.GetParticipants"

    def __init__(self, *, channel, filter, offset: int, limit: int, hash: int):
        self.channel = channel  # InputChannel
        self.filter = filter  # ChannelParticipantsFilter
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetParticipants":
        # No flags
        
        channel = TLObject.read(b)
        
        filter = TLObject.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Int.read(b)
        
        return GetParticipants(channel=channel, filter=filter, offset=offset, limit=limit, hash=hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
