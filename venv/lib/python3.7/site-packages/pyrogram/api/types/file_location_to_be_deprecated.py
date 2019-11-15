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


class FileLocationToBeDeprecated(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xbc7fc6cd``

    Parameters:
        volume_id: ``int`` ``64-bit``
        local_id: ``int`` ``32-bit``
    """

    __slots__ = ["volume_id", "local_id"]

    ID = 0xbc7fc6cd
    QUALNAME = "types.FileLocationToBeDeprecated"

    def __init__(self, *, volume_id: int, local_id: int):
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "FileLocationToBeDeprecated":
        # No flags
        
        volume_id = Long.read(b)
        
        local_id = Int.read(b)
        
        return FileLocationToBeDeprecated(volume_id=volume_id, local_id=local_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.volume_id))
        
        b.write(Int(self.local_id))
        
        return b.getvalue()
