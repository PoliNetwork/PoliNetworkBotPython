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


class InputPeerPhotoFileLocation(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x27d69997``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        volume_id: ``int`` ``64-bit``
        local_id: ``int`` ``32-bit``
        big (optional): ``bool``
    """

    __slots__ = ["peer", "volume_id", "local_id", "big"]

    ID = 0x27d69997
    QUALNAME = "types.InputPeerPhotoFileLocation"

    def __init__(self, *, peer, volume_id: int, local_id: int, big: bool = None):
        self.big = big  # flags.0?true
        self.peer = peer  # InputPeer
        self.volume_id = volume_id  # long
        self.local_id = local_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "InputPeerPhotoFileLocation":
        flags = Int.read(b)
        
        big = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        volume_id = Long.read(b)
        
        local_id = Int.read(b)
        
        return InputPeerPhotoFileLocation(peer=peer, volume_id=volume_id, local_id=local_id, big=big)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.volume_id))
        
        b.write(Int(self.local_id))
        
        return b.getvalue()
