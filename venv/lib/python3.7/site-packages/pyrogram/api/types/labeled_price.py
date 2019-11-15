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


class LabeledPrice(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xcb296bf8``

    Parameters:
        label: ``str``
        amount: ``int`` ``64-bit``
    """

    __slots__ = ["label", "amount"]

    ID = 0xcb296bf8
    QUALNAME = "types.LabeledPrice"

    def __init__(self, *, label: str, amount: int):
        self.label = label  # string
        self.amount = amount  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "LabeledPrice":
        # No flags
        
        label = String.read(b)
        
        amount = Long.read(b)
        
        return LabeledPrice(label=label, amount=amount)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.label))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
