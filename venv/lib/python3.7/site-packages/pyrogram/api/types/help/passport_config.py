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


class PassportConfig(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xa098d6af``

    Parameters:
        hash: ``int`` ``32-bit``
        countries_langs: :obj:`DataJSON <pyrogram.api.types.DataJSON>`

    See Also:
        This object can be returned by :obj:`help.GetPassportConfig <pyrogram.api.functions.help.GetPassportConfig>`.
    """

    __slots__ = ["hash", "countries_langs"]

    ID = 0xa098d6af
    QUALNAME = "types.help.PassportConfig"

    def __init__(self, *, hash: int, countries_langs):
        self.hash = hash  # int
        self.countries_langs = countries_langs  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args) -> "PassportConfig":
        # No flags
        
        hash = Int.read(b)
        
        countries_langs = TLObject.read(b)
        
        return PassportConfig(hash=hash, countries_langs=countries_langs)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.hash))
        
        b.write(self.countries_langs.write())
        
        return b.getvalue()
