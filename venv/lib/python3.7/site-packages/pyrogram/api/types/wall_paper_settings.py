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


class WallPaperSettings(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xa12f40b8``

    Parameters:
        blur (optional): ``bool``
        motion (optional): ``bool``
        background_color (optional): ``int`` ``32-bit``
        intensity (optional): ``int`` ``32-bit``
    """

    __slots__ = ["blur", "motion", "background_color", "intensity"]

    ID = 0xa12f40b8
    QUALNAME = "types.WallPaperSettings"

    def __init__(self, *, blur: bool = None, motion: bool = None, background_color: int = None, intensity: int = None):
        self.blur = blur  # flags.1?true
        self.motion = motion  # flags.2?true
        self.background_color = background_color  # flags.0?int
        self.intensity = intensity  # flags.3?int

    @staticmethod
    def read(b: BytesIO, *args) -> "WallPaperSettings":
        flags = Int.read(b)
        
        blur = True if flags & (1 << 1) else False
        motion = True if flags & (1 << 2) else False
        background_color = Int.read(b) if flags & (1 << 0) else None
        intensity = Int.read(b) if flags & (1 << 3) else None
        return WallPaperSettings(blur=blur, motion=motion, background_color=background_color, intensity=intensity)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.blur is not None else 0
        flags |= (1 << 2) if self.motion is not None else 0
        flags |= (1 << 0) if self.background_color is not None else 0
        flags |= (1 << 3) if self.intensity is not None else 0
        b.write(Int(flags))
        
        if self.background_color is not None:
            b.write(Int(self.background_color))
        
        if self.intensity is not None:
            b.write(Int(self.intensity))
        
        return b.getvalue()
