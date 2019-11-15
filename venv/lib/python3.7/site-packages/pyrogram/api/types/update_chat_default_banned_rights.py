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


class UpdateChatDefaultBannedRights(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x54c01850``

    Parameters:
        peer: Either :obj:`PeerUser <pyrogram.api.types.PeerUser>`, :obj:`PeerChat <pyrogram.api.types.PeerChat>` or :obj:`PeerChannel <pyrogram.api.types.PeerChannel>`
        default_banned_rights: :obj:`ChatBannedRights <pyrogram.api.types.ChatBannedRights>`
        version: ``int`` ``32-bit``
    """

    __slots__ = ["peer", "default_banned_rights", "version"]

    ID = 0x54c01850
    QUALNAME = "types.UpdateChatDefaultBannedRights"

    def __init__(self, *, peer, default_banned_rights, version: int):
        self.peer = peer  # Peer
        self.default_banned_rights = default_banned_rights  # ChatBannedRights
        self.version = version  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateChatDefaultBannedRights":
        # No flags
        
        peer = TLObject.read(b)
        
        default_banned_rights = TLObject.read(b)
        
        version = Int.read(b)
        
        return UpdateChatDefaultBannedRights(peer=peer, default_banned_rights=default_banned_rights, version=version)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.default_banned_rights.write())
        
        b.write(Int(self.version))
        
        return b.getvalue()
