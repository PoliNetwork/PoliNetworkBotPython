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


class UrlAuthResultRequest(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x92d33a0e``

    Parameters:
        bot: Either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`
        domain: ``str``
        request_write_access (optional): ``bool``

    See Also:
        This object can be returned by :obj:`messages.RequestUrlAuth <pyrogram.api.functions.messages.RequestUrlAuth>` and :obj:`messages.AcceptUrlAuth <pyrogram.api.functions.messages.AcceptUrlAuth>`.
    """

    __slots__ = ["bot", "domain", "request_write_access"]

    ID = 0x92d33a0e
    QUALNAME = "types.UrlAuthResultRequest"

    def __init__(self, *, bot, domain: str, request_write_access: bool = None):
        self.request_write_access = request_write_access  # flags.0?true
        self.bot = bot  # User
        self.domain = domain  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "UrlAuthResultRequest":
        flags = Int.read(b)
        
        request_write_access = True if flags & (1 << 0) else False
        bot = TLObject.read(b)
        
        domain = String.read(b)
        
        return UrlAuthResultRequest(bot=bot, domain=domain, request_write_access=request_write_access)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.request_write_access is not None else 0
        b.write(Int(flags))
        
        b.write(self.bot.write())
        
        b.write(String(self.domain))
        
        return b.getvalue()
