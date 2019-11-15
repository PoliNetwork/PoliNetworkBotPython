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


class WallPaper(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xa437c3ed``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        slug: ``str``
        document: Either :obj:`DocumentEmpty <pyrogram.api.types.DocumentEmpty>` or :obj:`Document <pyrogram.api.types.Document>`
        creator (optional): ``bool``
        default (optional): ``bool``
        pattern (optional): ``bool``
        dark (optional): ``bool``
        settings (optional): :obj:`WallPaperSettings <pyrogram.api.types.WallPaperSettings>`

    See Also:
        This object can be returned by :obj:`account.GetWallPaper <pyrogram.api.functions.account.GetWallPaper>` and :obj:`account.UploadWallPaper <pyrogram.api.functions.account.UploadWallPaper>`.
    """

    __slots__ = ["id", "access_hash", "slug", "document", "creator", "default", "pattern", "dark", "settings"]

    ID = 0xa437c3ed
    QUALNAME = "types.WallPaper"

    def __init__(self, *, id: int, access_hash: int, slug: str, document, creator: bool = None, default: bool = None, pattern: bool = None, dark: bool = None, settings=None):
        self.id = id  # long
        self.creator = creator  # flags.0?true
        self.default = default  # flags.1?true
        self.pattern = pattern  # flags.3?true
        self.dark = dark  # flags.4?true
        self.access_hash = access_hash  # long
        self.slug = slug  # string
        self.document = document  # Document
        self.settings = settings  # flags.2?WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "WallPaper":
        
        id = Long.read(b)
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        pattern = True if flags & (1 << 3) else False
        dark = True if flags & (1 << 4) else False
        access_hash = Long.read(b)
        
        slug = String.read(b)
        
        document = TLObject.read(b)
        
        settings = TLObject.read(b) if flags & (1 << 2) else None
        
        return WallPaper(id=id, access_hash=access_hash, slug=slug, document=document, creator=creator, default=default, pattern=pattern, dark=dark, settings=settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.creator is not None else 0
        flags |= (1 << 1) if self.default is not None else 0
        flags |= (1 << 3) if self.pattern is not None else 0
        flags |= (1 << 4) if self.dark is not None else 0
        flags |= (1 << 2) if self.settings is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.slug))
        
        b.write(self.document.write())
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        return b.getvalue()
