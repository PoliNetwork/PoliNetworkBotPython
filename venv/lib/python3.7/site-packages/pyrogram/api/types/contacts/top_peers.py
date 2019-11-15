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


class TopPeers(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x70b772a8``

    Parameters:
        categories: List of :obj:`TopPeerCategoryPeers <pyrogram.api.types.TopPeerCategoryPeers>`
        chats: List of either :obj:`ChatEmpty <pyrogram.api.types.ChatEmpty>`, :obj:`Chat <pyrogram.api.types.Chat>`, :obj:`ChatForbidden <pyrogram.api.types.ChatForbidden>`, :obj:`Channel <pyrogram.api.types.Channel>` or :obj:`ChannelForbidden <pyrogram.api.types.ChannelForbidden>`
        users: List of either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`

    See Also:
        This object can be returned by :obj:`contacts.GetTopPeers <pyrogram.api.functions.contacts.GetTopPeers>`.
    """

    __slots__ = ["categories", "chats", "users"]

    ID = 0x70b772a8
    QUALNAME = "types.contacts.TopPeers"

    def __init__(self, *, categories: list, chats: list, users: list):
        self.categories = categories  # Vector<TopPeerCategoryPeers>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args) -> "TopPeers":
        # No flags
        
        categories = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return TopPeers(categories=categories, chats=chats, users=users)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.categories))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
