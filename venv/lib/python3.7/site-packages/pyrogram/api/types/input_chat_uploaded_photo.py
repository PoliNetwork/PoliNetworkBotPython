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


class InputChatUploadedPhoto(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x927c55b4``

    Parameters:
        file: Either :obj:`InputFile <pyrogram.api.types.InputFile>` or :obj:`InputFileBig <pyrogram.api.types.InputFileBig>`
    """

    __slots__ = ["file"]

    ID = 0x927c55b4
    QUALNAME = "types.InputChatUploadedPhoto"

    def __init__(self, *, file):
        self.file = file  # InputFile

    @staticmethod
    def read(b: BytesIO, *args) -> "InputChatUploadedPhoto":
        # No flags
        
        file = TLObject.read(b)
        
        return InputChatUploadedPhoto(file=file)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.file.write())
        
        return b.getvalue()
