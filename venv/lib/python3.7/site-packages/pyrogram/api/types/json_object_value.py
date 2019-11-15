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


class JsonObjectValue(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xc0de1bd9``

    Parameters:
        key: ``str``
        value: Either :obj:`JsonNull <pyrogram.api.types.JsonNull>`, :obj:`JsonBool <pyrogram.api.types.JsonBool>`, :obj:`JsonNumber <pyrogram.api.types.JsonNumber>`, :obj:`JsonString <pyrogram.api.types.JsonString>`, :obj:`JsonArray <pyrogram.api.types.JsonArray>` or :obj:`JsonObject <pyrogram.api.types.JsonObject>`
    """

    __slots__ = ["key", "value"]

    ID = 0xc0de1bd9
    QUALNAME = "types.JsonObjectValue"

    def __init__(self, *, key: str, value):
        self.key = key  # string
        self.value = value  # JSONValue

    @staticmethod
    def read(b: BytesIO, *args) -> "JsonObjectValue":
        # No flags
        
        key = String.read(b)
        
        value = TLObject.read(b)
        
        return JsonObjectValue(key=key, value=value)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.key))
        
        b.write(self.value.write())
        
        return b.getvalue()
