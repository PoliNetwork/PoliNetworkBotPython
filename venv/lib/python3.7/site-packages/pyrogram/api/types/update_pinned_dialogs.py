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


class UpdatePinnedDialogs(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xfa0f3ca2``

    Parameters:
        folder_id (optional): ``int`` ``32-bit``
        order (optional): List of either :obj:`DialogPeer <pyrogram.api.types.DialogPeer>` or :obj:`DialogPeerFolder <pyrogram.api.types.DialogPeerFolder>`
    """

    __slots__ = ["folder_id", "order"]

    ID = 0xfa0f3ca2
    QUALNAME = "types.UpdatePinnedDialogs"

    def __init__(self, *, folder_id: int = None, order: list = None):
        self.folder_id = folder_id  # flags.1?int
        self.order = order  # flags.0?Vector<DialogPeer>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdatePinnedDialogs":
        flags = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 1) else None
        order = TLObject.read(b) if flags & (1 << 0) else []
        
        return UpdatePinnedDialogs(folder_id=folder_id, order=order)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.folder_id is not None else 0
        flags |= (1 << 0) if self.order is not None else 0
        b.write(Int(flags))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        if self.order is not None:
            b.write(Vector(self.order))
        
        return b.getvalue()
