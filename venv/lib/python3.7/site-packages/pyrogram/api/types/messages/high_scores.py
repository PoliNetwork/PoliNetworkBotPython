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


class HighScores(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x9a3bfd99``

    Parameters:
        scores: List of :obj:`HighScore <pyrogram.api.types.HighScore>`
        users: List of either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`

    See Also:
        This object can be returned by :obj:`messages.GetGameHighScores <pyrogram.api.functions.messages.GetGameHighScores>` and :obj:`messages.GetInlineGameHighScores <pyrogram.api.functions.messages.GetInlineGameHighScores>`.
    """

    __slots__ = ["scores", "users"]

    ID = 0x9a3bfd99
    QUALNAME = "types.messages.HighScores"

    def __init__(self, *, scores: list, users: list):
        self.scores = scores  # Vector<HighScore>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args) -> "HighScores":
        # No flags
        
        scores = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return HighScores(scores=scores, users=users)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.scores))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
