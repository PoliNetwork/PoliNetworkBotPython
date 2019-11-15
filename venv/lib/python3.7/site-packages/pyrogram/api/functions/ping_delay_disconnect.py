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


class PingDelayDisconnect(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf3427b8c``

    Parameters:
        ping_id: ``int`` ``64-bit``
        disconnect_delay: ``int`` ``32-bit``

    Returns:
        :obj:`Pong <pyrogram.api.types.Pong>`
    """

    __slots__ = ["ping_id", "disconnect_delay"]

    ID = 0xf3427b8c
    QUALNAME = "functions.PingDelayDisconnect"

    def __init__(self, *, ping_id: int, disconnect_delay: int):
        self.ping_id = ping_id  # long
        self.disconnect_delay = disconnect_delay  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "PingDelayDisconnect":
        # No flags
        
        ping_id = Long.read(b)
        
        disconnect_delay = Int.read(b)
        
        return PingDelayDisconnect(ping_id=ping_id, disconnect_delay=disconnect_delay)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.ping_id))
        
        b.write(Int(self.disconnect_delay))
        
        return b.getvalue()
