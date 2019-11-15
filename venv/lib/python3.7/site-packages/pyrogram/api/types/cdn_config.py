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


class CdnConfig(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x5725e40a``

    Parameters:
        public_keys: List of :obj:`CdnPublicKey <pyrogram.api.types.CdnPublicKey>`

    See Also:
        This object can be returned by :obj:`help.GetCdnConfig <pyrogram.api.functions.help.GetCdnConfig>`.
    """

    __slots__ = ["public_keys"]

    ID = 0x5725e40a
    QUALNAME = "types.CdnConfig"

    def __init__(self, *, public_keys: list):
        self.public_keys = public_keys  # Vector<CdnPublicKey>

    @staticmethod
    def read(b: BytesIO, *args) -> "CdnConfig":
        # No flags
        
        public_keys = TLObject.read(b)
        
        return CdnConfig(public_keys=public_keys)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.public_keys))
        
        return b.getvalue()
