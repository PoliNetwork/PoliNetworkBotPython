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


class GetInlineGameHighScores(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x0f635e1b``

    Parameters:
        id: :obj:`InputBotInlineMessageID <pyrogram.api.types.InputBotInlineMessageID>`
        user_id: Either :obj:`InputUserEmpty <pyrogram.api.types.InputUserEmpty>`, :obj:`InputUserSelf <pyrogram.api.types.InputUserSelf>`, :obj:`InputUser <pyrogram.api.types.InputUser>` or :obj:`InputUserFromMessage <pyrogram.api.types.InputUserFromMessage>`

    Returns:
        :obj:`messages.HighScores <pyrogram.api.types.messages.HighScores>`
    """

    __slots__ = ["id", "user_id"]

    ID = 0x0f635e1b
    QUALNAME = "functions.messages.GetInlineGameHighScores"

    def __init__(self, *, id, user_id):
        self.id = id  # InputBotInlineMessageID
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args) -> "GetInlineGameHighScores":
        # No flags
        
        id = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return GetInlineGameHighScores(id=id, user_id=user_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
