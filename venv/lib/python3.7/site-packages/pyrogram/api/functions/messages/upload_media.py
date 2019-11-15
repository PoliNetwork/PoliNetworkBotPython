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


class UploadMedia(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x519bc2b1``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        media: Either :obj:`InputMediaEmpty <pyrogram.api.types.InputMediaEmpty>`, :obj:`InputMediaUploadedPhoto <pyrogram.api.types.InputMediaUploadedPhoto>`, :obj:`InputMediaPhoto <pyrogram.api.types.InputMediaPhoto>`, :obj:`InputMediaGeoPoint <pyrogram.api.types.InputMediaGeoPoint>`, :obj:`InputMediaContact <pyrogram.api.types.InputMediaContact>`, :obj:`InputMediaUploadedDocument <pyrogram.api.types.InputMediaUploadedDocument>`, :obj:`InputMediaDocument <pyrogram.api.types.InputMediaDocument>`, :obj:`InputMediaVenue <pyrogram.api.types.InputMediaVenue>`, :obj:`InputMediaGifExternal <pyrogram.api.types.InputMediaGifExternal>`, :obj:`InputMediaPhotoExternal <pyrogram.api.types.InputMediaPhotoExternal>`, :obj:`InputMediaDocumentExternal <pyrogram.api.types.InputMediaDocumentExternal>`, :obj:`InputMediaGame <pyrogram.api.types.InputMediaGame>`, :obj:`InputMediaInvoice <pyrogram.api.types.InputMediaInvoice>`, :obj:`InputMediaGeoLive <pyrogram.api.types.InputMediaGeoLive>` or :obj:`InputMediaPoll <pyrogram.api.types.InputMediaPoll>`

    Returns:
        Either :obj:`MessageMediaEmpty <pyrogram.api.types.MessageMediaEmpty>`, :obj:`MessageMediaPhoto <pyrogram.api.types.MessageMediaPhoto>`, :obj:`MessageMediaGeo <pyrogram.api.types.MessageMediaGeo>`, :obj:`MessageMediaContact <pyrogram.api.types.MessageMediaContact>`, :obj:`MessageMediaUnsupported <pyrogram.api.types.MessageMediaUnsupported>`, :obj:`MessageMediaDocument <pyrogram.api.types.MessageMediaDocument>`, :obj:`MessageMediaWebPage <pyrogram.api.types.MessageMediaWebPage>`, :obj:`MessageMediaVenue <pyrogram.api.types.MessageMediaVenue>`, :obj:`MessageMediaGame <pyrogram.api.types.MessageMediaGame>`, :obj:`MessageMediaInvoice <pyrogram.api.types.MessageMediaInvoice>`, :obj:`MessageMediaGeoLive <pyrogram.api.types.MessageMediaGeoLive>` or :obj:`MessageMediaPoll <pyrogram.api.types.MessageMediaPoll>`
    """

    __slots__ = ["peer", "media"]

    ID = 0x519bc2b1
    QUALNAME = "functions.messages.UploadMedia"

    def __init__(self, *, peer, media):
        self.peer = peer  # InputPeer
        self.media = media  # InputMedia

    @staticmethod
    def read(b: BytesIO, *args) -> "UploadMedia":
        # No flags
        
        peer = TLObject.read(b)
        
        media = TLObject.read(b)
        
        return UploadMedia(peer=peer, media=media)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.media.write())
        
        return b.getvalue()
