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


class ToggleDialogPin(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xa731e257``

    Parameters:
        peer: Either :obj:`InputDialogPeer <pyrogram.api.types.InputDialogPeer>` or :obj:`InputDialogPeerFolder <pyrogram.api.types.InputDialogPeerFolder>`
        pinned (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["peer", "pinned"]

    ID = 0xa731e257
    QUALNAME = "functions.messages.ToggleDialogPin"

    def __init__(self, *, peer, pinned: bool = None):
        self.pinned = pinned  # flags.0?true
        self.peer = peer  # InputDialogPeer

    @staticmethod
    def read(b: BytesIO, *args) -> "ToggleDialogPin":
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        return ToggleDialogPin(peer=peer, pinned=pinned)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pinned is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        return b.getvalue()
