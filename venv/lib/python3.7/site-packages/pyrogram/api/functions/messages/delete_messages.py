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


class DeleteMessages(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xe58e95d2``

    Parameters:
        id: List of ``int`` ``32-bit``
        revoke (optional): ``bool``

    Returns:
        :obj:`messages.AffectedMessages <pyrogram.api.types.messages.AffectedMessages>`
    """

    __slots__ = ["id", "revoke"]

    ID = 0xe58e95d2
    QUALNAME = "functions.messages.DeleteMessages"

    def __init__(self, *, id: list, revoke: bool = None):
        self.revoke = revoke  # flags.0?true
        self.id = id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args) -> "DeleteMessages":
        flags = Int.read(b)
        
        revoke = True if flags & (1 << 0) else False
        id = TLObject.read(b, Int)
        
        return DeleteMessages(id=id, revoke=revoke)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()
