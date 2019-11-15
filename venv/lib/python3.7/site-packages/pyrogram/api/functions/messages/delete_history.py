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


class DeleteHistory(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1c015b09``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        max_id: ``int`` ``32-bit``
        just_clear (optional): ``bool``
        revoke (optional): ``bool``

    Returns:
        :obj:`messages.AffectedHistory <pyrogram.api.types.messages.AffectedHistory>`
    """

    __slots__ = ["peer", "max_id", "just_clear", "revoke"]

    ID = 0x1c015b09
    QUALNAME = "functions.messages.DeleteHistory"

    def __init__(self, *, peer, max_id: int, just_clear: bool = None, revoke: bool = None):
        self.just_clear = just_clear  # flags.0?true
        self.revoke = revoke  # flags.1?true
        self.peer = peer  # InputPeer
        self.max_id = max_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "DeleteHistory":
        flags = Int.read(b)
        
        just_clear = True if flags & (1 << 0) else False
        revoke = True if flags & (1 << 1) else False
        peer = TLObject.read(b)
        
        max_id = Int.read(b)
        
        return DeleteHistory(peer=peer, max_id=max_id, just_clear=just_clear, revoke=revoke)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.just_clear is not None else 0
        flags |= (1 << 1) if self.revoke is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.max_id))
        
        return b.getvalue()
