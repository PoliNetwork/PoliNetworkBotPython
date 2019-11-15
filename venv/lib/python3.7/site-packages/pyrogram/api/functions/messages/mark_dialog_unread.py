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


class MarkDialogUnread(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xc286d98f``

    Parameters:
        peer: Either :obj:`InputDialogPeer <pyrogram.api.types.InputDialogPeer>` or :obj:`InputDialogPeerFolder <pyrogram.api.types.InputDialogPeerFolder>`
        unread (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["peer", "unread"]

    ID = 0xc286d98f
    QUALNAME = "functions.messages.MarkDialogUnread"

    def __init__(self, *, peer, unread: bool = None):
        self.unread = unread  # flags.0?true
        self.peer = peer  # InputDialogPeer

    @staticmethod
    def read(b: BytesIO, *args) -> "MarkDialogUnread":
        flags = Int.read(b)
        
        unread = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return MarkDialogUnread(peer=peer, unread=unread)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.unread is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
