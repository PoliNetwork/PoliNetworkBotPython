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


class AuthorizationSignUpRequired(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x44747e9a``

    Parameters:
        terms_of_service (optional): :obj:`help.TermsOfService <pyrogram.api.types.help.TermsOfService>`

    See Also:
        This object can be returned by :obj:`auth.SignUp <pyrogram.api.functions.auth.SignUp>`, :obj:`auth.SignIn <pyrogram.api.functions.auth.SignIn>`, :obj:`auth.ImportAuthorization <pyrogram.api.functions.auth.ImportAuthorization>`, :obj:`auth.ImportBotAuthorization <pyrogram.api.functions.auth.ImportBotAuthorization>`, :obj:`auth.CheckPassword <pyrogram.api.functions.auth.CheckPassword>` and :obj:`auth.RecoverPassword <pyrogram.api.functions.auth.RecoverPassword>`.
    """

    __slots__ = ["terms_of_service"]

    ID = 0x44747e9a
    QUALNAME = "types.auth.AuthorizationSignUpRequired"

    def __init__(self, *, terms_of_service=None):
        self.terms_of_service = terms_of_service  # flags.0?help.TermsOfService

    @staticmethod
    def read(b: BytesIO, *args) -> "AuthorizationSignUpRequired":
        flags = Int.read(b)
        
        terms_of_service = TLObject.read(b) if flags & (1 << 0) else None
        
        return AuthorizationSignUpRequired(terms_of_service=terms_of_service)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.terms_of_service is not None else 0
        b.write(Int(flags))
        
        if self.terms_of_service is not None:
            b.write(self.terms_of_service.write())
        
        return b.getvalue()
