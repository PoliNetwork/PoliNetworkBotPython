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


class UpdateTheme(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x3b8ea202``

    Parameters:
        format: ``str``
        theme: Either :obj:`InputTheme <pyrogram.api.types.InputTheme>` or :obj:`InputThemeSlug <pyrogram.api.types.InputThemeSlug>`
        slug (optional): ``str``
        title (optional): ``str``
        document (optional): Either :obj:`InputDocumentEmpty <pyrogram.api.types.InputDocumentEmpty>` or :obj:`InputDocument <pyrogram.api.types.InputDocument>`

    Returns:
        Either :obj:`ThemeDocumentNotModified <pyrogram.api.types.ThemeDocumentNotModified>` or :obj:`Theme <pyrogram.api.types.Theme>`
    """

    __slots__ = ["format", "theme", "slug", "title", "document"]

    ID = 0x3b8ea202
    QUALNAME = "functions.account.UpdateTheme"

    def __init__(self, *, format: str, theme, slug: str = None, title: str = None, document=None):
        self.format = format  # string
        self.theme = theme  # InputTheme
        self.slug = slug  # flags.0?string
        self.title = title  # flags.1?string
        self.document = document  # flags.2?InputDocument

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateTheme":
        flags = Int.read(b)
        
        format = String.read(b)
        
        theme = TLObject.read(b)
        
        slug = String.read(b) if flags & (1 << 0) else None
        title = String.read(b) if flags & (1 << 1) else None
        document = TLObject.read(b) if flags & (1 << 2) else None
        
        return UpdateTheme(format=format, theme=theme, slug=slug, title=title, document=document)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.slug is not None else 0
        flags |= (1 << 1) if self.title is not None else 0
        flags |= (1 << 2) if self.document is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        if self.slug is not None:
            b.write(String(self.slug))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        return b.getvalue()
