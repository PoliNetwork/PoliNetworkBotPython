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


class SetStickers(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xea8ca4f9``

    Parameters:
        channel: Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`
        stickerset: Either :obj:`InputStickerSetEmpty <pyrogram.api.types.InputStickerSetEmpty>`, :obj:`InputStickerSetID <pyrogram.api.types.InputStickerSetID>`, :obj:`InputStickerSetShortName <pyrogram.api.types.InputStickerSetShortName>` or :obj:`InputStickerSetAnimatedEmoji <pyrogram.api.types.InputStickerSetAnimatedEmoji>`

    Returns:
        ``bool``
    """

    __slots__ = ["channel", "stickerset"]

    ID = 0xea8ca4f9
    QUALNAME = "functions.channels.SetStickers"

    def __init__(self, *, channel, stickerset):
        self.channel = channel  # InputChannel
        self.stickerset = stickerset  # InputStickerSet

    @staticmethod
    def read(b: BytesIO, *args) -> "SetStickers":
        # No flags
        
        channel = TLObject.read(b)
        
        stickerset = TLObject.read(b)
        
        return SetStickers(channel=channel, stickerset=stickerset)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.stickerset.write())
        
        return b.getvalue()
