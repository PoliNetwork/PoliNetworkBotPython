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


class ReorderPinnedDialogs(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x3b1adf37``

    Parameters:
        folder_id: ``int`` ``32-bit``
        order: List of either :obj:`InputDialogPeer <pyrogram.api.types.InputDialogPeer>` or :obj:`InputDialogPeerFolder <pyrogram.api.types.InputDialogPeerFolder>`
        force (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["folder_id", "order", "force"]

    ID = 0x3b1adf37
    QUALNAME = "functions.messages.ReorderPinnedDialogs"

    def __init__(self, *, folder_id: int, order: list, force: bool = None):
        self.force = force  # flags.0?true
        self.folder_id = folder_id  # int
        self.order = order  # Vector<InputDialogPeer>

    @staticmethod
    def read(b: BytesIO, *args) -> "ReorderPinnedDialogs":
        flags = Int.read(b)
        
        force = True if flags & (1 << 0) else False
        folder_id = Int.read(b)
        
        order = TLObject.read(b)
        
        return ReorderPinnedDialogs(folder_id=folder_id, order=order, force=force)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.force is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.folder_id))
        
        b.write(Vector(self.order))
        
        return b.getvalue()
