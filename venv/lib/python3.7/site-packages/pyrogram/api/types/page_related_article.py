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


class PageRelatedArticle(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xb390dc08``

    Parameters:
        url: ``str``
        webpage_id: ``int`` ``64-bit``
        title (optional): ``str``
        description (optional): ``str``
        photo_id (optional): ``int`` ``64-bit``
        author (optional): ``str``
        published_date (optional): ``int`` ``32-bit``
    """

    __slots__ = ["url", "webpage_id", "title", "description", "photo_id", "author", "published_date"]

    ID = 0xb390dc08
    QUALNAME = "types.PageRelatedArticle"

    def __init__(self, *, url: str, webpage_id: int, title: str = None, description: str = None, photo_id: int = None, author: str = None, published_date: int = None):
        self.url = url  # string
        self.webpage_id = webpage_id  # long
        self.title = title  # flags.0?string
        self.description = description  # flags.1?string
        self.photo_id = photo_id  # flags.2?long
        self.author = author  # flags.3?string
        self.published_date = published_date  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args) -> "PageRelatedArticle":
        flags = Int.read(b)
        
        url = String.read(b)
        
        webpage_id = Long.read(b)
        
        title = String.read(b) if flags & (1 << 0) else None
        description = String.read(b) if flags & (1 << 1) else None
        photo_id = Long.read(b) if flags & (1 << 2) else None
        author = String.read(b) if flags & (1 << 3) else None
        published_date = Int.read(b) if flags & (1 << 4) else None
        return PageRelatedArticle(url=url, webpage_id=webpage_id, title=title, description=description, photo_id=photo_id, author=author, published_date=published_date)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.title is not None else 0
        flags |= (1 << 1) if self.description is not None else 0
        flags |= (1 << 2) if self.photo_id is not None else 0
        flags |= (1 << 3) if self.author is not None else 0
        flags |= (1 << 4) if self.published_date is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        b.write(Long(self.webpage_id))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo_id is not None:
            b.write(Long(self.photo_id))
        
        if self.author is not None:
            b.write(String(self.author))
        
        if self.published_date is not None:
            b.write(Int(self.published_date))
        
        return b.getvalue()
