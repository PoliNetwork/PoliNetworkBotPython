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


class CodeSettings(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xdebebe83``

    Parameters:
        allow_flashcall (optional): ``bool``
        current_number (optional): ``bool``
        allow_app_hash (optional): ``bool``
    """

    __slots__ = ["allow_flashcall", "current_number", "allow_app_hash"]

    ID = 0xdebebe83
    QUALNAME = "types.CodeSettings"

    def __init__(self, *, allow_flashcall: bool = None, current_number: bool = None, allow_app_hash: bool = None):
        self.allow_flashcall = allow_flashcall  # flags.0?true
        self.current_number = current_number  # flags.1?true
        self.allow_app_hash = allow_app_hash  # flags.4?true

    @staticmethod
    def read(b: BytesIO, *args) -> "CodeSettings":
        flags = Int.read(b)
        
        allow_flashcall = True if flags & (1 << 0) else False
        current_number = True if flags & (1 << 1) else False
        allow_app_hash = True if flags & (1 << 4) else False
        return CodeSettings(allow_flashcall=allow_flashcall, current_number=current_number, allow_app_hash=allow_app_hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_flashcall is not None else 0
        flags |= (1 << 1) if self.current_number is not None else 0
        flags |= (1 << 4) if self.allow_app_hash is not None else 0
        b.write(Int(flags))
        
        return b.getvalue()
