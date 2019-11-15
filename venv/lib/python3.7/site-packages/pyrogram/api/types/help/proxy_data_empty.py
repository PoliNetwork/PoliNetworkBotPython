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


class ProxyDataEmpty(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xe09e1fb8``

    Parameters:
        expires: ``int`` ``32-bit``

    See Also:
        This object can be returned by :obj:`help.GetProxyData <pyrogram.api.functions.help.GetProxyData>`.
    """

    __slots__ = ["expires"]

    ID = 0xe09e1fb8
    QUALNAME = "types.help.ProxyDataEmpty"

    def __init__(self, *, expires: int):
        self.expires = expires  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "ProxyDataEmpty":
        # No flags
        
        expires = Int.read(b)
        
        return ProxyDataEmpty(expires=expires)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        return b.getvalue()
