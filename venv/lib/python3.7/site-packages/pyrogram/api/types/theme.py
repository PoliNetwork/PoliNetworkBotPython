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


class Theme(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf7d90ce0``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        slug: ``str``
        title: ``str``
        installs_count: ``int`` ``32-bit``
        creator (optional): ``bool``
        default (optional): ``bool``
        document (optional): Either :obj:`DocumentEmpty <pyrogram.api.types.DocumentEmpty>` or :obj:`Document <pyrogram.api.types.Document>`

    See Also:
        This object can be returned by :obj:`account.CreateTheme <pyrogram.api.functions.account.CreateTheme>`, :obj:`account.UpdateTheme <pyrogram.api.functions.account.UpdateTheme>` and :obj:`account.GetTheme <pyrogram.api.functions.account.GetTheme>`.
    """

    __slots__ = ["id", "access_hash", "slug", "title", "installs_count", "creator", "default", "document"]

    ID = 0xf7d90ce0
    QUALNAME = "types.Theme"

    def __init__(self, *, id: int, access_hash: int, slug: str, title: str, installs_count: int, creator: bool = None, default: bool = None, document=None):
        self.creator = creator  # flags.0?true
        self.default = default  # flags.1?true
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.slug = slug  # string
        self.title = title  # string
        self.document = document  # flags.2?Document
        self.installs_count = installs_count  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "Theme":
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        default = True if flags & (1 << 1) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        slug = String.read(b)
        
        title = String.read(b)
        
        document = TLObject.read(b) if flags & (1 << 2) else None
        
        installs_count = Int.read(b)
        
        return Theme(id=id, access_hash=access_hash, slug=slug, title=title, installs_count=installs_count, creator=creator, default=default, document=document)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator is not None else 0
        flags |= (1 << 1) if self.default is not None else 0
        flags |= (1 << 2) if self.document is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        if self.document is not None:
            b.write(self.document.write())
        
        b.write(Int(self.installs_count))
        
        return b.getvalue()
