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


class InputKeyboardButtonUrlAuth(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd02e7fd4``

    Parameters:
        text: ``str``
        url: ``str``
        bot: Either :obj:`InputUserEmpty <pyrogram.api.types.InputUserEmpty>`, :obj:`InputUserSelf <pyrogram.api.types.InputUserSelf>`, :obj:`InputUser <pyrogram.api.types.InputUser>` or :obj:`InputUserFromMessage <pyrogram.api.types.InputUserFromMessage>`
        request_write_access (optional): ``bool``
        fwd_text (optional): ``str``
    """

    __slots__ = ["text", "url", "bot", "request_write_access", "fwd_text"]

    ID = 0xd02e7fd4
    QUALNAME = "types.InputKeyboardButtonUrlAuth"

    def __init__(self, *, text: str, url: str, bot, request_write_access: bool = None, fwd_text: str = None):
        self.request_write_access = request_write_access  # flags.0?true
        self.text = text  # string
        self.fwd_text = fwd_text  # flags.1?string
        self.url = url  # string
        self.bot = bot  # InputUser

    @staticmethod
    def read(b: BytesIO, *args) -> "InputKeyboardButtonUrlAuth":
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        text = String.read(b)
        
        fwd_text = String.read(b) if flags & (1 << 1) else None
        url = String.read(b)
        
        bot = TLObject.read(b)
        
        return InputKeyboardButtonUrlAuth(text=text, url=url, bot=bot, request_write_access=request_write_access, fwd_text=fwd_text)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access is not None else 0
        flags |= (1 << 1) if self.fwd_text is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.text))
        
        if self.fwd_text is not None:
            b.write(String(self.fwd_text))
        
        b.write(String(self.url))
        
        b.write(self.bot.write())
        
        return b.getvalue()
