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


class ChannelDifferenceTooLong(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xa4bcc6fe``

    Parameters:
        dialog: Either :obj:`Dialog <pyrogram.api.types.Dialog>` or :obj:`DialogFolder <pyrogram.api.types.DialogFolder>`
        messages: List of either :obj:`MessageEmpty <pyrogram.api.types.MessageEmpty>`, :obj:`Message <pyrogram.api.types.Message>` or :obj:`MessageService <pyrogram.api.types.MessageService>`
        chats: List of either :obj:`ChatEmpty <pyrogram.api.types.ChatEmpty>`, :obj:`Chat <pyrogram.api.types.Chat>`, :obj:`ChatForbidden <pyrogram.api.types.ChatForbidden>`, :obj:`Channel <pyrogram.api.types.Channel>` or :obj:`ChannelForbidden <pyrogram.api.types.ChannelForbidden>`
        users: List of either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`
        final (optional): ``bool``
        timeout (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by :obj:`updates.GetChannelDifference <pyrogram.api.functions.updates.GetChannelDifference>`.
    """

    __slots__ = ["dialog", "messages", "chats", "users", "final", "timeout"]

    ID = 0xa4bcc6fe
    QUALNAME = "types.updates.ChannelDifferenceTooLong"

    def __init__(self, *, dialog, messages: list, chats: list, users: list, final: bool = None, timeout: int = None):
        self.final = final  # flags.0?true
        self.timeout = timeout  # flags.1?int
        self.dialog = dialog  # Dialog
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelDifferenceTooLong":
        flags = Int.read(b)
        
        final = True if flags & (1 << 0) else False
        timeout = Int.read(b) if flags & (1 << 1) else None
        dialog = TLObject.read(b)
        
        messages = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return ChannelDifferenceTooLong(dialog=dialog, messages=messages, chats=chats, users=users, final=final, timeout=timeout)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.final is not None else 0
        flags |= (1 << 1) if self.timeout is not None else 0
        b.write(Int(flags))
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        b.write(self.dialog.write())
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
