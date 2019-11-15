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


class UserFull(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xedf17c12``

    Parameters:
        user: Either :obj:`UserEmpty <pyrogram.api.types.UserEmpty>` or :obj:`User <pyrogram.api.types.User>`
        settings: :obj:`PeerSettings <pyrogram.api.types.PeerSettings>`
        notify_settings: :obj:`PeerNotifySettings <pyrogram.api.types.PeerNotifySettings>`
        common_chats_count: ``int`` ``32-bit``
        blocked (optional): ``bool``
        phone_calls_available (optional): ``bool``
        phone_calls_private (optional): ``bool``
        can_pin_message (optional): ``bool``
        has_scheduled (optional): ``bool``
        about (optional): ``str``
        profile_photo (optional): Either :obj:`PhotoEmpty <pyrogram.api.types.PhotoEmpty>` or :obj:`Photo <pyrogram.api.types.Photo>`
        bot_info (optional): :obj:`BotInfo <pyrogram.api.types.BotInfo>`
        pinned_msg_id (optional): ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``

    See Also:
        This object can be returned by :obj:`users.GetFullUser <pyrogram.api.functions.users.GetFullUser>`.
    """

    __slots__ = ["user", "settings", "notify_settings", "common_chats_count", "blocked", "phone_calls_available", "phone_calls_private", "can_pin_message", "has_scheduled", "about", "profile_photo", "bot_info", "pinned_msg_id", "folder_id"]

    ID = 0xedf17c12
    QUALNAME = "types.UserFull"

    def __init__(self, *, user, settings, notify_settings, common_chats_count: int, blocked: bool = None, phone_calls_available: bool = None, phone_calls_private: bool = None, can_pin_message: bool = None, has_scheduled: bool = None, about: str = None, profile_photo=None, bot_info=None, pinned_msg_id: int = None, folder_id: int = None):
        self.blocked = blocked  # flags.0?true
        self.phone_calls_available = phone_calls_available  # flags.4?true
        self.phone_calls_private = phone_calls_private  # flags.5?true
        self.can_pin_message = can_pin_message  # flags.7?true
        self.has_scheduled = has_scheduled  # flags.12?true
        self.user = user  # User
        self.about = about  # flags.1?string
        self.settings = settings  # PeerSettings
        self.profile_photo = profile_photo  # flags.2?Photo
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.bot_info = bot_info  # flags.3?BotInfo
        self.pinned_msg_id = pinned_msg_id  # flags.6?int
        self.common_chats_count = common_chats_count  # int
        self.folder_id = folder_id  # flags.11?int

    @staticmethod
    def read(b: BytesIO, *args) -> "UserFull":
        flags = Int.read(b)
        
        blocked = True if flags & (1 << 0) else False
        phone_calls_available = True if flags & (1 << 4) else False
        phone_calls_private = True if flags & (1 << 5) else False
        can_pin_message = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 12) else False
        user = TLObject.read(b)
        
        about = String.read(b) if flags & (1 << 1) else None
        settings = TLObject.read(b)
        
        profile_photo = TLObject.read(b) if flags & (1 << 2) else None
        
        notify_settings = TLObject.read(b)
        
        bot_info = TLObject.read(b) if flags & (1 << 3) else None
        
        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        common_chats_count = Int.read(b)
        
        folder_id = Int.read(b) if flags & (1 << 11) else None
        return UserFull(user=user, settings=settings, notify_settings=notify_settings, common_chats_count=common_chats_count, blocked=blocked, phone_calls_available=phone_calls_available, phone_calls_private=phone_calls_private, can_pin_message=can_pin_message, has_scheduled=has_scheduled, about=about, profile_photo=profile_photo, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.blocked is not None else 0
        flags |= (1 << 4) if self.phone_calls_available is not None else 0
        flags |= (1 << 5) if self.phone_calls_private is not None else 0
        flags |= (1 << 7) if self.can_pin_message is not None else 0
        flags |= (1 << 12) if self.has_scheduled is not None else 0
        flags |= (1 << 1) if self.about is not None else 0
        flags |= (1 << 2) if self.profile_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.user.write())
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.settings.write())
        
        if self.profile_photo is not None:
            b.write(self.profile_photo.write())
        
        b.write(self.notify_settings.write())
        
        if self.bot_info is not None:
            b.write(self.bot_info.write())
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        b.write(Int(self.common_chats_count))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        return b.getvalue()
