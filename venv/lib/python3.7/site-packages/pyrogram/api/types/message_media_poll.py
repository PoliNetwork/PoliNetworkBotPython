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


class MessageMediaPoll(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x4bd6e798``

    Parameters:
        poll: :obj:`Poll <pyrogram.api.types.Poll>`
        results: :obj:`PollResults <pyrogram.api.types.PollResults>`

    See Also:
        This object can be returned by :obj:`messages.GetWebPagePreview <pyrogram.api.functions.messages.GetWebPagePreview>` and :obj:`messages.UploadMedia <pyrogram.api.functions.messages.UploadMedia>`.
    """

    __slots__ = ["poll", "results"]

    ID = 0x4bd6e798
    QUALNAME = "types.MessageMediaPoll"

    def __init__(self, *, poll, results):
        self.poll = poll  # Poll
        self.results = results  # PollResults

    @staticmethod
    def read(b: BytesIO, *args) -> "MessageMediaPoll":
        # No flags
        
        poll = TLObject.read(b)
        
        results = TLObject.read(b)
        
        return MessageMediaPoll(poll=poll, results=results)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.poll.write())
        
        b.write(self.results.write())
        
        return b.getvalue()
