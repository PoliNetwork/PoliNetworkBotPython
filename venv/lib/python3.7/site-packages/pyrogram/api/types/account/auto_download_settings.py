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


class AutoDownloadSettings(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x63cacf26``

    Parameters:
        low: :obj:`AutoDownloadSettings <pyrogram.api.types.AutoDownloadSettings>`
        medium: :obj:`AutoDownloadSettings <pyrogram.api.types.AutoDownloadSettings>`
        high: :obj:`AutoDownloadSettings <pyrogram.api.types.AutoDownloadSettings>`

    See Also:
        This object can be returned by :obj:`account.GetAutoDownloadSettings <pyrogram.api.functions.account.GetAutoDownloadSettings>`.
    """

    __slots__ = ["low", "medium", "high"]

    ID = 0x63cacf26
    QUALNAME = "types.account.AutoDownloadSettings"

    def __init__(self, *, low, medium, high):
        self.low = low  # AutoDownloadSettings
        self.medium = medium  # AutoDownloadSettings
        self.high = high  # AutoDownloadSettings

    @staticmethod
    def read(b: BytesIO, *args) -> "AutoDownloadSettings":
        # No flags
        
        low = TLObject.read(b)
        
        medium = TLObject.read(b)
        
        high = TLObject.read(b)
        
        return AutoDownloadSettings(low=low, medium=medium, high=high)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.low.write())
        
        b.write(self.medium.write())
        
        b.write(self.high.write())
        
        return b.getvalue()
