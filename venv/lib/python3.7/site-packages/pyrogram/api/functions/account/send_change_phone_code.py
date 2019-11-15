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


class SendChangePhoneCode(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x82574ae5``

    Parameters:
        phone_number: ``str``
        settings: :obj:`CodeSettings <pyrogram.api.types.CodeSettings>`

    Returns:
        :obj:`auth.SentCode <pyrogram.api.types.auth.SentCode>`
    """

    __slots__ = ["phone_number", "settings"]

    ID = 0x82574ae5
    QUALNAME = "functions.account.SendChangePhoneCode"

    def __init__(self, *, phone_number: str, settings):
        self.phone_number = phone_number  # string
        self.settings = settings  # CodeSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "SendChangePhoneCode":
        # No flags
        
        phone_number = String.read(b)
        
        settings = TLObject.read(b)
        
        return SendChangePhoneCode(phone_number=phone_number, settings=settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.phone_number))
        
        b.write(self.settings.write())
        
        return b.getvalue()
