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


class PhoneCallAccepted(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x997c454a``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        admin_id: ``int`` ``32-bit``
        participant_id: ``int`` ``32-bit``
        g_b: ``bytes``
        protocol: :obj:`PhoneCallProtocol <pyrogram.api.types.PhoneCallProtocol>`
        video (optional): ``bool``
    """

    __slots__ = ["id", "access_hash", "date", "admin_id", "participant_id", "g_b", "protocol", "video"]

    ID = 0x997c454a
    QUALNAME = "types.PhoneCallAccepted"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_b: bytes, protocol, video: bool = None):
        self.video = video  # flags.5?true
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.g_b = g_b  # bytes
        self.protocol = protocol  # PhoneCallProtocol

    @staticmethod
    def read(b: BytesIO, *args) -> "PhoneCallAccepted":
        flags = Int.read(b)
        
        video = True if flags & (1 << 5) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Int.read(b)
        
        participant_id = Int.read(b)
        
        g_b = Bytes.read(b)
        
        protocol = TLObject.read(b)
        
        return PhoneCallAccepted(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_b=g_b, protocol=protocol, video=video)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.video is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Int(self.admin_id))
        
        b.write(Int(self.participant_id))
        
        b.write(Bytes(self.g_b))
        
        b.write(self.protocol.write())
        
        return b.getvalue()
