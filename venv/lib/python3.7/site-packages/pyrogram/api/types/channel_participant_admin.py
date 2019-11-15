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


class ChannelParticipantAdmin(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xccbebbaf``

    Parameters:
        user_id: ``int`` ``32-bit``
        promoted_by: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        admin_rights: :obj:`ChatAdminRights <pyrogram.api.types.ChatAdminRights>`
        can_edit (optional): ``bool``
        is_self (optional): ``bool``
        inviter_id (optional): ``int`` ``32-bit``
        rank (optional): ``str``
    """

    __slots__ = ["user_id", "promoted_by", "date", "admin_rights", "can_edit", "is_self", "inviter_id", "rank"]

    ID = 0xccbebbaf
    QUALNAME = "types.ChannelParticipantAdmin"

    def __init__(self, *, user_id: int, promoted_by: int, date: int, admin_rights, can_edit: bool = None, is_self: bool = None, inviter_id: int = None, rank: str = None):
        self.can_edit = can_edit  # flags.0?true
        self.is_self = is_self  # flags.1?true
        self.user_id = user_id  # int
        self.inviter_id = inviter_id  # flags.1?int
        self.promoted_by = promoted_by  # int
        self.date = date  # int
        self.admin_rights = admin_rights  # ChatAdminRights
        self.rank = rank  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelParticipantAdmin":
        flags = Int.read(b)
        
        can_edit = True if flags & (1 << 0) else False
        is_self = True if flags & (1 << 1) else False
        user_id = Int.read(b)
        
        inviter_id = Int.read(b) if flags & (1 << 1) else None
        promoted_by = Int.read(b)
        
        date = Int.read(b)
        
        admin_rights = TLObject.read(b)
        
        rank = String.read(b) if flags & (1 << 2) else None
        return ChannelParticipantAdmin(user_id=user_id, promoted_by=promoted_by, date=date, admin_rights=admin_rights, can_edit=can_edit, is_self=is_self, inviter_id=inviter_id, rank=rank)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.can_edit is not None else 0
        flags |= (1 << 1) if self.is_self is not None else 0
        flags |= (1 << 1) if self.inviter_id is not None else 0
        flags |= (1 << 2) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.user_id))
        
        if self.inviter_id is not None:
            b.write(Int(self.inviter_id))
        
        b.write(Int(self.promoted_by))
        
        b.write(Int(self.date))
        
        b.write(self.admin_rights.write())
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()
