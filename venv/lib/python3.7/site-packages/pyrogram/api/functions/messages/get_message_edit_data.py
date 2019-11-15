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


class GetMessageEditData(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xfda68d36``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        id: ``int`` ``32-bit``

    Returns:
        :obj:`messages.MessageEditData <pyrogram.api.types.messages.MessageEditData>`
    """

    __slots__ = ["peer", "id"]

    ID = 0xfda68d36
    QUALNAME = "functions.messages.GetMessageEditData"

    def __init__(self, *, peer, id: int):
        self.peer = peer  # InputPeer
        self.id = id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetMessageEditData":
        # No flags
        
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        return GetMessageEditData(peer=peer, id=id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()
