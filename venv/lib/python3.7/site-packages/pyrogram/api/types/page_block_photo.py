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


class PageBlockPhoto(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1759c560``

    Parameters:
        photo_id: ``int`` ``64-bit``
        caption: :obj:`PageCaption <pyrogram.api.types.PageCaption>`
        url (optional): ``str``
        webpage_id (optional): ``int`` ``64-bit``
    """

    __slots__ = ["photo_id", "caption", "url", "webpage_id"]

    ID = 0x1759c560
    QUALNAME = "types.PageBlockPhoto"

    def __init__(self, *, photo_id: int, caption, url: str = None, webpage_id: int = None):
        self.photo_id = photo_id  # long
        self.caption = caption  # PageCaption
        self.url = url  # flags.0?string
        self.webpage_id = webpage_id  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockPhoto":
        flags = Int.read(b)
        
        photo_id = Long.read(b)
        
        caption = TLObject.read(b)
        
        url = String.read(b) if flags & (1 << 0) else None
        webpage_id = Long.read(b) if flags & (1 << 0) else None
        return PageBlockPhoto(photo_id=photo_id, caption=caption, url=url, webpage_id=webpage_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.url is not None else 0
        flags |= (1 << 0) if self.webpage_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.photo_id))
        
        b.write(self.caption.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.webpage_id is not None:
            b.write(Long(self.webpage_id))
        
        return b.getvalue()
