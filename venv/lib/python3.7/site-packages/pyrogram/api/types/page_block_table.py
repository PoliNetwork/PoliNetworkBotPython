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


class PageBlockTable(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xbf4dea82``

    Parameters:
        title: Either :obj:`TextEmpty <pyrogram.api.types.TextEmpty>`, :obj:`TextPlain <pyrogram.api.types.TextPlain>`, :obj:`TextBold <pyrogram.api.types.TextBold>`, :obj:`TextItalic <pyrogram.api.types.TextItalic>`, :obj:`TextUnderline <pyrogram.api.types.TextUnderline>`, :obj:`TextStrike <pyrogram.api.types.TextStrike>`, :obj:`TextFixed <pyrogram.api.types.TextFixed>`, :obj:`TextUrl <pyrogram.api.types.TextUrl>`, :obj:`TextEmail <pyrogram.api.types.TextEmail>`, :obj:`TextConcat <pyrogram.api.types.TextConcat>`, :obj:`TextSubscript <pyrogram.api.types.TextSubscript>`, :obj:`TextSuperscript <pyrogram.api.types.TextSuperscript>`, :obj:`TextMarked <pyrogram.api.types.TextMarked>`, :obj:`TextPhone <pyrogram.api.types.TextPhone>`, :obj:`TextImage <pyrogram.api.types.TextImage>` or :obj:`TextAnchor <pyrogram.api.types.TextAnchor>`
        rows: List of :obj:`PageTableRow <pyrogram.api.types.PageTableRow>`
        bordered (optional): ``bool``
        striped (optional): ``bool``
    """

    __slots__ = ["title", "rows", "bordered", "striped"]

    ID = 0xbf4dea82
    QUALNAME = "types.PageBlockTable"

    def __init__(self, *, title, rows: list, bordered: bool = None, striped: bool = None):
        self.bordered = bordered  # flags.0?true
        self.striped = striped  # flags.1?true
        self.title = title  # RichText
        self.rows = rows  # Vector<PageTableRow>

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockTable":
        flags = Int.read(b)
        
        bordered = True if flags & (1 << 0) else False
        striped = True if flags & (1 << 1) else False
        title = TLObject.read(b)
        
        rows = TLObject.read(b)
        
        return PageBlockTable(title=title, rows=rows, bordered=bordered, striped=striped)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.bordered is not None else 0
        flags |= (1 << 1) if self.striped is not None else 0
        b.write(Int(flags))
        
        b.write(self.title.write())
        
        b.write(Vector(self.rows))
        
        return b.getvalue()
