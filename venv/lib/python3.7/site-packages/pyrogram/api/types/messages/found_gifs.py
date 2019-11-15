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


class FoundGifs(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x450a1c0a``

    Parameters:
        next_offset: ``int`` ``32-bit``
        results: List of either :obj:`FoundGif <pyrogram.api.types.FoundGif>` or :obj:`FoundGifCached <pyrogram.api.types.FoundGifCached>`

    See Also:
        This object can be returned by :obj:`messages.SearchGifs <pyrogram.api.functions.messages.SearchGifs>`.
    """

    __slots__ = ["next_offset", "results"]

    ID = 0x450a1c0a
    QUALNAME = "types.messages.FoundGifs"

    def __init__(self, *, next_offset: int, results: list):
        self.next_offset = next_offset  # int
        self.results = results  # Vector<FoundGif>

    @staticmethod
    def read(b: BytesIO, *args) -> "FoundGifs":
        # No flags
        
        next_offset = Int.read(b)
        
        results = TLObject.read(b)
        
        return FoundGifs(next_offset=next_offset, results=results)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.next_offset))
        
        b.write(Vector(self.results))
        
        return b.getvalue()
