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


class Messages(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x8c718e87``

    Parameters:
        messages: List of either :obj:`MessageEmpty <pyrogram.api.types.MessageEmpty>`, :obj:`Message <pyrogram.api.types.Message>` or :obj:`MessageService <pyrogram.api.types.MessageService>`
        chats: List of either :obj:`ChatEmpty <pyrogram.api.types.ChatEmpty>`, :obj:`Chat <pyrogram.api.types.Chat>`, :obj:`ChatForbidden <pyrogram.api.types.ChatForbidden>`, :obj:`Channel <pyrogram.api.types.Channel>` or :obj:`ChannelForbidden <pyrogram.api.types.ChannelForbidden>`
        users: List of either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`

    See Also:
        This object can be returned by :obj:`messages.GetMessages <pyrogram.api.functions.messages.GetMessages>`, :obj:`messages.GetHistory <pyrogram.api.functions.messages.GetHistory>`, :obj:`messages.Search <pyrogram.api.functions.messages.Search>`, :obj:`messages.SearchGlobal <pyrogram.api.functions.messages.SearchGlobal>`, :obj:`messages.GetUnreadMentions <pyrogram.api.functions.messages.GetUnreadMentions>`, :obj:`messages.GetRecentLocations <pyrogram.api.functions.messages.GetRecentLocations>`, :obj:`messages.GetScheduledHistory <pyrogram.api.functions.messages.GetScheduledHistory>`, :obj:`messages.GetScheduledMessages <pyrogram.api.functions.messages.GetScheduledMessages>` and :obj:`channels.GetMessages <pyrogram.api.functions.channels.GetMessages>`.
    """

    __slots__ = ["messages", "chats", "users"]

    ID = 0x8c718e87
    QUALNAME = "types.messages.Messages"

    def __init__(self, *, messages: list, chats: list, users: list):
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args) -> "Messages":
        # No flags
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return Messages(messages=messages, chats=chats, users=users)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
