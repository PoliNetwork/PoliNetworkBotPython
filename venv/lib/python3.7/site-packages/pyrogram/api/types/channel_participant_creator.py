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


class ChannelParticipantCreator(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x808d15a4``

    Parameters:
        user_id: ``int`` ``32-bit``
        rank (optional): ``str``
    """

    __slots__ = ["user_id", "rank"]

    ID = 0x808d15a4
    QUALNAME = "types.ChannelParticipantCreator"

    def __init__(self, *, user_id: int, rank: str = None):
        self.user_id = user_id  # int
        self.rank = rank  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelParticipantCreator":
        flags = Int.read(b)
        
        user_id = Int.read(b)
        
        rank = String.read(b) if flags & (1 << 0) else None
        return ChannelParticipantCreator(user_id=user_id, rank=rank)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.user_id))
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()
