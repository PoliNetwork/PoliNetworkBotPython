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


class ChatOnlines(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf041e250``

    Parameters:
        onlines: ``int`` ``32-bit``

    See Also:
        This object can be returned by :obj:`messages.GetOnlines <pyrogram.api.functions.messages.GetOnlines>`.
    """

    __slots__ = ["onlines"]

    ID = 0xf041e250
    QUALNAME = "types.ChatOnlines"

    def __init__(self, *, onlines: int):
        self.onlines = onlines  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "ChatOnlines":
        # No flags
        
        onlines = Int.read(b)
        
        return ChatOnlines(onlines=onlines)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.onlines))
        
        return b.getvalue()
