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


class StickerSetInstallResultArchive(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x35e410a8``

    Parameters:
        sets: List of either :obj:`StickerSetCovered <pyrogram.api.types.StickerSetCovered>` or :obj:`StickerSetMultiCovered <pyrogram.api.types.StickerSetMultiCovered>`

    See Also:
        This object can be returned by :obj:`messages.InstallStickerSet <pyrogram.api.functions.messages.InstallStickerSet>`.
    """

    __slots__ = ["sets"]

    ID = 0x35e410a8
    QUALNAME = "types.messages.StickerSetInstallResultArchive"

    def __init__(self, *, sets: list):
        self.sets = sets  # Vector<StickerSetCovered>

    @staticmethod
    def read(b: BytesIO, *args) -> "StickerSetInstallResultArchive":
        # No flags
        
        sets = TLObject.read(b)
        
        return StickerSetInstallResultArchive(sets=sets)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.sets))
        
        return b.getvalue()
