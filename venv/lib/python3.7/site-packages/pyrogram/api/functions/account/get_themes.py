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


class GetThemes(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x285946f8``

    Parameters:
        format: ``str``
        hash: ``int`` ``32-bit``

    Returns:
        Either :obj:`account.ThemesNotModified <pyrogram.api.types.account.ThemesNotModified>` or :obj:`account.Themes <pyrogram.api.types.account.Themes>`
    """

    __slots__ = ["format", "hash"]

    ID = 0x285946f8
    QUALNAME = "functions.account.GetThemes"

    def __init__(self, *, format: str, hash: int):
        self.format = format  # string
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetThemes":
        # No flags
        
        format = String.read(b)
        
        hash = Int.read(b)
        
        return GetThemes(format=format, hash=hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
