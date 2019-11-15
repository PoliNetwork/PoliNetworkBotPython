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


class SearchCounter(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xe844ebff``

    Parameters:
        filter: Either :obj:`InputMessagesFilterEmpty <pyrogram.api.types.InputMessagesFilterEmpty>`, :obj:`InputMessagesFilterPhotos <pyrogram.api.types.InputMessagesFilterPhotos>`, :obj:`InputMessagesFilterVideo <pyrogram.api.types.InputMessagesFilterVideo>`, :obj:`InputMessagesFilterPhotoVideo <pyrogram.api.types.InputMessagesFilterPhotoVideo>`, :obj:`InputMessagesFilterDocument <pyrogram.api.types.InputMessagesFilterDocument>`, :obj:`InputMessagesFilterUrl <pyrogram.api.types.InputMessagesFilterUrl>`, :obj:`InputMessagesFilterGif <pyrogram.api.types.InputMessagesFilterGif>`, :obj:`InputMessagesFilterVoice <pyrogram.api.types.InputMessagesFilterVoice>`, :obj:`InputMessagesFilterMusic <pyrogram.api.types.InputMessagesFilterMusic>`, :obj:`InputMessagesFilterChatPhotos <pyrogram.api.types.InputMessagesFilterChatPhotos>`, :obj:`InputMessagesFilterPhoneCalls <pyrogram.api.types.InputMessagesFilterPhoneCalls>`, :obj:`InputMessagesFilterRoundVoice <pyrogram.api.types.InputMessagesFilterRoundVoice>`, :obj:`InputMessagesFilterRoundVideo <pyrogram.api.types.InputMessagesFilterRoundVideo>`, :obj:`InputMessagesFilterMyMentions <pyrogram.api.types.InputMessagesFilterMyMentions>`, :obj:`InputMessagesFilterGeo <pyrogram.api.types.InputMessagesFilterGeo>` or :obj:`InputMessagesFilterContacts <pyrogram.api.types.InputMessagesFilterContacts>`
        count: ``int`` ``32-bit``
        inexact (optional): ``bool``

    See Also:
        This object can be returned by :obj:`messages.GetSearchCounters <pyrogram.api.functions.messages.GetSearchCounters>`.
    """

    __slots__ = ["filter", "count", "inexact"]

    ID = 0xe844ebff
    QUALNAME = "types.messages.SearchCounter"

    def __init__(self, *, filter, count: int, inexact: bool = None):
        self.inexact = inexact  # flags.1?true
        self.filter = filter  # MessagesFilter
        self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "SearchCounter":
        flags = Int.read(b)
        
        inexact = True if flags & (1 << 1) else False
        filter = TLObject.read(b)
        
        count = Int.read(b)
        
        return SearchCounter(filter=filter, count=count, inexact=inexact)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.inexact is not None else 0
        b.write(Int(flags))
        
        b.write(self.filter.write())
        
        b.write(Int(self.count))
        
        return b.getvalue()
