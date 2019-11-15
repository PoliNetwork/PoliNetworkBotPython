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


class Poll(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd5529d06``

    Parameters:
        id: ``int`` ``64-bit``
        question: ``str``
        answers: List of :obj:`PollAnswer <pyrogram.api.types.PollAnswer>`
        closed (optional): ``bool``
    """

    __slots__ = ["id", "question", "answers", "closed"]

    ID = 0xd5529d06
    QUALNAME = "types.Poll"

    def __init__(self, *, id: int, question: str, answers: list, closed: bool = None):
        self.id = id  # long
        self.closed = closed  # flags.0?true
        self.question = question  # string
        self.answers = answers  # Vector<PollAnswer>

    @staticmethod
    def read(b: BytesIO, *args) -> "Poll":
        
        id = Long.read(b)
        flags = Int.read(b)
        
        closed = True if flags & (1 << 0) else False
        question = String.read(b)
        
        answers = TLObject.read(b)
        
        return Poll(id=id, question=question, answers=answers, closed=closed)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(Long(self.id))
        flags = 0
        flags |= (1 << 0) if self.closed is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.question))
        
        b.write(Vector(self.answers))
        
        return b.getvalue()
