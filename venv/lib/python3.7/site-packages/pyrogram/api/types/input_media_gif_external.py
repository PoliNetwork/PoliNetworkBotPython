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


class InputMediaGifExternal(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x4843b0fd``

    Parameters:
        url: ``str``
        q: ``str``
    """

    __slots__ = ["url", "q"]

    ID = 0x4843b0fd
    QUALNAME = "types.InputMediaGifExternal"

    def __init__(self, *, url: str, q: str):
        self.url = url  # string
        self.q = q  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "InputMediaGifExternal":
        # No flags
        
        url = String.read(b)
        
        q = String.read(b)
        
        return InputMediaGifExternal(url=url, q=q)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(String(self.q))
        
        return b.getvalue()
