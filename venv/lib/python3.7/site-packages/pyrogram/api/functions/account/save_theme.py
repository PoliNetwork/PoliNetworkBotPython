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


class SaveTheme(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf257106c``

    Parameters:
        theme: Either :obj:`InputTheme <pyrogram.api.types.InputTheme>` or :obj:`InputThemeSlug <pyrogram.api.types.InputThemeSlug>`
        unsave: ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["theme", "unsave"]

    ID = 0xf257106c
    QUALNAME = "functions.account.SaveTheme"

    def __init__(self, *, theme, unsave: bool):
        self.theme = theme  # InputTheme
        self.unsave = unsave  # Bool

    @staticmethod
    def read(b: BytesIO, *args) -> "SaveTheme":
        # No flags
        
        theme = TLObject.read(b)
        
        unsave = Bool.read(b)
        
        return SaveTheme(theme=theme, unsave=unsave)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.theme.write())
        
        b.write(Bool(self.unsave))
        
        return b.getvalue()
