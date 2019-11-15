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


class DropTempAuthKeys(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x8e48a188``

    Parameters:
        except_auth_keys: List of ``int`` ``64-bit``

    Returns:
        ``bool``
    """

    __slots__ = ["except_auth_keys"]

    ID = 0x8e48a188
    QUALNAME = "functions.auth.DropTempAuthKeys"

    def __init__(self, *, except_auth_keys: list):
        self.except_auth_keys = except_auth_keys  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args) -> "DropTempAuthKeys":
        # No flags
        
        except_auth_keys = TLObject.read(b, Long)
        
        return DropTempAuthKeys(except_auth_keys=except_auth_keys)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.except_auth_keys, Long))
        
        return b.getvalue()
