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


class UploadTheme(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1c3db333``

    Parameters:
        file: Either :obj:`InputFile <pyrogram.api.types.InputFile>` or :obj:`InputFileBig <pyrogram.api.types.InputFileBig>`
        file_name: ``str``
        mime_type: ``str``
        thumb (optional): Either :obj:`InputFile <pyrogram.api.types.InputFile>` or :obj:`InputFileBig <pyrogram.api.types.InputFileBig>`

    Returns:
        Either :obj:`DocumentEmpty <pyrogram.api.types.DocumentEmpty>` or :obj:`Document <pyrogram.api.types.Document>`
    """

    __slots__ = ["file", "file_name", "mime_type", "thumb"]

    ID = 0x1c3db333
    QUALNAME = "functions.account.UploadTheme"

    def __init__(self, *, file, file_name: str, mime_type: str, thumb=None):
        self.file = file  # InputFile
        self.thumb = thumb  # flags.0?InputFile
        self.file_name = file_name  # string
        self.mime_type = mime_type  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "UploadTheme":
        flags = Int.read(b)
        
        file = TLObject.read(b)
        
        thumb = TLObject.read(b) if flags & (1 << 0) else None
        
        file_name = String.read(b)
        
        mime_type = String.read(b)
        
        return UploadTheme(file=file, file_name=file_name, mime_type=mime_type, thumb=thumb)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.thumb is not None else 0
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(String(self.file_name))
        
        b.write(String(self.mime_type))
        
        return b.getvalue()
