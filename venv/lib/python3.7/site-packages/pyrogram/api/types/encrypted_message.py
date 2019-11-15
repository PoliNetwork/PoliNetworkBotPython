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


class EncryptedMessage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xed18c118``

    Parameters:
        random_id: ``int`` ``64-bit``
        chat_id: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        bytes: ``bytes``
        file: Either :obj:`EncryptedFileEmpty <pyrogram.api.types.EncryptedFileEmpty>` or :obj:`EncryptedFile <pyrogram.api.types.EncryptedFile>`
    """

    __slots__ = ["random_id", "chat_id", "date", "bytes", "file"]

    ID = 0xed18c118
    QUALNAME = "types.EncryptedMessage"

    def __init__(self, *, random_id: int, chat_id: int, date: int, bytes: bytes, file):
        self.random_id = random_id  # long
        self.chat_id = chat_id  # int
        self.date = date  # int
        self.bytes = bytes  # bytes
        self.file = file  # EncryptedFile

    @staticmethod
    def read(b: BytesIO, *args) -> "EncryptedMessage":
        # No flags
        
        random_id = Long.read(b)
        
        chat_id = Int.read(b)
        
        date = Int.read(b)
        
        bytes = Bytes.read(b)
        
        file = TLObject.read(b)
        
        return EncryptedMessage(random_id=random_id, chat_id=chat_id, date=date, bytes=bytes, file=file)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.random_id))
        
        b.write(Int(self.chat_id))
        
        b.write(Int(self.date))
        
        b.write(Bytes(self.bytes))
        
        b.write(self.file.write())
        
        return b.getvalue()
