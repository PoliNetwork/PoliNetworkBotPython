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


class GetAttachedStickers(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xcc5b67cc``

    Parameters:
        media: Either :obj:`InputStickeredMediaPhoto <pyrogram.api.types.InputStickeredMediaPhoto>` or :obj:`InputStickeredMediaDocument <pyrogram.api.types.InputStickeredMediaDocument>`

    Returns:
        List of either :obj:`StickerSetCovered <pyrogram.api.types.StickerSetCovered>` or :obj:`StickerSetMultiCovered <pyrogram.api.types.StickerSetMultiCovered>`
    """

    __slots__ = ["media"]

    ID = 0xcc5b67cc
    QUALNAME = "functions.messages.GetAttachedStickers"

    def __init__(self, *, media):
        self.media = media  # InputStickeredMedia

    @staticmethod
    def read(b: BytesIO, *args) -> "GetAttachedStickers":
        # No flags
        
        media = TLObject.read(b)
        
        return GetAttachedStickers(media=media)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.media.write())
        
        return b.getvalue()
