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


class UpdateDcOptions(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x8e5e9873``

    Parameters:
        dc_options: List of :obj:`DcOption <pyrogram.api.types.DcOption>`
    """

    __slots__ = ["dc_options"]

    ID = 0x8e5e9873
    QUALNAME = "types.UpdateDcOptions"

    def __init__(self, *, dc_options: list):
        self.dc_options = dc_options  # Vector<DcOption>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateDcOptions":
        # No flags
        
        dc_options = TLObject.read(b)
        
        return UpdateDcOptions(dc_options=dc_options)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.dc_options))
        
        return b.getvalue()
