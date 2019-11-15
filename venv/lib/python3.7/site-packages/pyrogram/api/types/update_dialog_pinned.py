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


class UpdateDialogPinned(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x6e6fe51c``

    Parameters:
        peer: Either :obj:`DialogPeer <pyrogram.api.types.DialogPeer>` or :obj:`DialogPeerFolder <pyrogram.api.types.DialogPeerFolder>`
        pinned (optional): ``bool``
        folder_id (optional): ``int`` ``32-bit``
    """

    __slots__ = ["peer", "pinned", "folder_id"]

    ID = 0x6e6fe51c
    QUALNAME = "types.UpdateDialogPinned"

    def __init__(self, *, peer, pinned: bool = None, folder_id: int = None):
        self.pinned = pinned  # flags.0?true
        self.folder_id = folder_id  # flags.1?int
        self.peer = peer  # DialogPeer

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateDialogPinned":
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        folder_id = Int.read(b) if flags & (1 << 1) else None
        peer = TLObject.read(b)
        
        return UpdateDialogPinned(peer=peer, pinned=pinned, folder_id=folder_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned is not None else 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        b.write(self.peer.write())
        
        return b.getvalue()
