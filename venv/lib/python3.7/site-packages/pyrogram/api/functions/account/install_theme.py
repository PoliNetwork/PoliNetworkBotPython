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


class InstallTheme(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x7ae43737``

    Parameters:
        dark (optional): ``bool``
        format (optional): ``str``
        theme (optional): Either :obj:`InputTheme <pyrogram.api.types.InputTheme>` or :obj:`InputThemeSlug <pyrogram.api.types.InputThemeSlug>`

    Returns:
        ``bool``
    """

    __slots__ = ["dark", "format", "theme"]

    ID = 0x7ae43737
    QUALNAME = "functions.account.InstallTheme"

    def __init__(self, *, dark: bool = None, format: str = None, theme=None):
        self.dark = dark  # flags.0?true
        self.format = format  # flags.1?string
        self.theme = theme  # flags.1?InputTheme

    @staticmethod
    def read(b: BytesIO, *args) -> "InstallTheme":
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        format = String.read(b) if flags & (1 << 1) else None
        theme = TLObject.read(b) if flags & (1 << 1) else None
        
        return InstallTheme(dark=dark, format=format, theme=theme)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark is not None else 0
        flags |= (1 << 1) if self.format is not None else 0
        flags |= (1 << 1) if self.theme is not None else 0
        b.write(Int(flags))
        
        if self.format is not None:
            b.write(String(self.format))
        
        if self.theme is not None:
            b.write(self.theme.write())
        
        return b.getvalue()
