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


class CreateChannel(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x3d5fb10f``

    Parameters:
        title: ``str``
        about: ``str``
        broadcast (optional): ``bool``
        megagroup (optional): ``bool``
        geo_point (optional): Either :obj:`InputGeoPointEmpty <pyrogram.api.types.InputGeoPointEmpty>` or :obj:`InputGeoPoint <pyrogram.api.types.InputGeoPoint>`
        address (optional): ``str``

    Returns:
        Either :obj:`UpdatesTooLong <pyrogram.api.types.UpdatesTooLong>`, :obj:`UpdateShortMessage <pyrogram.api.types.UpdateShortMessage>`, :obj:`UpdateShortChatMessage <pyrogram.api.types.UpdateShortChatMessage>`, :obj:`UpdateShort <pyrogram.api.types.UpdateShort>`, :obj:`UpdatesCombined <pyrogram.api.types.UpdatesCombined>`, :obj:`Update <pyrogram.api.types.Update>` or :obj:`UpdateShortSentMessage <pyrogram.api.types.UpdateShortSentMessage>`
    """

    __slots__ = ["title", "about", "broadcast", "megagroup", "geo_point", "address"]

    ID = 0x3d5fb10f
    QUALNAME = "functions.channels.CreateChannel"

    def __init__(self, *, title: str, about: str, broadcast: bool = None, megagroup: bool = None, geo_point=None, address: str = None):
        self.broadcast = broadcast  # flags.0?true
        self.megagroup = megagroup  # flags.1?true
        self.title = title  # string
        self.about = about  # string
        self.geo_point = geo_point  # flags.2?InputGeoPoint
        self.address = address  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args) -> "CreateChannel":
        flags = Int.read(b)
        
        broadcast = True if flags & (1 << 0) else False
        megagroup = True if flags & (1 << 1) else False
        title = String.read(b)
        
        about = String.read(b)
        
        geo_point = TLObject.read(b) if flags & (1 << 2) else None
        
        address = String.read(b) if flags & (1 << 2) else None
        return CreateChannel(title=title, about=about, broadcast=broadcast, megagroup=megagroup, geo_point=geo_point, address=address)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.broadcast is not None else 0
        flags |= (1 << 1) if self.megagroup is not None else 0
        flags |= (1 << 2) if self.geo_point is not None else 0
        flags |= (1 << 2) if self.address is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        b.write(String(self.about))
        
        if self.geo_point is not None:
            b.write(self.geo_point.write())
        
        if self.address is not None:
            b.write(String(self.address))
        
        return b.getvalue()
