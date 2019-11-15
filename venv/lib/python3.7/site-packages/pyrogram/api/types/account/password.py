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


class Password(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xad2641f8``

    Parameters:
        new_algo: Either :obj:`PasswordKdfAlgoUnknown <pyrogram.api.types.PasswordKdfAlgoUnknown>` or :obj:`PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow <pyrogram.api.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow>`
        new_secure_algo: Either :obj:`SecurePasswordKdfAlgoUnknown <pyrogram.api.types.SecurePasswordKdfAlgoUnknown>`, :obj:`SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000 <pyrogram.api.types.SecurePasswordKdfAlgoPBKDF2HMACSHA512iter100000>` or :obj:`SecurePasswordKdfAlgoSHA512 <pyrogram.api.types.SecurePasswordKdfAlgoSHA512>`
        secure_random: ``bytes``
        has_recovery (optional): ``bool``
        has_secure_values (optional): ``bool``
        has_password (optional): ``bool``
        current_algo (optional): Either :obj:`PasswordKdfAlgoUnknown <pyrogram.api.types.PasswordKdfAlgoUnknown>` or :obj:`PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow <pyrogram.api.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow>`
        srp_B (optional): ``bytes``
        srp_id (optional): ``int`` ``64-bit``
        hint (optional): ``str``
        email_unconfirmed_pattern (optional): ``str``

    See Also:
        This object can be returned by :obj:`account.GetPassword <pyrogram.api.functions.account.GetPassword>`.
    """

    __slots__ = ["new_algo", "new_secure_algo", "secure_random", "has_recovery", "has_secure_values", "has_password", "current_algo", "srp_B", "srp_id", "hint", "email_unconfirmed_pattern"]

    ID = 0xad2641f8
    QUALNAME = "types.account.Password"

    def __init__(self, *, new_algo, new_secure_algo, secure_random: bytes, has_recovery: bool = None, has_secure_values: bool = None, has_password: bool = None, current_algo=None, srp_B: bytes = None, srp_id: int = None, hint: str = None, email_unconfirmed_pattern: str = None):
        self.has_recovery = has_recovery  # flags.0?true
        self.has_secure_values = has_secure_values  # flags.1?true
        self.has_password = has_password  # flags.2?true
        self.current_algo = current_algo  # flags.2?PasswordKdfAlgo
        self.srp_B = srp_B  # flags.2?bytes
        self.srp_id = srp_id  # flags.2?long
        self.hint = hint  # flags.3?string
        self.email_unconfirmed_pattern = email_unconfirmed_pattern  # flags.4?string
        self.new_algo = new_algo  # PasswordKdfAlgo
        self.new_secure_algo = new_secure_algo  # SecurePasswordKdfAlgo
        self.secure_random = secure_random  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "Password":
        flags = Int.read(b)
        
        has_recovery = True if flags & (1 << 0) else False
        has_secure_values = True if flags & (1 << 1) else False
        has_password = True if flags & (1 << 2) else False
        current_algo = TLObject.read(b) if flags & (1 << 2) else None
        
        srp_B = Bytes.read(b) if flags & (1 << 2) else None
        srp_id = Long.read(b) if flags & (1 << 2) else None
        hint = String.read(b) if flags & (1 << 3) else None
        email_unconfirmed_pattern = String.read(b) if flags & (1 << 4) else None
        new_algo = TLObject.read(b)
        
        new_secure_algo = TLObject.read(b)
        
        secure_random = Bytes.read(b)
        
        return Password(new_algo=new_algo, new_secure_algo=new_secure_algo, secure_random=secure_random, has_recovery=has_recovery, has_secure_values=has_secure_values, has_password=has_password, current_algo=current_algo, srp_B=srp_B, srp_id=srp_id, hint=hint, email_unconfirmed_pattern=email_unconfirmed_pattern)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_recovery is not None else 0
        flags |= (1 << 1) if self.has_secure_values is not None else 0
        flags |= (1 << 2) if self.has_password is not None else 0
        flags |= (1 << 2) if self.current_algo is not None else 0
        flags |= (1 << 2) if self.srp_B is not None else 0
        flags |= (1 << 2) if self.srp_id is not None else 0
        flags |= (1 << 3) if self.hint is not None else 0
        flags |= (1 << 4) if self.email_unconfirmed_pattern is not None else 0
        b.write(Int(flags))
        
        if self.current_algo is not None:
            b.write(self.current_algo.write())
        
        if self.srp_B is not None:
            b.write(Bytes(self.srp_B))
        
        if self.srp_id is not None:
            b.write(Long(self.srp_id))
        
        if self.hint is not None:
            b.write(String(self.hint))
        
        if self.email_unconfirmed_pattern is not None:
            b.write(String(self.email_unconfirmed_pattern))
        
        b.write(self.new_algo.write())
        
        b.write(self.new_secure_algo.write())
        
        b.write(Bytes(self.secure_random))
        
        return b.getvalue()
