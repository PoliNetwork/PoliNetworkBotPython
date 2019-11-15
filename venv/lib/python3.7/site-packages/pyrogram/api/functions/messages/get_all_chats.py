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


class GetAllChats(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xeba80ff0``

    Parameters:
        except_ids: List of ``int`` ``32-bit``

    Returns:
        Either :obj:`messages.Chats <pyrogram.api.types.messages.Chats>` or :obj:`messages.ChatsSlice <pyrogram.api.types.messages.ChatsSlice>`
    """

    __slots__ = ["except_ids"]

    ID = 0xeba80ff0
    QUALNAME = "functions.messages.GetAllChats"

    def __init__(self, *, except_ids: list):
        self.except_ids = except_ids  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args) -> "GetAllChats":
        # No flags
        
        except_ids = TLObject.read(b, Int)
        
        return GetAllChats(except_ids=except_ids)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.except_ids, Int))
        
        return b.getvalue()
