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


class EditChatTitle(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xdc452855``

    Parameters:
        chat_id: ``int`` ``32-bit``
        title: ``str``

    Returns:
        Either :obj:`UpdatesTooLong <pyrogram.api.types.UpdatesTooLong>`, :obj:`UpdateShortMessage <pyrogram.api.types.UpdateShortMessage>`, :obj:`UpdateShortChatMessage <pyrogram.api.types.UpdateShortChatMessage>`, :obj:`UpdateShort <pyrogram.api.types.UpdateShort>`, :obj:`UpdatesCombined <pyrogram.api.types.UpdatesCombined>`, :obj:`Update <pyrogram.api.types.Update>` or :obj:`UpdateShortSentMessage <pyrogram.api.types.UpdateShortSentMessage>`
    """

    __slots__ = ["chat_id", "title"]

    ID = 0xdc452855
    QUALNAME = "functions.messages.EditChatTitle"

    def __init__(self, *, chat_id: int, title: str):
        self.chat_id = chat_id  # int
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "EditChatTitle":
        # No flags
        
        chat_id = Int.read(b)
        
        title = String.read(b)
        
        return EditChatTitle(chat_id=chat_id, title=title)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.chat_id))
        
        b.write(String(self.title))
        
        return b.getvalue()
