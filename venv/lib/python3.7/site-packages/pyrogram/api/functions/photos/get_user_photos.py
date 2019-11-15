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


class GetUserPhotos(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x91cd32a8``

    Parameters:
        user_id: Either :obj:`InputUserEmpty <pyrogram.api.types.InputUserEmpty>`, :obj:`InputUserSelf <pyrogram.api.types.InputUserSelf>`, :obj:`InputUser <pyrogram.api.types.InputUser>` or :obj:`InputUserFromMessage <pyrogram.api.types.InputUserFromMessage>`
        offset: ``int`` ``32-bit``
        max_id: ``int`` ``64-bit``
        limit: ``int`` ``32-bit``

    Returns:
        Either :obj:`photos.Photos <pyrogram.api.types.photos.Photos>` or :obj:`photos.PhotosSlice <pyrogram.api.types.photos.PhotosSlice>`
    """

    __slots__ = ["user_id", "offset", "max_id", "limit"]

    ID = 0x91cd32a8
    QUALNAME = "functions.photos.GetUserPhotos"

    def __init__(self, *, user_id, offset: int, max_id: int, limit: int):
        self.user_id = user_id  # InputUser
        self.offset = offset  # int
        self.max_id = max_id  # long
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetUserPhotos":
        # No flags
        
        user_id = TLObject.read(b)
        
        offset = Int.read(b)
        
        max_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetUserPhotos(user_id=user_id, offset=offset, max_id=max_id, limit=limit)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Int(self.offset))
        
        b.write(Long(self.max_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
