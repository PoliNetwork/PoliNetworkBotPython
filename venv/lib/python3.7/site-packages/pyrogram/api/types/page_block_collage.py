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


class PageBlockCollage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x65a0fa4d``

    Parameters:
        items: List of either :obj:`PageBlockUnsupported <pyrogram.api.types.PageBlockUnsupported>`, :obj:`PageBlockTitle <pyrogram.api.types.PageBlockTitle>`, :obj:`PageBlockSubtitle <pyrogram.api.types.PageBlockSubtitle>`, :obj:`PageBlockAuthorDate <pyrogram.api.types.PageBlockAuthorDate>`, :obj:`PageBlockHeader <pyrogram.api.types.PageBlockHeader>`, :obj:`PageBlockSubheader <pyrogram.api.types.PageBlockSubheader>`, :obj:`PageBlockParagraph <pyrogram.api.types.PageBlockParagraph>`, :obj:`PageBlockPreformatted <pyrogram.api.types.PageBlockPreformatted>`, :obj:`PageBlockFooter <pyrogram.api.types.PageBlockFooter>`, :obj:`PageBlockDivider <pyrogram.api.types.PageBlockDivider>`, :obj:`PageBlockAnchor <pyrogram.api.types.PageBlockAnchor>`, :obj:`PageBlockList <pyrogram.api.types.PageBlockList>`, :obj:`PageBlockBlockquote <pyrogram.api.types.PageBlockBlockquote>`, :obj:`PageBlockPullquote <pyrogram.api.types.PageBlockPullquote>`, :obj:`PageBlockPhoto <pyrogram.api.types.PageBlockPhoto>`, :obj:`PageBlockVideo <pyrogram.api.types.PageBlockVideo>`, :obj:`PageBlockCover <pyrogram.api.types.PageBlockCover>`, :obj:`PageBlockEmbed <pyrogram.api.types.PageBlockEmbed>`, :obj:`PageBlockEmbedPost <pyrogram.api.types.PageBlockEmbedPost>`, :obj:`PageBlockCollage <pyrogram.api.types.PageBlockCollage>`, :obj:`PageBlockSlideshow <pyrogram.api.types.PageBlockSlideshow>`, :obj:`PageBlockChannel <pyrogram.api.types.PageBlockChannel>`, :obj:`PageBlockAudio <pyrogram.api.types.PageBlockAudio>`, :obj:`PageBlockKicker <pyrogram.api.types.PageBlockKicker>`, :obj:`PageBlockTable <pyrogram.api.types.PageBlockTable>`, :obj:`PageBlockOrderedList <pyrogram.api.types.PageBlockOrderedList>`, :obj:`PageBlockDetails <pyrogram.api.types.PageBlockDetails>`, :obj:`PageBlockRelatedArticles <pyrogram.api.types.PageBlockRelatedArticles>` or :obj:`PageBlockMap <pyrogram.api.types.PageBlockMap>`
        caption: :obj:`PageCaption <pyrogram.api.types.PageCaption>`
    """

    __slots__ = ["items", "caption"]

    ID = 0x65a0fa4d
    QUALNAME = "types.PageBlockCollage"

    def __init__(self, *, items: list, caption):
        self.items = items  # Vector<PageBlock>
        self.caption = caption  # PageCaption

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockCollage":
        # No flags
        
        items = TLObject.read(b)
        
        caption = TLObject.read(b)
        
        return PageBlockCollage(items=items, caption=caption)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.items))
        
        b.write(self.caption.write())
        
        return b.getvalue()
