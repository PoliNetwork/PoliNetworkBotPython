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


class GetTopPeers(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd4982db5``

    Parameters:
        offset: ``int`` ``32-bit``
        limit: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``
        correspondents (optional): ``bool``
        bots_pm (optional): ``bool``
        bots_inline (optional): ``bool``
        phone_calls (optional): ``bool``
        forward_users (optional): ``bool``
        forward_chats (optional): ``bool``
        groups (optional): ``bool``
        channels (optional): ``bool``

    Returns:
        Either :obj:`contacts.TopPeersNotModified <pyrogram.api.types.contacts.TopPeersNotModified>`, :obj:`contacts.TopPeers <pyrogram.api.types.contacts.TopPeers>` or :obj:`contacts.TopPeersDisabled <pyrogram.api.types.contacts.TopPeersDisabled>`
    """

    __slots__ = ["offset", "limit", "hash", "correspondents", "bots_pm", "bots_inline", "phone_calls", "forward_users", "forward_chats", "groups", "channels"]

    ID = 0xd4982db5
    QUALNAME = "functions.contacts.GetTopPeers"

    def __init__(self, *, offset: int, limit: int, hash: int, correspondents: bool = None, bots_pm: bool = None, bots_inline: bool = None, phone_calls: bool = None, forward_users: bool = None, forward_chats: bool = None, groups: bool = None, channels: bool = None):
        self.correspondents = correspondents  # flags.0?true
        self.bots_pm = bots_pm  # flags.1?true
        self.bots_inline = bots_inline  # flags.2?true
        self.phone_calls = phone_calls  # flags.3?true
        self.forward_users = forward_users  # flags.4?true
        self.forward_chats = forward_chats  # flags.5?true
        self.groups = groups  # flags.10?true
        self.channels = channels  # flags.15?true
        self.offset = offset  # int
        self.limit = limit  # int
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetTopPeers":
        flags = Int.read(b)
        
        correspondents = True if flags & (1 << 0) else False
        bots_pm = True if flags & (1 << 1) else False
        bots_inline = True if flags & (1 << 2) else False
        phone_calls = True if flags & (1 << 3) else False
        forward_users = True if flags & (1 << 4) else False
        forward_chats = True if flags & (1 << 5) else False
        groups = True if flags & (1 << 10) else False
        channels = True if flags & (1 << 15) else False
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        hash = Int.read(b)
        
        return GetTopPeers(offset=offset, limit=limit, hash=hash, correspondents=correspondents, bots_pm=bots_pm, bots_inline=bots_inline, phone_calls=phone_calls, forward_users=forward_users, forward_chats=forward_chats, groups=groups, channels=channels)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.correspondents is not None else 0
        flags |= (1 << 1) if self.bots_pm is not None else 0
        flags |= (1 << 2) if self.bots_inline is not None else 0
        flags |= (1 << 3) if self.phone_calls is not None else 0
        flags |= (1 << 4) if self.forward_users is not None else 0
        flags |= (1 << 5) if self.forward_chats is not None else 0
        flags |= (1 << 10) if self.groups is not None else 0
        flags |= (1 << 15) if self.channels is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
