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


class InputMediaGeoLive(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xce4e82fd``

    Parameters:
        geo_point: Either :obj:`InputGeoPointEmpty <pyrogram.api.types.InputGeoPointEmpty>` or :obj:`InputGeoPoint <pyrogram.api.types.InputGeoPoint>`
        stopped (optional): ``bool``
        period (optional): ``int`` ``32-bit``
    """

    __slots__ = ["geo_point", "stopped", "period"]

    ID = 0xce4e82fd
    QUALNAME = "types.InputMediaGeoLive"

    def __init__(self, *, geo_point, stopped: bool = None, period: int = None):
        self.stopped = stopped  # flags.0?true
        self.geo_point = geo_point  # InputGeoPoint
        self.period = period  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args) -> "InputMediaGeoLive":
        flags = Int.read(b)
        
        stopped = True if flags & (1 << 0) else False
        geo_point = TLObject.read(b)
        
        period = Int.read(b) if flags & (1 << 1) else None
        return InputMediaGeoLive(geo_point=geo_point, stopped=stopped, period=period)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.stopped is not None else 0
        flags |= (1 << 1) if self.period is not None else 0
        b.write(Int(flags))
        
        b.write(self.geo_point.write())
        
        if self.period is not None:
            b.write(Int(self.period))
        
        return b.getvalue()
