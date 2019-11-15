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


class MessageMediaWebPage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xa32dd600``

    Parameters:
        webpage: Either :obj:`WebPageEmpty <pyrogram.api.types.WebPageEmpty>`, :obj:`WebPagePending <pyrogram.api.types.WebPagePending>`, :obj:`WebPage <pyrogram.api.types.WebPage>` or :obj:`WebPageNotModified <pyrogram.api.types.WebPageNotModified>`

    See Also:
        This object can be returned by :obj:`messages.GetWebPagePreview <pyrogram.api.functions.messages.GetWebPagePreview>` and :obj:`messages.UploadMedia <pyrogram.api.functions.messages.UploadMedia>`.
    """

    __slots__ = ["webpage"]

    ID = 0xa32dd600
    QUALNAME = "types.MessageMediaWebPage"

    def __init__(self, *, webpage):
        self.webpage = webpage  # WebPage

    @staticmethod
    def read(b: BytesIO, *args) -> "MessageMediaWebPage":
        # No flags
        
        webpage = TLObject.read(b)
        
        return MessageMediaWebPage(webpage=webpage)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.webpage.write())
        
        return b.getvalue()
