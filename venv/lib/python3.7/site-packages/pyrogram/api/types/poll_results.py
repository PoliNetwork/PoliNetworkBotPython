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


class PollResults(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x5755785a``

    Parameters:
        min (optional): ``bool``
        results (optional): List of :obj:`PollAnswerVoters <pyrogram.api.types.PollAnswerVoters>`
        total_voters (optional): ``int`` ``32-bit``
    """

    __slots__ = ["min", "results", "total_voters"]

    ID = 0x5755785a
    QUALNAME = "types.PollResults"

    def __init__(self, *, min: bool = None, results: list = None, total_voters: int = None):
        self.min = min  # flags.0?true
        self.results = results  # flags.1?Vector<PollAnswerVoters>
        self.total_voters = total_voters  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args) -> "PollResults":
        flags = Int.read(b)
        
        min = True if flags & (1 << 0) else False
        results = TLObject.read(b) if flags & (1 << 1) else []
        
        total_voters = Int.read(b) if flags & (1 << 2) else None
        return PollResults(min=min, results=results, total_voters=total_voters)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.min is not None else 0
        flags |= (1 << 1) if self.results is not None else 0
        flags |= (1 << 2) if self.total_voters is not None else 0
        b.write(Int(flags))
        
        if self.results is not None:
            b.write(Vector(self.results))
        
        if self.total_voters is not None:
            b.write(Int(self.total_voters))
        
        return b.getvalue()
