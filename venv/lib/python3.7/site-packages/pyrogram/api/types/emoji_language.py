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


class EmojiLanguage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xb3fb5361``

    Parameters:
        lang_code: ``str``

    See Also:
        This object can be returned by :obj:`messages.GetEmojiKeywordsLanguages <pyrogram.api.functions.messages.GetEmojiKeywordsLanguages>`.
    """

    __slots__ = ["lang_code"]

    ID = 0xb3fb5361
    QUALNAME = "types.EmojiLanguage"

    def __init__(self, *, lang_code: str):
        self.lang_code = lang_code  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "EmojiLanguage":
        # No flags
        
        lang_code = String.read(b)
        
        return EmojiLanguage(lang_code=lang_code)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        return b.getvalue()
