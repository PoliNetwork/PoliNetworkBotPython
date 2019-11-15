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


class SendConfirmPhoneCode(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1b3faa88``

    Parameters:
        hash: ``str``
        settings: :obj:`CodeSettings <pyrogram.api.types.CodeSettings>`

    Returns:
        :obj:`auth.SentCode <pyrogram.api.types.auth.SentCode>`
    """

    __slots__ = ["hash", "settings"]

    ID = 0x1b3faa88
    QUALNAME = "functions.account.SendConfirmPhoneCode"

    def __init__(self, *, hash: str, settings):
        self.hash = hash  # string
        self.settings = settings  # CodeSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "SendConfirmPhoneCode":
        # No flags
        
        hash = String.read(b)
        
        settings = TLObject.read(b)
        
        return SendConfirmPhoneCode(hash=hash, settings=settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.hash))
        
        b.write(self.settings.write())
        
        return b.getvalue()
