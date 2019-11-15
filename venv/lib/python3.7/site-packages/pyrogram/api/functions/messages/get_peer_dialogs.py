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


class GetPeerDialogs(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xe470bcfd``

    Parameters:
        peers: List of either :obj:`InputDialogPeer <pyrogram.api.types.InputDialogPeer>` or :obj:`InputDialogPeerFolder <pyrogram.api.types.InputDialogPeerFolder>`

    Returns:
        :obj:`messages.PeerDialogs <pyrogram.api.types.messages.PeerDialogs>`
    """

    __slots__ = ["peers"]

    ID = 0xe470bcfd
    QUALNAME = "functions.messages.GetPeerDialogs"

    def __init__(self, *, peers: list):
        self.peers = peers  # Vector<InputDialogPeer>

    @staticmethod
    def read(b: BytesIO, *args) -> "GetPeerDialogs":
        # No flags
        
        peers = TLObject.read(b)
        
        return GetPeerDialogs(peers=peers)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.peers))
        
        return b.getvalue()
