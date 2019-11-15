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


class ResetTopPeerRating(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1ae373ac``

    Parameters:
        category: Either :obj:`TopPeerCategoryBotsPM <pyrogram.api.types.TopPeerCategoryBotsPM>`, :obj:`TopPeerCategoryBotsInline <pyrogram.api.types.TopPeerCategoryBotsInline>`, :obj:`TopPeerCategoryCorrespondents <pyrogram.api.types.TopPeerCategoryCorrespondents>`, :obj:`TopPeerCategoryGroups <pyrogram.api.types.TopPeerCategoryGroups>`, :obj:`TopPeerCategoryChannels <pyrogram.api.types.TopPeerCategoryChannels>`, :obj:`TopPeerCategoryPhoneCalls <pyrogram.api.types.TopPeerCategoryPhoneCalls>`, :obj:`TopPeerCategoryForwardUsers <pyrogram.api.types.TopPeerCategoryForwardUsers>` or :obj:`TopPeerCategoryForwardChats <pyrogram.api.types.TopPeerCategoryForwardChats>`
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`

    Returns:
        ``bool``
    """

    __slots__ = ["category", "peer"]

    ID = 0x1ae373ac
    QUALNAME = "functions.contacts.ResetTopPeerRating"

    def __init__(self, *, category, peer):
        self.category = category  # TopPeerCategory
        self.peer = peer  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args) -> "ResetTopPeerRating":
        # No flags
        
        category = TLObject.read(b)
        
        peer = TLObject.read(b)
        
        return ResetTopPeerRating(category=category, peer=peer)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.category.write())
        
        b.write(self.peer.write())
        
        return b.getvalue()
