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


class DeletePhotos(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x87cf7f2f``

    Parameters:
        id: List of either :obj:`InputPhotoEmpty <pyrogram.api.types.InputPhotoEmpty>` or :obj:`InputPhoto <pyrogram.api.types.InputPhoto>`

    Returns:
        List of ``int`` ``64-bit``
    """

    __slots__ = ["id"]

    ID = 0x87cf7f2f
    QUALNAME = "functions.photos.DeletePhotos"

    def __init__(self, *, id: list):
        self.id = id  # Vector<InputPhoto>

    @staticmethod
    def read(b: BytesIO, *args) -> "DeletePhotos":
        # No flags
        
        id = TLObject.read(b)
        
        return DeletePhotos(id=id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.id))
        
        return b.getvalue()
