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


class GetEmojiKeywordsLanguages(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x4e9963b2``

    Parameters:
        lang_codes: List of ``str``

    Returns:
        List of :obj:`EmojiLanguage <pyrogram.api.types.EmojiLanguage>`
    """

    __slots__ = ["lang_codes"]

    ID = 0x4e9963b2
    QUALNAME = "functions.messages.GetEmojiKeywordsLanguages"

    def __init__(self, *, lang_codes: list):
        self.lang_codes = lang_codes  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args) -> "GetEmojiKeywordsLanguages":
        # No flags
        
        lang_codes = TLObject.read(b, String)
        
        return GetEmojiKeywordsLanguages(lang_codes=lang_codes)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.lang_codes, String))
        
        return b.getvalue()
