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


class UpdateDraftMessage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xee2bb969``

    Parameters:
        peer: Either :obj:`PeerUser <pyrogram.api.types.PeerUser>`, :obj:`PeerChat <pyrogram.api.types.PeerChat>` or :obj:`PeerChannel <pyrogram.api.types.PeerChannel>`
        draft: Either :obj:`DraftMessageEmpty <pyrogram.api.types.DraftMessageEmpty>` or :obj:`DraftMessage <pyrogram.api.types.DraftMessage>`
    """

    __slots__ = ["peer", "draft"]

    ID = 0xee2bb969
    QUALNAME = "types.UpdateDraftMessage"

    def __init__(self, *, peer, draft):
        self.peer = peer  # Peer
        self.draft = draft  # DraftMessage

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateDraftMessage":
        # No flags
        
        peer = TLObject.read(b)
        
        draft = TLObject.read(b)
        
        return UpdateDraftMessage(peer=peer, draft=draft)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.draft.write())
        
        return b.getvalue()
