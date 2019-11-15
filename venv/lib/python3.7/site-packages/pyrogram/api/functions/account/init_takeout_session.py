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


class InitTakeoutSession(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf05b4804``

    Parameters:
        contacts (optional): ``bool``
        message_users (optional): ``bool``
        message_chats (optional): ``bool``
        message_megagroups (optional): ``bool``
        message_channels (optional): ``bool``
        files (optional): ``bool``
        file_max_size (optional): ``int`` ``32-bit``

    Returns:
        :obj:`account.Takeout <pyrogram.api.types.account.Takeout>`
    """

    __slots__ = ["contacts", "message_users", "message_chats", "message_megagroups", "message_channels", "files", "file_max_size"]

    ID = 0xf05b4804
    QUALNAME = "functions.account.InitTakeoutSession"

    def __init__(self, *, contacts: bool = None, message_users: bool = None, message_chats: bool = None, message_megagroups: bool = None, message_channels: bool = None, files: bool = None, file_max_size: int = None):
        self.contacts = contacts  # flags.0?true
        self.message_users = message_users  # flags.1?true
        self.message_chats = message_chats  # flags.2?true
        self.message_megagroups = message_megagroups  # flags.3?true
        self.message_channels = message_channels  # flags.4?true
        self.files = files  # flags.5?true
        self.file_max_size = file_max_size  # flags.5?int

    @staticmethod
    def read(b: BytesIO, *args) -> "InitTakeoutSession":
        flags = Int.read(b)
        
        contacts = True if flags & (1 << 0) else False
        message_users = True if flags & (1 << 1) else False
        message_chats = True if flags & (1 << 2) else False
        message_megagroups = True if flags & (1 << 3) else False
        message_channels = True if flags & (1 << 4) else False
        files = True if flags & (1 << 5) else False
        file_max_size = Int.read(b) if flags & (1 << 5) else None
        return InitTakeoutSession(contacts=contacts, message_users=message_users, message_chats=message_chats, message_megagroups=message_megagroups, message_channels=message_channels, files=files, file_max_size=file_max_size)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.contacts is not None else 0
        flags |= (1 << 1) if self.message_users is not None else 0
        flags |= (1 << 2) if self.message_chats is not None else 0
        flags |= (1 << 3) if self.message_megagroups is not None else 0
        flags |= (1 << 4) if self.message_channels is not None else 0
        flags |= (1 << 5) if self.files is not None else 0
        flags |= (1 << 5) if self.file_max_size is not None else 0
        b.write(Int(flags))
        
        if self.file_max_size is not None:
            b.write(Int(self.file_max_size))
        
        return b.getvalue()
