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


class CreateStickerSet(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x9bd86e6a``

    Parameters:
        user_id: Either :obj:`InputUserEmpty <pyrogram.api.types.InputUserEmpty>`, :obj:`InputUserSelf <pyrogram.api.types.InputUserSelf>`, :obj:`InputUser <pyrogram.api.types.InputUser>` or :obj:`InputUserFromMessage <pyrogram.api.types.InputUserFromMessage>`
        title: ``str``
        short_name: ``str``
        stickers: List of :obj:`InputStickerSetItem <pyrogram.api.types.InputStickerSetItem>`
        masks (optional): ``bool``

    Returns:
        :obj:`messages.StickerSet <pyrogram.api.types.messages.StickerSet>`
    """

    __slots__ = ["user_id", "title", "short_name", "stickers", "masks"]

    ID = 0x9bd86e6a
    QUALNAME = "functions.stickers.CreateStickerSet"

    def __init__(self, *, user_id, title: str, short_name: str, stickers: list, masks: bool = None):
        self.masks = masks  # flags.0?true
        self.user_id = user_id  # InputUser
        self.title = title  # string
        self.short_name = short_name  # string
        self.stickers = stickers  # Vector<InputStickerSetItem>

    @staticmethod
    def read(b: BytesIO, *args) -> "CreateStickerSet":
        flags = Int.read(b)
        
        masks = True if flags & (1 << 0) else False
        user_id = TLObject.read(b)
        
        title = String.read(b)
        
        short_name = String.read(b)
        
        stickers = TLObject.read(b)
        
        return CreateStickerSet(user_id=user_id, title=title, short_name=short_name, stickers=stickers, masks=masks)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.masks is not None else 0
        b.write(Int(flags))
        
        b.write(self.user_id.write())
        
        b.write(String(self.title))
        
        b.write(String(self.short_name))
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()
