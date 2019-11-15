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


class GetPinnedDialogs(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd6b94df2``

    Parameters:
        folder_id: ``int`` ``32-bit``

    Returns:
        :obj:`messages.PeerDialogs <pyrogram.api.types.messages.PeerDialogs>`
    """

    __slots__ = ["folder_id"]

    ID = 0xd6b94df2
    QUALNAME = "functions.messages.GetPinnedDialogs"

    def __init__(self, *, folder_id: int):
        self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetPinnedDialogs":
        # No flags
        
        folder_id = Int.read(b)
        
        return GetPinnedDialogs(folder_id=folder_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.folder_id))
        
        return b.getvalue()
