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


class DocumentAttributeSticker(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x6319d612``

    Parameters:
        alt: ``str``
        stickerset: Either :obj:`InputStickerSetEmpty <pyrogram.api.types.InputStickerSetEmpty>`, :obj:`InputStickerSetID <pyrogram.api.types.InputStickerSetID>`, :obj:`InputStickerSetShortName <pyrogram.api.types.InputStickerSetShortName>` or :obj:`InputStickerSetAnimatedEmoji <pyrogram.api.types.InputStickerSetAnimatedEmoji>`
        mask (optional): ``bool``
        mask_coords (optional): :obj:`MaskCoords <pyrogram.api.types.MaskCoords>`
    """

    __slots__ = ["alt", "stickerset", "mask", "mask_coords"]

    ID = 0x6319d612
    QUALNAME = "types.DocumentAttributeSticker"

    def __init__(self, *, alt: str, stickerset, mask: bool = None, mask_coords=None):
        self.mask = mask  # flags.1?true
        self.alt = alt  # string
        self.stickerset = stickerset  # InputStickerSet
        self.mask_coords = mask_coords  # flags.0?MaskCoords

    @staticmethod
    def read(b: BytesIO, *args) -> "DocumentAttributeSticker":
        flags = Int.read(b)
        
        mask = True if flags & (1 << 1) else False
        alt = String.read(b)
        
        stickerset = TLObject.read(b)
        
        mask_coords = TLObject.read(b) if flags & (1 << 0) else None
        
        return DocumentAttributeSticker(alt=alt, stickerset=stickerset, mask=mask, mask_coords=mask_coords)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.mask is not None else 0
        flags |= (1 << 0) if self.mask_coords is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.alt))
        
        b.write(self.stickerset.write())
        
        if self.mask_coords is not None:
            b.write(self.mask_coords.write())
        
        return b.getvalue()
