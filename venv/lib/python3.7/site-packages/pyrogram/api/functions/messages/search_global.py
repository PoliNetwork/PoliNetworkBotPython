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


class SearchGlobal(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xbf7225a4``

    Parameters:
        q: ``str``
        offset_rate: ``int`` ``32-bit``
        offset_peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        offset_id: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``

    Returns:
        Either :obj:`messages.Messages <pyrogram.api.types.messages.Messages>`, :obj:`messages.MessagesSlice <pyrogram.api.types.messages.MessagesSlice>`, :obj:`messages.ChannelMessages <pyrogram.api.types.messages.ChannelMessages>` or :obj:`messages.MessagesNotModified <pyrogram.api.types.messages.MessagesNotModified>`
    """

    __slots__ = ["q", "offset_rate", "offset_peer", "offset_id", "limit", "folder_id"]

    ID = 0xbf7225a4
    QUALNAME = "functions.messages.SearchGlobal"

    def __init__(self, *, q: str, offset_rate: int, offset_peer, offset_id: int, limit: int, folder_id: int = None):
        self.folder_id = folder_id  # flags.0?int
        self.q = q  # string
        self.offset_rate = offset_rate  # int
        self.offset_peer = offset_peer  # InputPeer
        self.offset_id = offset_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "SearchGlobal":
        flags = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 0) else None
        q = String.read(b)
        
        offset_rate = Int.read(b)
        
        offset_peer = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return SearchGlobal(q=q, offset_rate=offset_rate, offset_peer=offset_peer, offset_id=offset_id, limit=limit, folder_id=folder_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(String(self.q))
        
        b.write(Int(self.offset_rate))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
