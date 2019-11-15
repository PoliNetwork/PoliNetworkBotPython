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


class PasswordSettings(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x9a5c33e5``

    Parameters:
        email (optional): ``str``
        secure_settings (optional): :obj:`SecureSecretSettings <pyrogram.api.types.SecureSecretSettings>`

    See Also:
        This object can be returned by :obj:`account.GetPasswordSettings <pyrogram.api.functions.account.GetPasswordSettings>`.
    """

    __slots__ = ["email", "secure_settings"]

    ID = 0x9a5c33e5
    QUALNAME = "types.account.PasswordSettings"

    def __init__(self, *, email: str = None, secure_settings=None):
        self.email = email  # flags.0?string
        self.secure_settings = secure_settings  # flags.1?SecureSecretSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "PasswordSettings":
        flags = Int.read(b)
        
        email = String.read(b) if flags & (1 << 0) else None
        secure_settings = TLObject.read(b) if flags & (1 << 1) else None
        
        return PasswordSettings(email=email, secure_settings=secure_settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.email is not None else 0
        flags |= (1 << 1) if self.secure_settings is not None else 0
        b.write(Int(flags))
        
        if self.email is not None:
            b.write(String(self.email))
        
        if self.secure_settings is not None:
            b.write(self.secure_settings.write())
        
        return b.getvalue()
