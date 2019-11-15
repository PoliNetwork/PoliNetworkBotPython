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


class KeyboardButtonUrlAuth(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x10b78d29``

    Parameters:
        text: ``str``
        url: ``str``
        button_id: ``int`` ``32-bit``
        fwd_text (optional): ``str``
    """

    __slots__ = ["text", "url", "button_id", "fwd_text"]

    ID = 0x10b78d29
    QUALNAME = "types.KeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, button_id: int, fwd_text: str = None):
        self.text = text  # string
        self.fwd_text = fwd_text  # flags.0?string
        self.url = url  # string
        self.button_id = button_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "KeyboardButtonUrlAuth":
        flags = Int.read(b)
        
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 0) else None
        url = String.read(b)
        
        button_id = Int.read(b)
        
        return KeyboardButtonUrlAuth(text=text, url=url, button_id=button_id, fwd_text=fwd_text)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(Int(self.button_id))
        
        return b.getvalue()
