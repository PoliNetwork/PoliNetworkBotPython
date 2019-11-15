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


class Chat(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x3bda1bde``

    Parameters:
        id: ``int`` ``32-bit``
        title: ``str``
        photo: Either :obj:`ChatPhotoEmpty <pyrogram.api.types.ChatPhotoEmpty>` or :obj:`ChatPhoto <pyrogram.api.types.ChatPhoto>`
        participants_count: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
        creator (optional): ``bool``
        kicked (optional): ``bool``
        left (optional): ``bool``
        deactivated (optional): ``bool``
        migrated_to (optional): Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`
        admin_rights (optional): :obj:`ChatAdminRights <pyrogram.api.types.ChatAdminRights>`
        default_banned_rights (optional): :obj:`ChatBannedRights <pyrogram.api.types.ChatBannedRights>`
    """

    __slots__ = ["id", "title", "photo", "participants_count", "date", "version", "creator", "kicked", "left", "deactivated", "migrated_to", "admin_rights", "default_banned_rights"]

    ID = 0x3bda1bde
    QUALNAME = "types.Chat"

    def __init__(self, *, id: int, title: str, photo, participants_count: int, date: int, version: int, creator: bool = None, kicked: bool = None, left: bool = None, deactivated: bool = None, migrated_to=None, admin_rights=None, default_banned_rights=None):
        self.creator = creator  # flags.0?true
        self.kicked = kicked  # flags.1?true
        self.left = left  # flags.2?true
        self.deactivated = deactivated  # flags.5?true
        self.id = id  # int
        self.title = title  # string
        self.photo = photo  # ChatPhoto
        self.participants_count = participants_count  # int
        self.date = date  # int
        self.version = version  # int
        self.migrated_to = migrated_to  # flags.6?InputChannel
        self.admin_rights = admin_rights  # flags.14?ChatAdminRights
        self.default_banned_rights = default_banned_rights  # flags.18?ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args) -> "Chat":
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        kicked = True if flags & (1 << 1) else False
        left = True if flags & (1 << 2) else False
        deactivated = True if flags & (1 << 5) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        photo = TLObject.read(b)
        
        participants_count = Int.read(b)
        
        date = Int.read(b)
        
        version = Int.read(b)
        
        migrated_to = TLObject.read(b) if flags & (1 << 6) else None
        
        admin_rights = TLObject.read(b) if flags & (1 << 14) else None
        
        default_banned_rights = TLObject.read(b) if flags & (1 << 18) else None
        
        return Chat(id=id, title=title, photo=photo, participants_count=participants_count, date=date, version=version, creator=creator, kicked=kicked, left=left, deactivated=deactivated, migrated_to=migrated_to, admin_rights=admin_rights, default_banned_rights=default_banned_rights)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator is not None else 0
        flags |= (1 << 1) if self.kicked is not None else 0
        flags |= (1 << 2) if self.left is not None else 0
        flags |= (1 << 5) if self.deactivated is not None else 0
        flags |= (1 << 6) if self.migrated_to is not None else 0
        flags |= (1 << 14) if self.admin_rights is not None else 0
        flags |= (1 << 18) if self.default_banned_rights is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        b.write(self.photo.write())
        
        b.write(Int(self.participants_count))
        
        b.write(Int(self.date))
        
        b.write(Int(self.version))
        
        if self.migrated_to is not None:
            b.write(self.migrated_to.write())
        
        if self.admin_rights is not None:
            b.write(self.admin_rights.write())
        
        if self.default_banned_rights is not None:
            b.write(self.default_banned_rights.write())
        
        return b.getvalue()
