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


class InputFileLocation(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xdfdaabe1``

    Parameters:
        volume_id: ``int`` ``64-bit``
        local_id: ``int`` ``32-bit``
        secret: ``int`` ``64-bit``
        file_reference: ``bytes``
    """

    __slots__ = ["volume_id", "local_id", "secret", "file_reference"]

    ID = 0xdfdaabe1
    QUALNAME = "types.InputFileLocation"

    def __init__(self, *, volume_id: int, local_id: int, secret: int, file_reference: bytes):
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int
        self.secret = secret  # long
        self.file_reference = file_reference  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "InputFileLocation":
        # No flags
        
        volume_id = Long.read(b)
        
        local_id = Int.read(b)
        
        secret = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        return InputFileLocation(volume_id=volume_id, local_id=local_id, secret=secret, file_reference=file_reference)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.volume_id))
        
        b.write(Int(self.local_id))
        
        b.write(Long(self.secret))
        
        b.write(Bytes(self.file_reference))
        
        return b.getvalue()
