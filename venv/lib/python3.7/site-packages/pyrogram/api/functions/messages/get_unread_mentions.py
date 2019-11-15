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


class GetUnreadMentions(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x46578472``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        offset_id: ``int`` ``32-bit``
        add_offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        max_id: ``int`` ``32-bit``
        min_id: ``int`` ``32-bit``

    Returns:
        Either :obj:`messages.Messages <pyrogram.api.types.messages.Messages>`, :obj:`messages.MessagesSlice <pyrogram.api.types.messages.MessagesSlice>`, :obj:`messages.ChannelMessages <pyrogram.api.types.messages.ChannelMessages>` or :obj:`messages.MessagesNotModified <pyrogram.api.types.messages.MessagesNotModified>`
    """

    __slots__ = ["peer", "offset_id", "add_offset", "limit", "max_id", "min_id"]

    ID = 0x46578472
    QUALNAME = "functions.messages.GetUnreadMentions"

    def __init__(self, *, peer, offset_id: int, add_offset: int, limit: int, max_id: int, min_id: int):
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetUnreadMentions":
        # No flags
        
        peer = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        add_offset = Int.read(b)
        
        limit = Int.read(b)
        
        max_id = Int.read(b)
        
        min_id = Int.read(b)
        
        return GetUnreadMentions(peer=peer, offset_id=offset_id, add_offset=add_offset, limit=limit, max_id=max_id, min_id=min_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.add_offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.min_id))
        
        return b.getvalue()
