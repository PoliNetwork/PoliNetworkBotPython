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


class PhoneCallWaiting(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1b8f4ad1``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        admin_id: ``int`` ``32-bit``
        participant_id: ``int`` ``32-bit``
        protocol: :obj:`PhoneCallProtocol <pyrogram.api.types.PhoneCallProtocol>`
        video (optional): ``bool``
        receive_date (optional): ``int`` ``32-bit``
    """

    __slots__ = ["id", "access_hash", "date", "admin_id", "participant_id", "protocol", "video", "receive_date"]

    ID = 0x1b8f4ad1
    QUALNAME = "types.PhoneCallWaiting"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, protocol, video: bool = None, receive_date: int = None):
        self.video = video  # flags.5?true
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.protocol = protocol  # PhoneCallProtocol
        self.receive_date = receive_date  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args) -> "PhoneCallWaiting":
        flags = Int.read(b)
        
        video = True if flags & (1 << 5) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Int.read(b)
        
        participant_id = Int.read(b)
        
        protocol = TLObject.read(b)
        
        receive_date = Int.read(b) if flags & (1 << 0) else None
        return PhoneCallWaiting(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, protocol=protocol, video=video, receive_date=receive_date)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.video is not None else 0
        flags |= (1 << 0) if self.receive_date is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Int(self.admin_id))
        
        b.write(Int(self.participant_id))
        
        b.write(self.protocol.write())
        
        if self.receive_date is not None:
            b.write(Int(self.receive_date))
        
        return b.getvalue()
