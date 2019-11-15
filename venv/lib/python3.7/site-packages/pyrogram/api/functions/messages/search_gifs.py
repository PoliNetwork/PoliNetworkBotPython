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


class SearchGifs(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xbf9a776b``

    Parameters:
        q: ``str``
        offset: ``int`` ``32-bit``

    Returns:
        :obj:`messages.FoundGifs <pyrogram.api.types.messages.FoundGifs>`
    """

    __slots__ = ["q", "offset"]

    ID = 0xbf9a776b
    QUALNAME = "functions.messages.SearchGifs"

    def __init__(self, *, q: str, offset: int):
        self.q = q  # string
        self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "SearchGifs":
        # No flags
        
        q = String.read(b)
        
        offset = Int.read(b)
        
        return SearchGifs(q=q, offset=offset)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.q))
        
        b.write(Int(self.offset))
        
        return b.getvalue()
