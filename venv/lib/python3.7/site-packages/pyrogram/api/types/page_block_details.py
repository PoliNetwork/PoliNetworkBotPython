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


class PageBlockDetails(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x76768bed``

    Parameters:
        blocks: List of either :obj:`PageBlockUnsupported <pyrogram.api.types.PageBlockUnsupported>`, :obj:`PageBlockTitle <pyrogram.api.types.PageBlockTitle>`, :obj:`PageBlockSubtitle <pyrogram.api.types.PageBlockSubtitle>`, :obj:`PageBlockAuthorDate <pyrogram.api.types.PageBlockAuthorDate>`, :obj:`PageBlockHeader <pyrogram.api.types.PageBlockHeader>`, :obj:`PageBlockSubheader <pyrogram.api.types.PageBlockSubheader>`, :obj:`PageBlockParagraph <pyrogram.api.types.PageBlockParagraph>`, :obj:`PageBlockPreformatted <pyrogram.api.types.PageBlockPreformatted>`, :obj:`PageBlockFooter <pyrogram.api.types.PageBlockFooter>`, :obj:`PageBlockDivider <pyrogram.api.types.PageBlockDivider>`, :obj:`PageBlockAnchor <pyrogram.api.types.PageBlockAnchor>`, :obj:`PageBlockList <pyrogram.api.types.PageBlockList>`, :obj:`PageBlockBlockquote <pyrogram.api.types.PageBlockBlockquote>`, :obj:`PageBlockPullquote <pyrogram.api.types.PageBlockPullquote>`, :obj:`PageBlockPhoto <pyrogram.api.types.PageBlockPhoto>`, :obj:`PageBlockVideo <pyrogram.api.types.PageBlockVideo>`, :obj:`PageBlockCover <pyrogram.api.types.PageBlockCover>`, :obj:`PageBlockEmbed <pyrogram.api.types.PageBlockEmbed>`, :obj:`PageBlockEmbedPost <pyrogram.api.types.PageBlockEmbedPost>`, :obj:`PageBlockCollage <pyrogram.api.types.PageBlockCollage>`, :obj:`PageBlockSlideshow <pyrogram.api.types.PageBlockSlideshow>`, :obj:`PageBlockChannel <pyrogram.api.types.PageBlockChannel>`, :obj:`PageBlockAudio <pyrogram.api.types.PageBlockAudio>`, :obj:`PageBlockKicker <pyrogram.api.types.PageBlockKicker>`, :obj:`PageBlockTable <pyrogram.api.types.PageBlockTable>`, :obj:`PageBlockOrderedList <pyrogram.api.types.PageBlockOrderedList>`, :obj:`PageBlockDetails <pyrogram.api.types.PageBlockDetails>`, :obj:`PageBlockRelatedArticles <pyrogram.api.types.PageBlockRelatedArticles>` or :obj:`PageBlockMap <pyrogram.api.types.PageBlockMap>`
        title: Either :obj:`TextEmpty <pyrogram.api.types.TextEmpty>`, :obj:`TextPlain <pyrogram.api.types.TextPlain>`, :obj:`TextBold <pyrogram.api.types.TextBold>`, :obj:`TextItalic <pyrogram.api.types.TextItalic>`, :obj:`TextUnderline <pyrogram.api.types.TextUnderline>`, :obj:`TextStrike <pyrogram.api.types.TextStrike>`, :obj:`TextFixed <pyrogram.api.types.TextFixed>`, :obj:`TextUrl <pyrogram.api.types.TextUrl>`, :obj:`TextEmail <pyrogram.api.types.TextEmail>`, :obj:`TextConcat <pyrogram.api.types.TextConcat>`, :obj:`TextSubscript <pyrogram.api.types.TextSubscript>`, :obj:`TextSuperscript <pyrogram.api.types.TextSuperscript>`, :obj:`TextMarked <pyrogram.api.types.TextMarked>`, :obj:`TextPhone <pyrogram.api.types.TextPhone>`, :obj:`TextImage <pyrogram.api.types.TextImage>` or :obj:`TextAnchor <pyrogram.api.types.TextAnchor>`
        open (optional): ``bool``
    """

    __slots__ = ["blocks", "title", "open"]

    ID = 0x76768bed
    QUALNAME = "types.PageBlockDetails"

    def __init__(self, *, blocks: list, title, open: bool = None):
        self.open = open  # flags.0?true
        self.blocks = blocks  # Vector<PageBlock>
        self.title = title  # RichText

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockDetails":
        flags = Int.read(b)
        
        open = True if flags & (1 << 0) else False
        blocks = TLObject.read(b)
        
        title = TLObject.read(b)
        
        return PageBlockDetails(blocks=blocks, title=title, open=open)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.open is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.blocks))
        
        b.write(self.title.write())
        
        return b.getvalue()
