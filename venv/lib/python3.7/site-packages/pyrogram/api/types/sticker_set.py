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


class StickerSet(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xeeb46f27``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        title: ``str``
        short_name: ``str``
        count: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``
        archived (optional): ``bool``
        official (optional): ``bool``
        masks (optional): ``bool``
        animated (optional): ``bool``
        installed_date (optional): ``int`` ``32-bit``
        thumb (optional): Either :obj:`PhotoSizeEmpty <pyrogram.api.types.PhotoSizeEmpty>`, :obj:`PhotoSize <pyrogram.api.types.PhotoSize>`, :obj:`PhotoCachedSize <pyrogram.api.types.PhotoCachedSize>` or :obj:`PhotoStrippedSize <pyrogram.api.types.PhotoStrippedSize>`
        thumb_dc_id (optional): ``int`` ``32-bit``
    """

    __slots__ = ["id", "access_hash", "title", "short_name", "count", "hash", "archived", "official", "masks", "animated", "installed_date", "thumb", "thumb_dc_id"]

    ID = 0xeeb46f27
    QUALNAME = "types.StickerSet"

    def __init__(self, *, id: int, access_hash: int, title: str, short_name: str, count: int, hash: int, archived: bool = None, official: bool = None, masks: bool = None, animated: bool = None, installed_date: int = None, thumb=None, thumb_dc_id: int = None):
        self.archived = archived  # flags.1?true
        self.official = official  # flags.2?true
        self.masks = masks  # flags.3?true
        self.animated = animated  # flags.5?true
        self.installed_date = installed_date  # flags.0?int
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.title = title  # string
        self.short_name = short_name  # string
        self.thumb = thumb  # flags.4?PhotoSize
        self.thumb_dc_id = thumb_dc_id  # flags.4?int
        self.count = count  # int
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "StickerSet":
        flags = Int.read(b)
        
        archived = True if flags & (1 << 1) else False
        official = True if flags & (1 << 2) else False
        masks = True if flags & (1 << 3) else False
        animated = True if flags & (1 << 5) else False
        installed_date = Int.read(b) if flags & (1 << 0) else None
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        title = String.read(b)
        
        short_name = String.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 4) else None
        
        thumb_dc_id = Int.read(b) if flags & (1 << 4) else None
        count = Int.read(b)
        
        hash = Int.read(b)
        
        return StickerSet(id=id, access_hash=access_hash, title=title, short_name=short_name, count=count, hash=hash, archived=archived, official=official, masks=masks, animated=animated, installed_date=installed_date, thumb=thumb, thumb_dc_id=thumb_dc_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.archived is not None else 0
        flags |= (1 << 2) if self.official is not None else 0
        flags |= (1 << 3) if self.masks is not None else 0
        flags |= (1 << 5) if self.animated is not None else 0
        flags |= (1 << 0) if self.installed_date is not None else 0
        flags |= (1 << 4) if self.thumb is not None else 0
        flags |= (1 << 4) if self.thumb_dc_id is not None else 0
        b.write(Int(flags))
        
        if self.installed_date is not None:
            b.write(Int(self.installed_date))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.title))
        
        b.write(String(self.short_name))
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        if self.thumb_dc_id is not None:
            b.write(Int(self.thumb_dc_id))
        
        b.write(Int(self.count))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
