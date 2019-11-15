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


class Channel(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd31a961e``

    Parameters:
        id: ``int`` ``32-bit``
        title: ``str``
        photo: Either :obj:`ChatPhotoEmpty <pyrogram.api.types.ChatPhotoEmpty>` or :obj:`ChatPhoto <pyrogram.api.types.ChatPhoto>`
        date: ``int`` ``32-bit``
        version: ``int`` ``32-bit``
        creator (optional): ``bool``
        left (optional): ``bool``
        broadcast (optional): ``bool``
        verified (optional): ``bool``
        megagroup (optional): ``bool``
        restricted (optional): ``bool``
        signatures (optional): ``bool``
        min (optional): ``bool``
        scam (optional): ``bool``
        has_link (optional): ``bool``
        has_geo (optional): ``bool``
        slowmode_enabled (optional): ``bool``
        access_hash (optional): ``int`` ``64-bit``
        username (optional): ``str``
        restriction_reason (optional): List of :obj:`RestrictionReason <pyrogram.api.types.RestrictionReason>`
        admin_rights (optional): :obj:`ChatAdminRights <pyrogram.api.types.ChatAdminRights>`
        banned_rights (optional): :obj:`ChatBannedRights <pyrogram.api.types.ChatBannedRights>`
        default_banned_rights (optional): :obj:`ChatBannedRights <pyrogram.api.types.ChatBannedRights>`
        participants_count (optional): ``int`` ``32-bit``
    """

    __slots__ = ["id", "title", "photo", "date", "version", "creator", "left", "broadcast", "verified", "megagroup", "restricted", "signatures", "min", "scam", "has_link", "has_geo", "slowmode_enabled", "access_hash", "username", "restriction_reason", "admin_rights", "banned_rights", "default_banned_rights", "participants_count"]

    ID = 0xd31a961e
    QUALNAME = "types.Channel"

    def __init__(self, *, id: int, title: str, photo, date: int, version: int, creator: bool = None, left: bool = None, broadcast: bool = None, verified: bool = None, megagroup: bool = None, restricted: bool = None, signatures: bool = None, min: bool = None, scam: bool = None, has_link: bool = None, has_geo: bool = None, slowmode_enabled: bool = None, access_hash: int = None, username: str = None, restriction_reason: list = None, admin_rights=None, banned_rights=None, default_banned_rights=None, participants_count: int = None):
        self.creator = creator  # flags.0?true
        self.left = left  # flags.2?true
        self.broadcast = broadcast  # flags.5?true
        self.verified = verified  # flags.7?true
        self.megagroup = megagroup  # flags.8?true
        self.restricted = restricted  # flags.9?true
        self.signatures = signatures  # flags.11?true
        self.min = min  # flags.12?true
        self.scam = scam  # flags.19?true
        self.has_link = has_link  # flags.20?true
        self.has_geo = has_geo  # flags.21?true
        self.slowmode_enabled = slowmode_enabled  # flags.22?true
        self.id = id  # int
        self.access_hash = access_hash  # flags.13?long
        self.title = title  # string
        self.username = username  # flags.6?string
        self.photo = photo  # ChatPhoto
        self.date = date  # int
        self.version = version  # int
        self.restriction_reason = restriction_reason  # flags.9?Vector<RestrictionReason>
        self.admin_rights = admin_rights  # flags.14?ChatAdminRights
        self.banned_rights = banned_rights  # flags.15?ChatBannedRights
        self.default_banned_rights = default_banned_rights  # flags.18?ChatBannedRights
        self.participants_count = participants_count  # flags.17?int

    @staticmethod
    def read(b: BytesIO, *args) -> "Channel":
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        left = True if flags & (1 << 2) else False
        broadcast = True if flags & (1 << 5) else False
        verified = True if flags & (1 << 7) else False
        megagroup = True if flags & (1 << 8) else False
        restricted = True if flags & (1 << 9) else False
        signatures = True if flags & (1 << 11) else False
        min = True if flags & (1 << 12) else False
        scam = True if flags & (1 << 19) else False
        has_link = True if flags & (1 << 20) else False
        has_geo = True if flags & (1 << 21) else False
        slowmode_enabled = True if flags & (1 << 22) else False
        id = Int.read(b)
        
        access_hash = Long.read(b) if flags & (1 << 13) else None
        title = String.read(b)
        
        username = String.read(b) if flags & (1 << 6) else None
        photo = TLObject.read(b)
        
        date = Int.read(b)
        
        version = Int.read(b)
        
        restriction_reason = TLObject.read(b) if flags & (1 << 9) else []
        
        admin_rights = TLObject.read(b) if flags & (1 << 14) else None
        
        banned_rights = TLObject.read(b) if flags & (1 << 15) else None
        
        default_banned_rights = TLObject.read(b) if flags & (1 << 18) else None
        
        participants_count = Int.read(b) if flags & (1 << 17) else None
        return Channel(id=id, title=title, photo=photo, date=date, version=version, creator=creator, left=left, broadcast=broadcast, verified=verified, megagroup=megagroup, restricted=restricted, signatures=signatures, min=min, scam=scam, has_link=has_link, has_geo=has_geo, slowmode_enabled=slowmode_enabled, access_hash=access_hash, username=username, restriction_reason=restriction_reason, admin_rights=admin_rights, banned_rights=banned_rights, default_banned_rights=default_banned_rights, participants_count=participants_count)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator is not None else 0
        flags |= (1 << 2) if self.left is not None else 0
        flags |= (1 << 5) if self.broadcast is not None else 0
        flags |= (1 << 7) if self.verified is not None else 0
        flags |= (1 << 8) if self.megagroup is not None else 0
        flags |= (1 << 9) if self.restricted is not None else 0
        flags |= (1 << 11) if self.signatures is not None else 0
        flags |= (1 << 12) if self.min is not None else 0
        flags |= (1 << 19) if self.scam is not None else 0
        flags |= (1 << 20) if self.has_link is not None else 0
        flags |= (1 << 21) if self.has_geo is not None else 0
        flags |= (1 << 22) if self.slowmode_enabled is not None else 0
        flags |= (1 << 13) if self.access_hash is not None else 0
        flags |= (1 << 6) if self.username is not None else 0
        flags |= (1 << 9) if self.restriction_reason is not None else 0
        flags |= (1 << 14) if self.admin_rights is not None else 0
        flags |= (1 << 15) if self.banned_rights is not None else 0
        flags |= (1 << 18) if self.default_banned_rights is not None else 0
        flags |= (1 << 17) if self.participants_count is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.access_hash is not None:
            b.write(Long(self.access_hash))
        
        b.write(String(self.title))
        
        if self.username is not None:
            b.write(String(self.username))
        
        b.write(self.photo.write())
        
        b.write(Int(self.date))
        
        b.write(Int(self.version))
        
        if self.restriction_reason is not None:
            b.write(Vector(self.restriction_reason))
        
        if self.admin_rights is not None:
            b.write(self.admin_rights.write())
        
        if self.banned_rights is not None:
            b.write(self.banned_rights.write())
        
        if self.default_banned_rights is not None:
            b.write(self.default_banned_rights.write())
        
        if self.participants_count is not None:
            b.write(Int(self.participants_count))
        
        return b.getvalue()
