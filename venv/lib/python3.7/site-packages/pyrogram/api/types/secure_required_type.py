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


class SecureRequiredType(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x829d99da``

    Parameters:
        type: Either :obj:`SecureValueTypePersonalDetails <pyrogram.api.types.SecureValueTypePersonalDetails>`, :obj:`SecureValueTypePassport <pyrogram.api.types.SecureValueTypePassport>`, :obj:`SecureValueTypeDriverLicense <pyrogram.api.types.SecureValueTypeDriverLicense>`, :obj:`SecureValueTypeIdentityCard <pyrogram.api.types.SecureValueTypeIdentityCard>`, :obj:`SecureValueTypeInternalPassport <pyrogram.api.types.SecureValueTypeInternalPassport>`, :obj:`SecureValueTypeAddress <pyrogram.api.types.SecureValueTypeAddress>`, :obj:`SecureValueTypeUtilityBill <pyrogram.api.types.SecureValueTypeUtilityBill>`, :obj:`SecureValueTypeBankStatement <pyrogram.api.types.SecureValueTypeBankStatement>`, :obj:`SecureValueTypeRentalAgreement <pyrogram.api.types.SecureValueTypeRentalAgreement>`, :obj:`SecureValueTypePassportRegistration <pyrogram.api.types.SecureValueTypePassportRegistration>`, :obj:`SecureValueTypeTemporaryRegistration <pyrogram.api.types.SecureValueTypeTemporaryRegistration>`, :obj:`SecureValueTypePhone <pyrogram.api.types.SecureValueTypePhone>` or :obj:`SecureValueTypeEmail <pyrogram.api.types.SecureValueTypeEmail>`
        native_names (optional): ``bool``
        selfie_required (optional): ``bool``
        translation_required (optional): ``bool``
    """

    __slots__ = ["type", "native_names", "selfie_required", "translation_required"]

    ID = 0x829d99da
    QUALNAME = "types.SecureRequiredType"

    def __init__(self, *, type, native_names: bool = None, selfie_required: bool = None, translation_required: bool = None):
        self.native_names = native_names  # flags.0?true
        self.selfie_required = selfie_required  # flags.1?true
        self.translation_required = translation_required  # flags.2?true
        self.type = type  # SecureValueType

    @staticmethod
    def read(b: BytesIO, *args) -> "SecureRequiredType":
        flags = Int.read(b)
        
        native_names = True if flags & (1 << 0) else False
        selfie_required = True if flags & (1 << 1) else False
        translation_required = True if flags & (1 << 2) else False
        type = TLObject.read(b)
        
        return SecureRequiredType(type=type, native_names=native_names, selfie_required=selfie_required, translation_required=translation_required)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.native_names is not None else 0
        flags |= (1 << 1) if self.selfie_required is not None else 0
        flags |= (1 << 2) if self.translation_required is not None else 0
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        return b.getvalue()
