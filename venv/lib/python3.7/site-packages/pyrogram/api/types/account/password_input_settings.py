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


class PasswordInputSettings(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xc23727c9``

    Parameters:
        new_algo (optional): Either :obj:`PasswordKdfAlgoUnknown <pyrogram.api.types.PasswordKdfAlgoUnknown>` or :obj:`PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow <pyrogram.api.types.PasswordKdfAlgoSHA256SHA256PBKDF2HMACSHA512iter100000SHA256ModPow>`
        new_password_hash (optional): ``bytes``
        hint (optional): ``str``
        email (optional): ``str``
        new_secure_settings (optional): :obj:`SecureSecretSettings <pyrogram.api.types.SecureSecretSettings>`
    """

    __slots__ = ["new_algo", "new_password_hash", "hint", "email", "new_secure_settings"]

    ID = 0xc23727c9
    QUALNAME = "types.account.PasswordInputSettings"

    def __init__(self, *, new_algo=None, new_password_hash: bytes = None, hint: str = None, email: str = None, new_secure_settings=None):
        self.new_algo = new_algo  # flags.0?PasswordKdfAlgo
        self.new_password_hash = new_password_hash  # flags.0?bytes
        self.hint = hint  # flags.0?string
        self.email = email  # flags.1?string
        self.new_secure_settings = new_secure_settings  # flags.2?SecureSecretSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "PasswordInputSettings":
        flags = Int.read(b)
        
        new_algo = TLObject.read(b) if flags & (1 << 0) else None
        
        new_password_hash = Bytes.read(b) if flags & (1 << 0) else None
        hint = String.read(b) if flags & (1 << 0) else None
        email = String.read(b) if flags & (1 << 1) else None
        new_secure_settings = TLObject.read(b) if flags & (1 << 2) else None
        
        return PasswordInputSettings(new_algo=new_algo, new_password_hash=new_password_hash, hint=hint, email=email, new_secure_settings=new_secure_settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.new_algo is not None else 0
        flags |= (1 << 0) if self.new_password_hash is not None else 0
        flags |= (1 << 0) if self.hint is not None else 0
        flags |= (1 << 1) if self.email is not None else 0
        flags |= (1 << 2) if self.new_secure_settings is not None else 0
        b.write(Int(flags))
        
        if self.new_algo is not None:
            b.write(self.new_algo.write())
        
        if self.new_password_hash is not None:
            b.write(Bytes(self.new_password_hash))
        
        if self.hint is not None:
            b.write(String(self.hint))
        
        if self.email is not None:
            b.write(String(self.email))
        
        if self.new_secure_settings is not None:
            b.write(self.new_secure_settings.write())
        
        return b.getvalue()
