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


class GetSearchCounters(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x732eef00``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        filters: List of either :obj:`InputMessagesFilterEmpty <pyrogram.api.types.InputMessagesFilterEmpty>`, :obj:`InputMessagesFilterPhotos <pyrogram.api.types.InputMessagesFilterPhotos>`, :obj:`InputMessagesFilterVideo <pyrogram.api.types.InputMessagesFilterVideo>`, :obj:`InputMessagesFilterPhotoVideo <pyrogram.api.types.InputMessagesFilterPhotoVideo>`, :obj:`InputMessagesFilterDocument <pyrogram.api.types.InputMessagesFilterDocument>`, :obj:`InputMessagesFilterUrl <pyrogram.api.types.InputMessagesFilterUrl>`, :obj:`InputMessagesFilterGif <pyrogram.api.types.InputMessagesFilterGif>`, :obj:`InputMessagesFilterVoice <pyrogram.api.types.InputMessagesFilterVoice>`, :obj:`InputMessagesFilterMusic <pyrogram.api.types.InputMessagesFilterMusic>`, :obj:`InputMessagesFilterChatPhotos <pyrogram.api.types.InputMessagesFilterChatPhotos>`, :obj:`InputMessagesFilterPhoneCalls <pyrogram.api.types.InputMessagesFilterPhoneCalls>`, :obj:`InputMessagesFilterRoundVoice <pyrogram.api.types.InputMessagesFilterRoundVoice>`, :obj:`InputMessagesFilterRoundVideo <pyrogram.api.types.InputMessagesFilterRoundVideo>`, :obj:`InputMessagesFilterMyMentions <pyrogram.api.types.InputMessagesFilterMyMentions>`, :obj:`InputMessagesFilterGeo <pyrogram.api.types.InputMessagesFilterGeo>` or :obj:`InputMessagesFilterContacts <pyrogram.api.types.InputMessagesFilterContacts>`

    Returns:
        List of :obj:`messages.SearchCounter <pyrogram.api.types.messages.SearchCounter>`
    """

    __slots__ = ["peer", "filters"]

    ID = 0x732eef00
    QUALNAME = "functions.messages.GetSearchCounters"

    def __init__(self, *, peer, filters: list):
        self.peer = peer  # InputPeer
        self.filters = filters  # Vector<MessagesFilter>

    @staticmethod
    def read(b: BytesIO, *args) -> "GetSearchCounters":
        # No flags
        
        peer = TLObject.read(b)
        
        filters = TLObject.read(b)
        
        return GetSearchCounters(peer=peer, filters=filters)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.filters))
        
        return b.getvalue()
