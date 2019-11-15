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


class ChannelAdminLogEventActionDefaultBannedRights(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x2df5fc0a``

    Parameters:
        prev_banned_rights: :obj:`ChatBannedRights <pyrogram.api.types.ChatBannedRights>`
        new_banned_rights: :obj:`ChatBannedRights <pyrogram.api.types.ChatBannedRights>`
    """

    __slots__ = ["prev_banned_rights", "new_banned_rights"]

    ID = 0x2df5fc0a
    QUALNAME = "types.ChannelAdminLogEventActionDefaultBannedRights"

    def __init__(self, *, prev_banned_rights, new_banned_rights):
        self.prev_banned_rights = prev_banned_rights  # ChatBannedRights
        self.new_banned_rights = new_banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEventActionDefaultBannedRights":
        # No flags
        
        prev_banned_rights = TLObject.read(b)
        
        new_banned_rights = TLObject.read(b)
        
        return ChannelAdminLogEventActionDefaultBannedRights(prev_banned_rights=prev_banned_rights, new_banned_rights=new_banned_rights)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_banned_rights.write())
        
        b.write(self.new_banned_rights.write())
        
        return b.getvalue()
