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


class Themes(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x7f676421``

    Parameters:
        hash: ``int`` ``32-bit``
        themes: List of either :obj:`ThemeDocumentNotModified <pyrogram.api.types.ThemeDocumentNotModified>` or :obj:`Theme <pyrogram.api.types.Theme>`

    See Also:
        This object can be returned by :obj:`account.GetThemes <pyrogram.api.functions.account.GetThemes>`.
    """

    __slots__ = ["hash", "themes"]

    ID = 0x7f676421
    QUALNAME = "types.account.Themes"

    def __init__(self, *, hash: int, themes: list):
        self.hash = hash  # int
        self.themes = themes  # Vector<Theme>

    @staticmethod
    def read(b: BytesIO, *args) -> "Themes":
        # No flags
        
        hash = Int.read(b)
        
        themes = TLObject.read(b)
        
        return Themes(hash=hash, themes=themes)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(Vector(self.themes))
        
        return b.getvalue()
