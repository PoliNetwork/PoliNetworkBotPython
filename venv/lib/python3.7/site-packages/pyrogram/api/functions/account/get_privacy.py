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


class GetPrivacy(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xdadbc950``

    Parameters:
        key: Either :obj:`InputPrivacyKeyStatusTimestamp <pyrogram.api.types.InputPrivacyKeyStatusTimestamp>`, :obj:`InputPrivacyKeyChatInvite <pyrogram.api.types.InputPrivacyKeyChatInvite>`, :obj:`InputPrivacyKeyPhoneCall <pyrogram.api.types.InputPrivacyKeyPhoneCall>`, :obj:`InputPrivacyKeyPhoneP2P <pyrogram.api.types.InputPrivacyKeyPhoneP2P>`, :obj:`InputPrivacyKeyForwards <pyrogram.api.types.InputPrivacyKeyForwards>`, :obj:`InputPrivacyKeyProfilePhoto <pyrogram.api.types.InputPrivacyKeyProfilePhoto>`, :obj:`InputPrivacyKeyPhoneNumber <pyrogram.api.types.InputPrivacyKeyPhoneNumber>` or :obj:`InputPrivacyKeyAddedByPhone <pyrogram.api.types.InputPrivacyKeyAddedByPhone>`

    Returns:
        :obj:`account.PrivacyRules <pyrogram.api.types.account.PrivacyRules>`
    """

    __slots__ = ["key"]

    ID = 0xdadbc950
    QUALNAME = "functions.account.GetPrivacy"

    def __init__(self, *, key):
        self.key = key  # InputPrivacyKey

    @staticmethod
    def read(b: BytesIO, *args) -> "GetPrivacy":
        # No flags
        
        key = TLObject.read(b)
        
        return GetPrivacy(key=key)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        return b.getvalue()
