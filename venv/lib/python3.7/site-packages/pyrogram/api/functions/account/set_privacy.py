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


class SetPrivacy(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xc9f81ce8``

    Parameters:
        key: Either :obj:`InputPrivacyKeyStatusTimestamp <pyrogram.api.types.InputPrivacyKeyStatusTimestamp>`, :obj:`InputPrivacyKeyChatInvite <pyrogram.api.types.InputPrivacyKeyChatInvite>`, :obj:`InputPrivacyKeyPhoneCall <pyrogram.api.types.InputPrivacyKeyPhoneCall>`, :obj:`InputPrivacyKeyPhoneP2P <pyrogram.api.types.InputPrivacyKeyPhoneP2P>`, :obj:`InputPrivacyKeyForwards <pyrogram.api.types.InputPrivacyKeyForwards>`, :obj:`InputPrivacyKeyProfilePhoto <pyrogram.api.types.InputPrivacyKeyProfilePhoto>`, :obj:`InputPrivacyKeyPhoneNumber <pyrogram.api.types.InputPrivacyKeyPhoneNumber>` or :obj:`InputPrivacyKeyAddedByPhone <pyrogram.api.types.InputPrivacyKeyAddedByPhone>`
        rules: List of either :obj:`InputPrivacyValueAllowContacts <pyrogram.api.types.InputPrivacyValueAllowContacts>`, :obj:`InputPrivacyValueAllowAll <pyrogram.api.types.InputPrivacyValueAllowAll>`, :obj:`InputPrivacyValueAllowUsers <pyrogram.api.types.InputPrivacyValueAllowUsers>`, :obj:`InputPrivacyValueDisallowContacts <pyrogram.api.types.InputPrivacyValueDisallowContacts>`, :obj:`InputPrivacyValueDisallowAll <pyrogram.api.types.InputPrivacyValueDisallowAll>`, :obj:`InputPrivacyValueDisallowUsers <pyrogram.api.types.InputPrivacyValueDisallowUsers>`, :obj:`InputPrivacyValueAllowChatParticipants <pyrogram.api.types.InputPrivacyValueAllowChatParticipants>` or :obj:`InputPrivacyValueDisallowChatParticipants <pyrogram.api.types.InputPrivacyValueDisallowChatParticipants>`

    Returns:
        :obj:`account.PrivacyRules <pyrogram.api.types.account.PrivacyRules>`
    """

    __slots__ = ["key", "rules"]

    ID = 0xc9f81ce8
    QUALNAME = "functions.account.SetPrivacy"

    def __init__(self, *, key, rules: list):
        self.key = key  # InputPrivacyKey
        self.rules = rules  # Vector<InputPrivacyRule>

    @staticmethod
    def read(b: BytesIO, *args) -> "SetPrivacy":
        # No flags
        
        key = TLObject.read(b)
        
        rules = TLObject.read(b)
        
        return SetPrivacy(key=key, rules=rules)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        b.write(Vector(self.rules))
        
        return b.getvalue()
