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


class PollAnswerVoters(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x3b6ddad2``

    Parameters:
        option: ``bytes``
        voters: ``int`` ``32-bit``
        chosen (optional): ``bool``
    """

    __slots__ = ["option", "voters", "chosen"]

    ID = 0x3b6ddad2
    QUALNAME = "types.PollAnswerVoters"

    def __init__(self, *, option: bytes, voters: int, chosen: bool = None):
        self.chosen = chosen  # flags.0?true
        self.option = option  # bytes
        self.voters = voters  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "PollAnswerVoters":
        flags = Int.read(b)
        
        chosen = True if flags & (1 << 0) else False
        option = Bytes.read(b)
        
        voters = Int.read(b)
        
        return PollAnswerVoters(option=option, voters=voters, chosen=chosen)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.chosen is not None else 0
        b.write(Int(flags))
        
        b.write(Bytes(self.option))
        
        b.write(Int(self.voters))
        
        return b.getvalue()
