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


class BotInlineMessageMediaVenue(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x8a86659c``

    Parameters:
        geo: Either :obj:`GeoPointEmpty <pyrogram.api.types.GeoPointEmpty>` or :obj:`GeoPoint <pyrogram.api.types.GeoPoint>`
        title: ``str``
        address: ``str``
        provider: ``str``
        venue_id: ``str``
        venue_type: ``str``
        reply_markup (optional): Either :obj:`ReplyKeyboardHide <pyrogram.api.types.ReplyKeyboardHide>`, :obj:`ReplyKeyboardForceReply <pyrogram.api.types.ReplyKeyboardForceReply>`, :obj:`ReplyKeyboardMarkup <pyrogram.api.types.ReplyKeyboardMarkup>` or :obj:`ReplyInlineMarkup <pyrogram.api.types.ReplyInlineMarkup>`
    """

    __slots__ = ["geo", "title", "address", "provider", "venue_id", "venue_type", "reply_markup"]

    ID = 0x8a86659c
    QUALNAME = "types.BotInlineMessageMediaVenue"

    def __init__(self, *, geo, title: str, address: str, provider: str, venue_id: str, venue_type: str, reply_markup=None):
        self.geo = geo  # GeoPoint
        self.title = title  # string
        self.address = address  # string
        self.provider = provider  # string
        self.venue_id = venue_id  # string
        self.venue_type = venue_type  # string
        self.reply_markup = reply_markup  # flags.2?ReplyMarkup

    @staticmethod
    def read(b: BytesIO, *args) -> "BotInlineMessageMediaVenue":
        flags = Int.read(b)
        
        geo = TLObject.read(b)
        
        title = String.read(b)
        
        address = String.read(b)
        
        provider = String.read(b)
        
        venue_id = String.read(b)
        
        venue_type = String.read(b)
        
        reply_markup = TLObject.read(b) if flags & (1 << 2) else None
        
        return BotInlineMessageMediaVenue(geo=geo, title=title, address=address, provider=provider, venue_id=venue_id, venue_type=venue_type, reply_markup=reply_markup)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.reply_markup is not None else 0
        b.write(Int(flags))
        
        b.write(self.geo.write())
        
        b.write(String(self.title))
        
        b.write(String(self.address))
        
        b.write(String(self.provider))
        
        b.write(String(self.venue_id))
        
        b.write(String(self.venue_type))
        
        if self.reply_markup is not None:
            b.write(self.reply_markup.write())
        
        return b.getvalue()
