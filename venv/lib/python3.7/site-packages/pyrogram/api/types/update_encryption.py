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


class UpdateEncryption(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xb4a2e88d``

    Parameters:
        chat: Either :obj:`EncryptedChatEmpty <pyrogram.api.types.EncryptedChatEmpty>`, :obj:`EncryptedChatWaiting <pyrogram.api.types.EncryptedChatWaiting>`, :obj:`EncryptedChatRequested <pyrogram.api.types.EncryptedChatRequested>`, :obj:`EncryptedChat <pyrogram.api.types.EncryptedChat>` or :obj:`EncryptedChatDiscarded <pyrogram.api.types.EncryptedChatDiscarded>`
        date: ``int`` ``32-bit``
    """

    __slots__ = ["chat", "date"]

    ID = 0xb4a2e88d
    QUALNAME = "types.UpdateEncryption"

    def __init__(self, *, chat, date: int):
        self.chat = chat  # EncryptedChat
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateEncryption":
        # No flags
        
        chat = TLObject.read(b)
        
        date = Int.read(b)
        
        return UpdateEncryption(chat=chat, date=date)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chat.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()
