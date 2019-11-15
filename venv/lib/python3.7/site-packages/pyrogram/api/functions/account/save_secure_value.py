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


class SaveSecureValue(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x899fe31d``

    Parameters:
        value: :obj:`InputSecureValue <pyrogram.api.types.InputSecureValue>`
        secure_secret_id: ``int`` ``64-bit``

    Returns:
        :obj:`SecureValue <pyrogram.api.types.SecureValue>`
    """

    __slots__ = ["value", "secure_secret_id"]

    ID = 0x899fe31d
    QUALNAME = "functions.account.SaveSecureValue"

    def __init__(self, *, value, secure_secret_id: int):
        self.value = value  # InputSecureValue
        self.secure_secret_id = secure_secret_id  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "SaveSecureValue":
        # No flags
        
        value = TLObject.read(b)
        
        secure_secret_id = Long.read(b)
        
        return SaveSecureValue(value=value, secure_secret_id=secure_secret_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.value.write())
        
        b.write(Long(self.secure_secret_id))
        
        return b.getvalue()
