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


class UpdatePhoneCall(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xab0f6b1e``

    Parameters:
        phone_call: Either :obj:`PhoneCallEmpty <pyrogram.api.types.PhoneCallEmpty>`, :obj:`PhoneCallWaiting <pyrogram.api.types.PhoneCallWaiting>`, :obj:`PhoneCallRequested <pyrogram.api.types.PhoneCallRequested>`, :obj:`PhoneCallAccepted <pyrogram.api.types.PhoneCallAccepted>`, :obj:`PhoneCall <pyrogram.api.types.PhoneCall>` or :obj:`PhoneCallDiscarded <pyrogram.api.types.PhoneCallDiscarded>`
    """

    __slots__ = ["phone_call"]

    ID = 0xab0f6b1e
    QUALNAME = "types.UpdatePhoneCall"

    def __init__(self, *, phone_call):
        self.phone_call = phone_call  # PhoneCall

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdatePhoneCall":
        # No flags
        
        phone_call = TLObject.read(b)
        
        return UpdatePhoneCall(phone_call=phone_call)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.phone_call.write())
        
        return b.getvalue()
