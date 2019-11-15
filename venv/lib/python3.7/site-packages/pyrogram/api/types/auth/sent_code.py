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


class SentCode(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x5e002502``

    Parameters:
        type: Either :obj:`auth.SentCodeTypeApp <pyrogram.api.types.auth.SentCodeTypeApp>`, :obj:`auth.SentCodeTypeSms <pyrogram.api.types.auth.SentCodeTypeSms>`, :obj:`auth.SentCodeTypeCall <pyrogram.api.types.auth.SentCodeTypeCall>` or :obj:`auth.SentCodeTypeFlashCall <pyrogram.api.types.auth.SentCodeTypeFlashCall>`
        phone_code_hash: ``str``
        next_type (optional): Either :obj:`auth.CodeTypeSms <pyrogram.api.types.auth.CodeTypeSms>`, :obj:`auth.CodeTypeCall <pyrogram.api.types.auth.CodeTypeCall>` or :obj:`auth.CodeTypeFlashCall <pyrogram.api.types.auth.CodeTypeFlashCall>`
        timeout (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by :obj:`auth.SendCode <pyrogram.api.functions.auth.SendCode>`, :obj:`auth.ResendCode <pyrogram.api.functions.auth.ResendCode>`, :obj:`account.SendChangePhoneCode <pyrogram.api.functions.account.SendChangePhoneCode>`, :obj:`account.SendConfirmPhoneCode <pyrogram.api.functions.account.SendConfirmPhoneCode>` and :obj:`account.SendVerifyPhoneCode <pyrogram.api.functions.account.SendVerifyPhoneCode>`.
    """

    __slots__ = ["type", "phone_code_hash", "next_type", "timeout"]

    ID = 0x5e002502
    QUALNAME = "types.auth.SentCode"

    def __init__(self, *, type, phone_code_hash: str, next_type=None, timeout: int = None):
        self.type = type  # auth.SentCodeType
        self.phone_code_hash = phone_code_hash  # string
        self.next_type = next_type  # flags.1?auth.CodeType
        self.timeout = timeout  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args) -> "SentCode":
        flags = Int.read(b)
        
        type = TLObject.read(b)
        
        phone_code_hash = String.read(b)
        
        next_type = TLObject.read(b) if flags & (1 << 1) else None
        
        timeout = Int.read(b) if flags & (1 << 2) else None
        return SentCode(type=type, phone_code_hash=phone_code_hash, next_type=next_type, timeout=timeout)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.next_type is not None else 0
        flags |= (1 << 2) if self.timeout is not None else 0
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        b.write(String(self.phone_code_hash))
        
        if self.next_type is not None:
            b.write(self.next_type.write())
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        return b.getvalue()
