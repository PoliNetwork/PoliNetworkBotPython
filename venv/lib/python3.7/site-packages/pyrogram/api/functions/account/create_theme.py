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


class CreateTheme(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x2b7ffd7f``

    Parameters:
        slug: ``str``
        title: ``str``
        document: Either :obj:`InputDocumentEmpty <pyrogram.api.types.InputDocumentEmpty>` or :obj:`InputDocument <pyrogram.api.types.InputDocument>`

    Returns:
        Either :obj:`ThemeDocumentNotModified <pyrogram.api.types.ThemeDocumentNotModified>` or :obj:`Theme <pyrogram.api.types.Theme>`
    """

    __slots__ = ["slug", "title", "document"]

    ID = 0x2b7ffd7f
    QUALNAME = "functions.account.CreateTheme"

    def __init__(self, *, slug: str, title: str, document):
        self.slug = slug  # string
        self.title = title  # string
        self.document = document  # InputDocument

    @staticmethod
    def read(b: BytesIO, *args) -> "CreateTheme":
        # No flags
        
        slug = String.read(b)
        
        title = String.read(b)
        
        document = TLObject.read(b)
        
        return CreateTheme(slug=slug, title=title, document=document)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        b.write(self.document.write())
        
        return b.getvalue()
