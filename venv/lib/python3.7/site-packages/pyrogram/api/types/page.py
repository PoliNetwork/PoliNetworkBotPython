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


class Page(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xae891bec``

    Parameters:
        url: ``str``
        blocks: List of either :obj:`PageBlockUnsupported <pyrogram.api.types.PageBlockUnsupported>`, :obj:`PageBlockTitle <pyrogram.api.types.PageBlockTitle>`, :obj:`PageBlockSubtitle <pyrogram.api.types.PageBlockSubtitle>`, :obj:`PageBlockAuthorDate <pyrogram.api.types.PageBlockAuthorDate>`, :obj:`PageBlockHeader <pyrogram.api.types.PageBlockHeader>`, :obj:`PageBlockSubheader <pyrogram.api.types.PageBlockSubheader>`, :obj:`PageBlockParagraph <pyrogram.api.types.PageBlockParagraph>`, :obj:`PageBlockPreformatted <pyrogram.api.types.PageBlockPreformatted>`, :obj:`PageBlockFooter <pyrogram.api.types.PageBlockFooter>`, :obj:`PageBlockDivider <pyrogram.api.types.PageBlockDivider>`, :obj:`PageBlockAnchor <pyrogram.api.types.PageBlockAnchor>`, :obj:`PageBlockList <pyrogram.api.types.PageBlockList>`, :obj:`PageBlockBlockquote <pyrogram.api.types.PageBlockBlockquote>`, :obj:`PageBlockPullquote <pyrogram.api.types.PageBlockPullquote>`, :obj:`PageBlockPhoto <pyrogram.api.types.PageBlockPhoto>`, :obj:`PageBlockVideo <pyrogram.api.types.PageBlockVideo>`, :obj:`PageBlockCover <pyrogram.api.types.PageBlockCover>`, :obj:`PageBlockEmbed <pyrogram.api.types.PageBlockEmbed>`, :obj:`PageBlockEmbedPost <pyrogram.api.types.PageBlockEmbedPost>`, :obj:`PageBlockCollage <pyrogram.api.types.PageBlockCollage>`, :obj:`PageBlockSlideshow <pyrogram.api.types.PageBlockSlideshow>`, :obj:`PageBlockChannel <pyrogram.api.types.PageBlockChannel>`, :obj:`PageBlockAudio <pyrogram.api.types.PageBlockAudio>`, :obj:`PageBlockKicker <pyrogram.api.types.PageBlockKicker>`, :obj:`PageBlockTable <pyrogram.api.types.PageBlockTable>`, :obj:`PageBlockOrderedList <pyrogram.api.types.PageBlockOrderedList>`, :obj:`PageBlockDetails <pyrogram.api.types.PageBlockDetails>`, :obj:`PageBlockRelatedArticles <pyrogram.api.types.PageBlockRelatedArticles>` or :obj:`PageBlockMap <pyrogram.api.types.PageBlockMap>`
        photos: List of either :obj:`PhotoEmpty <pyrogram.api.types.PhotoEmpty>` or :obj:`Photo <pyrogram.api.types.Photo>`
        documents: List of either :obj:`DocumentEmpty <pyrogram.api.types.DocumentEmpty>` or :obj:`Document <pyrogram.api.types.Document>`
        part (optional): ``bool``
        rtl (optional): ``bool``
        v2 (optional): ``bool``
    """

    __slots__ = ["url", "blocks", "photos", "documents", "part", "rtl", "v2"]

    ID = 0xae891bec
    QUALNAME = "types.Page"

    def __init__(self, *, url: str, blocks: list, photos: list, documents: list, part: bool = None, rtl: bool = None, v2: bool = None):
        self.part = part  # flags.0?true
        self.rtl = rtl  # flags.1?true
        self.v2 = v2  # flags.2?true
        self.url = url  # string
        self.blocks = blocks  # Vector<PageBlock>
        self.photos = photos  # Vector<Photo>
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args) -> "Page":
        flags = Int.read(b)
        
        part = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 1) else False
        v2 = True if flags & (1 << 2) else False
        url = String.read(b)
        
        blocks = TLObject.read(b)
        
        photos = TLObject.read(b)
        
        documents = TLObject.read(b)
        
        return Page(url=url, blocks=blocks, photos=photos, documents=documents, part=part, rtl=rtl, v2=v2)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.part is not None else 0
        flags |= (1 << 1) if self.rtl is not None else 0
        flags |= (1 << 2) if self.v2 is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        b.write(Vector(self.blocks))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
