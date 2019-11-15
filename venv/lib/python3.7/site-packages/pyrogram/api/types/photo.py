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


class Photo(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd07504a5``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        file_reference: ``bytes``
        date: ``int`` ``32-bit``
        sizes: List of either :obj:`PhotoSizeEmpty <pyrogram.api.types.PhotoSizeEmpty>`, :obj:`PhotoSize <pyrogram.api.types.PhotoSize>`, :obj:`PhotoCachedSize <pyrogram.api.types.PhotoCachedSize>` or :obj:`PhotoStrippedSize <pyrogram.api.types.PhotoStrippedSize>`
        dc_id: ``int`` ``32-bit``
        has_stickers (optional): ``bool``
    """

    __slots__ = ["id", "access_hash", "file_reference", "date", "sizes", "dc_id", "has_stickers"]

    ID = 0xd07504a5
    QUALNAME = "types.Photo"

    def __init__(self, *, id: int, access_hash: int, file_reference: bytes, date: int, sizes: list, dc_id: int, has_stickers: bool = None):
        self.has_stickers = has_stickers  # flags.0?true
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.file_reference = file_reference  # bytes
        self.date = date  # int
        self.sizes = sizes  # Vector<PhotoSize>
        self.dc_id = dc_id  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "Photo":
        flags = Int.read(b)
        
        has_stickers = True if flags & (1 << 0) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        file_reference = Bytes.read(b)
        
        date = Int.read(b)
        
        sizes = TLObject.read(b)
        
        dc_id = Int.read(b)
        
        return Photo(id=id, access_hash=access_hash, file_reference=file_reference, date=date, sizes=sizes, dc_id=dc_id, has_stickers=has_stickers)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.has_stickers is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Bytes(self.file_reference))
        
        b.write(Int(self.date))
        
        b.write(Vector(self.sizes))
        
        b.write(Int(self.dc_id))
        
        return b.getvalue()
