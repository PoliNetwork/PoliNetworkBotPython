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
        ID: ``0xd246fd47``

    Parameters:
        photo_size_max: ``int`` ``32-bit``
        video_size_max: ``int`` ``32-bit``
        file_size_max: ``int`` ``32-bit``
        disabled (optional): ``bool``
        video_preload_large (optional): ``bool``
        audio_preload_next (optional): ``bool``
        phonecalls_less_data (optional): ``bool``
    """

    __slots__ = ["photo_size_max", "video_size_max", "file_size_max", "disabled", "video_preload_large", "audio_preload_next", "phonecalls_less_data"]

    ID = 0xd246fd47
    QUALNAME = "types.AutoDownloadSettings"

    def __init__(self, *, photo_size_max: int, video_size_max: int, file_size_max: int, disabled: bool = None, video_preload_large: bool = None, audio_preload_next: bool = None, phonecalls_less_data: bool = None):
        self.disabled = disabled  # flags.0?true
        self.video_preload_large = video_preload_large  # flags.1?true
        self.audio_preload_next = audio_preload_next  # flags.2?true
        self.phonecalls_less_data = phonecalls_less_data  # flags.3?true
        self.photo_size_max = photo_size_max  # int
        self.video_size_max = video_size_max  # int
        self.file_size_max = file_size_max  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "AutoDownloadSettings":
        flags = Int.read(b)
        
        disabled = True if flags & (1 << 0) else False
        video_preload_large = True if flags & (1 << 1) else False
        audio_preload_next = True if flags & (1 << 2) else False
        phonecalls_less_data = True if flags & (1 << 3) else False
        photo_size_max = Int.read(b)
        
        video_size_max = Int.read(b)
        
        file_size_max = Int.read(b)
        
        return AutoDownloadSettings(photo_size_max=photo_size_max, video_size_max=video_size_max, file_size_max=file_size_max, disabled=disabled, video_preload_large=video_preload_large, audio_preload_next=audio_preload_next, phonecalls_less_data=phonecalls_less_data)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.disabled is not None else 0
        flags |= (1 << 1) if self.video_preload_large is not None else 0
        flags |= (1 << 2) if self.audio_preload_next is not None else 0
        flags |= (1 << 3) if self.phonecalls_less_data is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.photo_size_max))
        
        b.write(Int(self.video_size_max))
        
        b.write(Int(self.file_size_max))
        
        return b.getvalue()
