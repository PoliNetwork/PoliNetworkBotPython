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


class PhoneCall(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x8742ae7f``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        admin_id: ``int`` ``32-bit``
        participant_id: ``int`` ``32-bit``
        g_a_or_b: ``bytes``
        key_fingerprint: ``int`` ``64-bit``
        protocol: :obj:`PhoneCallProtocol <pyrogram.api.types.PhoneCallProtocol>`
        connections: List of :obj:`PhoneConnection <pyrogram.api.types.PhoneConnection>`
        start_date: ``int`` ``32-bit``
        p2p_allowed (optional): ``bool``
    """

    __slots__ = ["id", "access_hash", "date", "admin_id", "participant_id", "g_a_or_b", "key_fingerprint", "protocol", "connections", "start_date", "p2p_allowed"]

    ID = 0x8742ae7f
    QUALNAME = "types.PhoneCall"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int, g_a_or_b: bytes, key_fingerprint: int, protocol, connections: list, start_date: int, p2p_allowed: bool = None):
        self.p2p_allowed = p2p_allowed  # flags.5?true
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.g_a_or_b = g_a_or_b  # bytes
        self.key_fingerprint = key_fingerprint  # long
        self.protocol = protocol  # PhoneCallProtocol
        self.connections = connections  # Vector<PhoneConnection>
        self.start_date = start_date  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "PhoneCall":
        flags = Int.read(b)
        
        p2p_allowed = True if flags & (1 << 5) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Int.read(b)
        
        participant_id = Int.read(b)
        
        g_a_or_b = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        protocol = TLObject.read(b)
        
        connections = TLObject.read(b)
        
        start_date = Int.read(b)
        
        return PhoneCall(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id, g_a_or_b=g_a_or_b, key_fingerprint=key_fingerprint, protocol=protocol, connections=connections, start_date=start_date, p2p_allowed=p2p_allowed)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.p2p_allowed is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Int(self.admin_id))
        
        b.write(Int(self.participant_id))
        
        b.write(Bytes(self.g_a_or_b))
        
        b.write(Long(self.key_fingerprint))
        
        b.write(self.protocol.write())
        
        b.write(Vector(self.connections))
        
        b.write(Int(self.start_date))
        
        return b.getvalue()
