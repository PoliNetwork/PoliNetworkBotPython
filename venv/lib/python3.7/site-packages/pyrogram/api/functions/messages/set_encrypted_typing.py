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


class SetEncryptedTyping(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x791451ed``

    Parameters:
        peer: :obj:`InputEncryptedChat <pyrogram.api.types.InputEncryptedChat>`
        typing: ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["peer", "typing"]

    ID = 0x791451ed
    QUALNAME = "functions.messages.SetEncryptedTyping"

    def __init__(self, *, peer, typing: bool):
        self.peer = peer  # InputEncryptedChat
        self.typing = typing  # Bool

    @staticmethod
    def read(b: BytesIO, *args) -> "SetEncryptedTyping":
        # No flags
        
        peer = TLObject.read(b)
        
        typing = Bool.read(b)
        
        return SetEncryptedTyping(peer=peer, typing=typing)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bool(self.typing))
        
        return b.getvalue()
