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


class DeleteScheduledMessages(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x59ae2b16``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        id: List of ``int`` ``32-bit``

    Returns:
        Either :obj:`UpdatesTooLong <pyrogram.api.types.UpdatesTooLong>`, :obj:`UpdateShortMessage <pyrogram.api.types.UpdateShortMessage>`, :obj:`UpdateShortChatMessage <pyrogram.api.types.UpdateShortChatMessage>`, :obj:`UpdateShort <pyrogram.api.types.UpdateShort>`, :obj:`UpdatesCombined <pyrogram.api.types.UpdatesCombined>`, :obj:`Update <pyrogram.api.types.Update>` or :obj:`UpdateShortSentMessage <pyrogram.api.types.UpdateShortSentMessage>`
    """

    __slots__ = ["peer", "id"]

    ID = 0x59ae2b16
    QUALNAME = "functions.messages.DeleteScheduledMessages"

    def __init__(self, *, peer, id: list):
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args) -> "DeleteScheduledMessages":
        # No flags
        
        peer = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        return DeleteScheduledMessages(peer=peer, id=id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        return b.getvalue()
