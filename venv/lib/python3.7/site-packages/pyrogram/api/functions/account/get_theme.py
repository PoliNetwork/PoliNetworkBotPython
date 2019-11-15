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


class GetTheme(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x8d9d742b``

    Parameters:
        format: ``str``
        theme: Either :obj:`InputTheme <pyrogram.api.types.InputTheme>` or :obj:`InputThemeSlug <pyrogram.api.types.InputThemeSlug>`
        document_id: ``int`` ``64-bit``

    Returns:
        Either :obj:`ThemeDocumentNotModified <pyrogram.api.types.ThemeDocumentNotModified>` or :obj:`Theme <pyrogram.api.types.Theme>`
    """

    __slots__ = ["format", "theme", "document_id"]

    ID = 0x8d9d742b
    QUALNAME = "functions.account.GetTheme"

    def __init__(self, *, format: str, theme, document_id: int):
        self.format = format  # string
        self.theme = theme  # InputTheme
        self.document_id = document_id  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "GetTheme":
        # No flags
        
        format = String.read(b)
        
        theme = TLObject.read(b)
        
        document_id = Long.read(b)
        
        return GetTheme(format=format, theme=theme, document_id=document_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        b.write(Long(self.document_id))
        
        return b.getvalue()
