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


class SaveAutoDownloadSettings(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x76f36233``

    Parameters:
        settings: :obj:`AutoDownloadSettings <pyrogram.api.types.AutoDownloadSettings>`
        low (optional): ``bool``
        high (optional): ``bool``

    Returns:
        ``bool``
    """

    __slots__ = ["settings", "low", "high"]

    ID = 0x76f36233
    QUALNAME = "functions.account.SaveAutoDownloadSettings"

    def __init__(self, *, settings, low: bool = None, high: bool = None):
        self.low = low  # flags.0?true
        self.high = high  # flags.1?true
        self.settings = settings  # AutoDownloadSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "SaveAutoDownloadSettings":
        flags = Int.read(b)
        
        low = True if flags & (1 << 0) else False
        high = True if flags & (1 << 1) else False
        settings = TLObject.read(b)
        
        return SaveAutoDownloadSettings(settings=settings, low=low, high=high)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.low is not None else 0
        flags |= (1 << 1) if self.high is not None else 0
        b.write(Int(flags))
        
        b.write(self.settings.write())
        
        return b.getvalue()
