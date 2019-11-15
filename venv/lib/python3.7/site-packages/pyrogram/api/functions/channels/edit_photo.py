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


class EditPhoto(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xf12e57c9``

    Parameters:
        channel: Either :obj:`InputChannelEmpty <pyrogram.api.types.InputChannelEmpty>`, :obj:`InputChannel <pyrogram.api.types.InputChannel>` or :obj:`InputChannelFromMessage <pyrogram.api.types.InputChannelFromMessage>`
        photo: Either :obj:`InputChatPhotoEmpty <pyrogram.api.types.InputChatPhotoEmpty>`, :obj:`InputChatUploadedPhoto <pyrogram.api.types.InputChatUploadedPhoto>` or :obj:`InputChatPhoto <pyrogram.api.types.InputChatPhoto>`

    Returns:
        Either :obj:`UpdatesTooLong <pyrogram.api.types.UpdatesTooLong>`, :obj:`UpdateShortMessage <pyrogram.api.types.UpdateShortMessage>`, :obj:`UpdateShortChatMessage <pyrogram.api.types.UpdateShortChatMessage>`, :obj:`UpdateShort <pyrogram.api.types.UpdateShort>`, :obj:`UpdatesCombined <pyrogram.api.types.UpdatesCombined>`, :obj:`Update <pyrogram.api.types.Update>` or :obj:`UpdateShortSentMessage <pyrogram.api.types.UpdateShortSentMessage>`
    """

    __slots__ = ["channel", "photo"]

    ID = 0xf12e57c9
    QUALNAME = "functions.channels.EditPhoto"

    def __init__(self, *, channel, photo):
        self.channel = channel  # InputChannel
        self.photo = photo  # InputChatPhoto

    @staticmethod
    def read(b: BytesIO, *args) -> "EditPhoto":
        # No flags
        
        channel = TLObject.read(b)
        
        photo = TLObject.read(b)
        
        return EditPhoto(channel=channel, photo=photo)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.photo.write())
        
        return b.getvalue()
