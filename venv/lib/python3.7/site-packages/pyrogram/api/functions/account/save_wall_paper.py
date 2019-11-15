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


class SaveWallPaper(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x6c5a5b37``

    Parameters:
        wallpaper: Either :obj:`InputWallPaper <pyrogram.api.types.InputWallPaper>` or :obj:`InputWallPaperSlug <pyrogram.api.types.InputWallPaperSlug>`
        unsave: ``bool``
        settings: :obj:`WallPaperSettings <pyrogram.api.types.WallPaperSettings>`

    Returns:
        ``bool``
    """

    __slots__ = ["wallpaper", "unsave", "settings"]

    ID = 0x6c5a5b37
    QUALNAME = "functions.account.SaveWallPaper"

    def __init__(self, *, wallpaper, unsave: bool, settings):
        self.wallpaper = wallpaper  # InputWallPaper
        self.unsave = unsave  # Bool
        self.settings = settings  # WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "SaveWallPaper":
        # No flags
        
        wallpaper = TLObject.read(b)
        
        unsave = Bool.read(b)
        
        settings = TLObject.read(b)
        
        return SaveWallPaper(wallpaper=wallpaper, unsave=unsave, settings=settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        b.write(Bool(self.unsave))
        
        b.write(self.settings.write())
        
        return b.getvalue()
