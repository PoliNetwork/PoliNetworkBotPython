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


class GetRecentStickers(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x5ea192c9``

    Parameters:
        hash: ``int`` ``32-bit``
        attached (optional): ``bool``

    Returns:
        Either :obj:`messages.RecentStickersNotModified <pyrogram.api.types.messages.RecentStickersNotModified>` or :obj:`messages.RecentStickers <pyrogram.api.types.messages.RecentStickers>`
    """

    __slots__ = ["hash", "attached"]

    ID = 0x5ea192c9
    QUALNAME = "functions.messages.GetRecentStickers"

    def __init__(self, *, hash: int, attached: bool = None):
        self.attached = attached  # flags.0?true
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetRecentStickers":
        flags = Int.read(b)
        
        attached = True if flags & (1 << 0) else False
        hash = Int.read(b)
        
        return GetRecentStickers(hash=hash, attached=attached)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.attached is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
