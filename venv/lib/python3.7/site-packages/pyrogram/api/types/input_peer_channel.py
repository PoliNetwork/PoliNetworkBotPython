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


class InputPeerChannel(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x20adaef8``

    Parameters:
        channel_id: ``int`` ``32-bit``
        access_hash: ``int`` ``64-bit``
    """

    __slots__ = ["channel_id", "access_hash"]

    ID = 0x20adaef8
    QUALNAME = "types.InputPeerChannel"

    def __init__(self, *, channel_id: int, access_hash: int):
        self.channel_id = channel_id  # int
        self.access_hash = access_hash  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "InputPeerChannel":
        # No flags
        
        channel_id = Int.read(b)
        
        access_hash = Long.read(b)
        
        return InputPeerChannel(channel_id=channel_id, access_hash=access_hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.channel_id))
        
        b.write(Long(self.access_hash))
        
        return b.getvalue()
