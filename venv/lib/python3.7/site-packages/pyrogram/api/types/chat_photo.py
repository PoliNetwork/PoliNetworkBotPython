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


class ChatPhoto(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x475cdbd5``

    Parameters:
        photo_small: :obj:`FileLocationToBeDeprecated <pyrogram.api.types.FileLocationToBeDeprecated>`
        photo_big: :obj:`FileLocationToBeDeprecated <pyrogram.api.types.FileLocationToBeDeprecated>`
        dc_id: ``int`` ``32-bit``
    """

    __slots__ = ["photo_small", "photo_big", "dc_id"]

    ID = 0x475cdbd5
    QUALNAME = "types.ChatPhoto"

    def __init__(self, *, photo_small, photo_big, dc_id: int):
        self.photo_small = photo_small  # FileLocation
        self.photo_big = photo_big  # FileLocation
        self.dc_id = dc_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "ChatPhoto":
        # No flags
        
        photo_small = TLObject.read(b)
        
        photo_big = TLObject.read(b)
        
        dc_id = Int.read(b)
        
        return ChatPhoto(photo_small=photo_small, photo_big=photo_big, dc_id=dc_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.photo_small.write())
        
        b.write(self.photo_big.write())
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()
