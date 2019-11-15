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


class FinishTakeoutSession(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1d2652ee``

    Parameters:
        success (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["success"]

    ID = 0x1d2652ee
    QUALNAME = "functions.account.FinishTakeoutSession"

    def __init__(self, *, success: bool = None):
        self.success = success  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args) -> "FinishTakeoutSession":
        flags = Int.read(b)
        
        success = True if flags & (1 << 0) else False
        return FinishTakeoutSession(success=success)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.success is not None else 0
        b.write(Int(flags))
        
        return b.getvalue()
