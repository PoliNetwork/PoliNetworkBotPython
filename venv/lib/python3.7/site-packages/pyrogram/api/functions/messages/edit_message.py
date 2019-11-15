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


class EditMessage(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x48f71778``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        id: ``int`` ``32-bit``
        no_webpage (optional): ``bool``
        message (optional): ``str``
        media (optional): Either :obj:`InputMediaEmpty <pyrogram.api.types.InputMediaEmpty>`, :obj:`InputMediaUploadedPhoto <pyrogram.api.types.InputMediaUploadedPhoto>`, :obj:`InputMediaPhoto <pyrogram.api.types.InputMediaPhoto>`, :obj:`InputMediaGeoPoint <pyrogram.api.types.InputMediaGeoPoint>`, :obj:`InputMediaContact <pyrogram.api.types.InputMediaContact>`, :obj:`InputMediaUploadedDocument <pyrogram.api.types.InputMediaUploadedDocument>`, :obj:`InputMediaDocument <pyrogram.api.types.InputMediaDocument>`, :obj:`InputMediaVenue <pyrogram.api.types.InputMediaVenue>`, :obj:`InputMediaGifExternal <pyrogram.api.types.InputMediaGifExternal>`, :obj:`InputMediaPhotoExternal <pyrogram.api.types.InputMediaPhotoExternal>`, :obj:`InputMediaDocumentExternal <pyrogram.api.types.InputMediaDocumentExternal>`, :obj:`InputMediaGame <pyrogram.api.types.InputMediaGame>`, :obj:`InputMediaInvoice <pyrogram.api.types.InputMediaInvoice>`, :obj:`InputMediaGeoLive <pyrogram.api.types.InputMediaGeoLive>` or :obj:`InputMediaPoll <pyrogram.api.types.InputMediaPoll>`
        reply_markup (optional): Either :obj:`ReplyKeyboardHide <pyrogram.api.types.ReplyKeyboardHide>`, :obj:`ReplyKeyboardForceReply <pyrogram.api.types.ReplyKeyboardForceReply>`, :obj:`ReplyKeyboardMarkup <pyrogram.api.types.ReplyKeyboardMarkup>` or :obj:`ReplyInlineMarkup <pyrogram.api.types.ReplyInlineMarkup>`
        entities (optional): List of either :obj:`MessageEntityUnknown <pyrogram.api.types.MessageEntityUnknown>`, :obj:`MessageEntityMention <pyrogram.api.types.MessageEntityMention>`, :obj:`MessageEntityHashtag <pyrogram.api.types.MessageEntityHashtag>`, :obj:`MessageEntityBotCommand <pyrogram.api.types.MessageEntityBotCommand>`, :obj:`MessageEntityUrl <pyrogram.api.types.MessageEntityUrl>`, :obj:`MessageEntityEmail <pyrogram.api.types.MessageEntityEmail>`, :obj:`MessageEntityBold <pyrogram.api.types.MessageEntityBold>`, :obj:`MessageEntityItalic <pyrogram.api.types.MessageEntityItalic>`, :obj:`MessageEntityCode <pyrogram.api.types.MessageEntityCode>`, :obj:`MessageEntityPre <pyrogram.api.types.MessageEntityPre>`, :obj:`MessageEntityTextUrl <pyrogram.api.types.MessageEntityTextUrl>`, :obj:`MessageEntityMentionName <pyrogram.api.types.MessageEntityMentionName>`, :obj:`InputMessageEntityMentionName <pyrogram.api.types.InputMessageEntityMentionName>`, :obj:`MessageEntityPhone <pyrogram.api.types.MessageEntityPhone>`, :obj:`MessageEntityCashtag <pyrogram.api.types.MessageEntityCashtag>`, :obj:`MessageEntityUnderline <pyrogram.api.types.MessageEntityUnderline>`, :obj:`MessageEntityStrike <pyrogram.api.types.MessageEntityStrike>` or :obj:`MessageEntityBlockquote <pyrogram.api.types.MessageEntityBlockquote>`
        schedule_date (optional): ``int`` ``32-bit``

    Returns:
        Either :obj:`UpdatesTooLong <pyrogram.api.types.UpdatesTooLong>`, :obj:`UpdateShortMessage <pyrogram.api.types.UpdateShortMessage>`, :obj:`UpdateShortChatMessage <pyrogram.api.types.UpdateShortChatMessage>`, :obj:`UpdateShort <pyrogram.api.types.UpdateShort>`, :obj:`UpdatesCombined <pyrogram.api.types.UpdatesCombined>`, :obj:`Update <pyrogram.api.types.Update>` or :obj:`UpdateShortSentMessage <pyrogram.api.types.UpdateShortSentMessage>`
    """

    __slots__ = ["peer", "id", "no_webpage", "message", "media", "reply_markup", "entities", "schedule_date"]

    ID = 0x48f71778
    QUALNAME = "functions.messages.EditMessage"

    def __init__(self, *, peer, id: int, no_webpage: bool = None, message: str = None, media=None, reply_markup=None, entities: list = None, schedule_date: int = None):
        self.no_webpage = no_webpage  # flags.1?true
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.message = message  # flags.11?string
        self.media = media  # flags.14?InputMedia
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup
        self.entities = entities  # flags.3?Vector<MessageEntity>
        self.schedule_date = schedule_date  # flags.15?int

    @staticmethod
    def read(b: BytesIO, *args) -> "EditMessage":
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        message = String.read(b) if flags & (1 << 11) else None
        media = TLObject.read(b) if flags & (1 << 14) else None
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        entities = TLObject.read(b) if flags & (1 << 3) else []
        
        schedule_date = Int.read(b) if flags & (1 << 15) else None
        return EditMessage(peer=peer, id=id, no_webpage=no_webpage, message=message, media=media, reply_markup=reply_markup, entities=entities, schedule_date=schedule_date)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage is not None else 0
        flags |= (1 << 11) if self.message is not None else 0
        flags |= (1 << 14) if self.media is not None else 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        flags |= (1 << 3) if self.entities is not None else 0
        flags |= (1 << 15) if self.schedule_date is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        if self.message is not None:
            b.write(String(self.message))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        return b.getvalue()
