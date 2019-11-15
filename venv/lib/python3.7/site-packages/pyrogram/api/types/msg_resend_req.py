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


class MsgResendReq(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x7d861a08``

    Parameters:
        msg_ids: List of ``int`` ``64-bit``
    """

    __slots__ = ["msg_ids"]

    ID = 0x7d861a08
    QUALNAME = "types.MsgResendReq"

    def __init__(self, *, msg_ids: list):
        self.msg_ids = msg_ids  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args) -> "MsgResendReq":
        # No flags
        
        msg_ids = TLObject.read(b, Long)
        
        return MsgResendReq(msg_ids=msg_ids)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.msg_ids, Long))
        
        return b.getvalue()
