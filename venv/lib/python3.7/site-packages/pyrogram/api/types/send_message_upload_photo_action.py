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


class SendMessageUploadPhotoAction(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd1d34a26``

    Parameters:
        progress: ``int`` ``32-bit``
    """

    __slots__ = ["progress"]

    ID = 0xd1d34a26
    QUALNAME = "types.SendMessageUploadPhotoAction"

    def __init__(self, *, progress: int):
        self.progress = progress  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "SendMessageUploadPhotoAction":
        # No flags
        
        progress = Int.read(b)
        
        return SendMessageUploadPhotoAction(progress=progress)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.progress))
        
        return b.getvalue()
