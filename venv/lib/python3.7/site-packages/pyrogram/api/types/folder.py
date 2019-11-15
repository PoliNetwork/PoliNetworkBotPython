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


class Folder(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xff544e65``

    Parameters:
        id: ``int`` ``32-bit``
        title: ``str``
        autofill_new_broadcasts (optional): ``bool``
        autofill_public_groups (optional): ``bool``
        autofill_new_correspondents (optional): ``bool``
        photo (optional): Either :obj:`ChatPhotoEmpty <pyrogram.api.types.ChatPhotoEmpty>` or :obj:`ChatPhoto <pyrogram.api.types.ChatPhoto>`
    """

    __slots__ = ["id", "title", "autofill_new_broadcasts", "autofill_public_groups", "autofill_new_correspondents", "photo"]

    ID = 0xff544e65
    QUALNAME = "types.Folder"

    def __init__(self, *, id: int, title: str, autofill_new_broadcasts: bool = None, autofill_public_groups: bool = None, autofill_new_correspondents: bool = None, photo=None):
        self.autofill_new_broadcasts = autofill_new_broadcasts  # flags.0?true
        self.autofill_public_groups = autofill_public_groups  # flags.1?true
        self.autofill_new_correspondents = autofill_new_correspondents  # flags.2?true
        self.id = id  # int
        self.title = title  # string
        self.photo = photo  # flags.3?ChatPhoto

    @staticmethod
    def read(b: BytesIO, *args) -> "Folder":
        flags = Int.read(b)
        
        autofill_new_broadcasts = True if flags & (1 << 0) else False
        autofill_public_groups = True if flags & (1 << 1) else False
        autofill_new_correspondents = True if flags & (1 << 2) else False
        id = Int.read(b)
        
        title = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 3) else None
        
        return Folder(id=id, title=title, autofill_new_broadcasts=autofill_new_broadcasts, autofill_public_groups=autofill_public_groups, autofill_new_correspondents=autofill_new_correspondents, photo=photo)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.autofill_new_broadcasts is not None else 0
        flags |= (1 << 1) if self.autofill_public_groups is not None else 0
        flags |= (1 << 2) if self.autofill_new_correspondents is not None else 0
        flags |= (1 << 3) if self.photo is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.title))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        return b.getvalue()
