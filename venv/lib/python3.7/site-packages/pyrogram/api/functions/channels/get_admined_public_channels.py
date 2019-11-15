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


class GetAdminedPublicChannels(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf8b036af``

    Parameters:
        by_location (optional): ``bool``
        check_limit (optional): ``bool``

    Returns:
        Either :obj:`messages.Chats <pyrogram.api.types.messages.Chats>` or :obj:`messages.ChatsSlice <pyrogram.api.types.messages.ChatsSlice>`
    """

    __slots__ = ["by_location", "check_limit"]

    ID = 0xf8b036af
    QUALNAME = "functions.channels.GetAdminedPublicChannels"

    def __init__(self, *, by_location: bool = None, check_limit: bool = None):
        self.by_location = by_location  # flags.0?true
        self.check_limit = check_limit  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args) -> "GetAdminedPublicChannels":
        flags = Int.read(b)
        
        by_location = True if flags & (1 << 0) else False
        check_limit = True if flags & (1 << 1) else False
        return GetAdminedPublicChannels(by_location=by_location, check_limit=check_limit)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.by_location is not None else 0
        flags |= (1 << 1) if self.check_limit is not None else 0
        b.write(Int(flags))
        
        return b.getvalue()
