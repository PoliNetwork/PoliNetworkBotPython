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


class AuthorizationForm(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xad2e1cd8``

    Parameters:
        required_types: List of either :obj:`SecureRequiredType <pyrogram.api.types.SecureRequiredType>` or :obj:`SecureRequiredTypeOneOf <pyrogram.api.types.SecureRequiredTypeOneOf>`
        values: List of :obj:`SecureValue <pyrogram.api.types.SecureValue>`
        errors: List of either :obj:`SecureValueErrorData <pyrogram.api.types.SecureValueErrorData>`, :obj:`SecureValueErrorFrontSide <pyrogram.api.types.SecureValueErrorFrontSide>`, :obj:`SecureValueErrorReverseSide <pyrogram.api.types.SecureValueErrorReverseSide>`, :obj:`SecureValueErrorSelfie <pyrogram.api.types.SecureValueErrorSelfie>`, :obj:`SecureValueErrorFile <pyrogram.api.types.SecureValueErrorFile>`, :obj:`SecureValueErrorFiles <pyrogram.api.types.SecureValueErrorFiles>`, :obj:`SecureValueError <pyrogram.api.types.SecureValueError>`, :obj:`SecureValueErrorTranslationFile <pyrogram.api.types.SecureValueErrorTranslationFile>` or :obj:`SecureValueErrorTranslationFiles <pyrogram.api.types.SecureValueErrorTranslationFiles>`
        users: List of either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`
        privacy_policy_url (optional): ``str``

    See Also:
        This object can be returned by :obj:`account.GetAuthorizationForm <pyrogram.api.functions.account.GetAuthorizationForm>`.
    """

    __slots__ = ["required_types", "values", "errors", "users", "privacy_policy_url"]

    ID = 0xad2e1cd8
    QUALNAME = "types.account.AuthorizationForm"

    def __init__(self, *, required_types: list, values: list, errors: list, users: list, privacy_policy_url: str = None):
        self.required_types = required_types  # Vector<SecureRequiredType>
        self.values = values  # Vector<SecureValue>
        self.errors = errors  # Vector<SecureValueError>
        self.users = users  # Vector<User>
        self.privacy_policy_url = privacy_policy_url  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args) -> "AuthorizationForm":
        flags = Int.read(b)
        
        required_types = TLObject.read(b)
        
        values = TLObject.read(b)
        
        errors = TLObject.read(b)
        
        users = TLObject.read(b)
        
        privacy_policy_url = String.read(b) if flags & (1 << 0) else None
        return AuthorizationForm(required_types=required_types, values=values, errors=errors, users=users, privacy_policy_url=privacy_policy_url)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.privacy_policy_url is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.required_types))
        
        b.write(Vector(self.values))
        
        b.write(Vector(self.errors))
        
        b.write(Vector(self.users))
        
        if self.privacy_policy_url is not None:
            b.write(String(self.privacy_policy_url))
        
        return b.getvalue()
