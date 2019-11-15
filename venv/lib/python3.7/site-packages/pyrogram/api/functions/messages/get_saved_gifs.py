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


class GetSavedGifs(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x83bf3d52``

    Parameters:
        hash: ``int`` ``32-bit``

    Returns:
        Either :obj:`messages.SavedGifsNotModified <pyrogram.api.types.messages.SavedGifsNotModified>` or :obj:`messages.SavedGifs <pyrogram.api.types.messages.SavedGifs>`
    """

    __slots__ = ["hash"]

    ID = 0x83bf3d52
    QUALNAME = "functions.messages.GetSavedGifs"

    def __init__(self, *, hash: int):
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetSavedGifs":
        # No flags
        
        hash = Int.read(b)
        
        return GetSavedGifs(hash=hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        return b.getvalue()
