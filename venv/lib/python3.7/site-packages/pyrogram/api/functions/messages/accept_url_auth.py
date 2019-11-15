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


class AcceptUrlAuth(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf729ea98``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        msg_id: ``int`` ``32-bit``
        button_id: ``int`` ``32-bit``
        write_allowed (optional): ``bool``

    Returns:
        Either :obj:`UrlAuthResultRequest <pyrogram.api.types.UrlAuthResultRequest>`, :obj:`UrlAuthResultAccepted <pyrogram.api.types.UrlAuthResultAccepted>` or :obj:`UrlAuthResultDefault <pyrogram.api.types.UrlAuthResultDefault>`
    """

    __slots__ = ["peer", "msg_id", "button_id", "write_allowed"]

    ID = 0xf729ea98
    QUALNAME = "functions.messages.AcceptUrlAuth"

    def __init__(self, *, peer, msg_id: int, button_id: int, write_allowed: bool = None):
        self.write_allowed = write_allowed  # flags.0?true
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.button_id = button_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "AcceptUrlAuth":
        flags = Int.read(b)
        
        write_allowed = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        button_id = Int.read(b)
        
        return AcceptUrlAuth(peer=peer, msg_id=msg_id, button_id=button_id, write_allowed=write_allowed)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.write_allowed is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Int(self.button_id))
        
        return b.getvalue()
