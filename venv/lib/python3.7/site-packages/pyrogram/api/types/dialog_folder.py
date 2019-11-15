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


class DialogFolder(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x71bd134c``

    Parameters:
        folder: :obj:`Folder <pyrogram.api.types.Folder>`
        peer: Either :obj:`PeerUser <pyrogram.api.types.PeerUser>`, :obj:`PeerChat <pyrogram.api.types.PeerChat>` or :obj:`PeerChannel <pyrogram.api.types.PeerChannel>`
        top_message: ``int`` ``32-bit``
        unread_muted_peers_count: ``int`` ``32-bit``
        unread_unmuted_peers_count: ``int`` ``32-bit``
        unread_muted_messages_count: ``int`` ``32-bit``
        unread_unmuted_messages_count: ``int`` ``32-bit``
        pinned (optional): ``bool``
    """

    __slots__ = ["folder", "peer", "top_message", "unread_muted_peers_count", "unread_unmuted_peers_count", "unread_muted_messages_count", "unread_unmuted_messages_count", "pinned"]

    ID = 0x71bd134c
    QUALNAME = "types.DialogFolder"

    def __init__(self, *, folder, peer, top_message: int, unread_muted_peers_count: int, unread_unmuted_peers_count: int, unread_muted_messages_count: int, unread_unmuted_messages_count: int, pinned: bool = None):
        self.pinned = pinned  # flags.2?true
        self.folder = folder  # Folder
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.unread_muted_peers_count = unread_muted_peers_count  # int
        self.unread_unmuted_peers_count = unread_unmuted_peers_count  # int
        self.unread_muted_messages_count = unread_muted_messages_count  # int
        self.unread_unmuted_messages_count = unread_unmuted_messages_count  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "DialogFolder":
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        folder = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        top_message = Int.read(b)
        
        unread_muted_peers_count = Int.read(b)
        
        unread_unmuted_peers_count = Int.read(b)
        
        unread_muted_messages_count = Int.read(b)
        
        unread_unmuted_messages_count = Int.read(b)
        
        return DialogFolder(folder=folder, peer=peer, top_message=top_message, unread_muted_peers_count=unread_muted_peers_count, unread_unmuted_peers_count=unread_unmuted_peers_count, unread_muted_messages_count=unread_muted_messages_count, unread_unmuted_messages_count=unread_unmuted_messages_count, pinned=pinned)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned is not None else 0
        b.write(Int(flags))
        
        b.write(self.folder.write())
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.unread_muted_peers_count))
        
        b.write(Int(self.unread_unmuted_peers_count))
        
        b.write(Int(self.unread_muted_messages_count))
        
        b.write(Int(self.unread_unmuted_messages_count))
        
        return b.getvalue()
