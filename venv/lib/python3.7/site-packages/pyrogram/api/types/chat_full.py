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


class ChatFull(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x1b7c9db3``

    Parameters:
        id: ``int`` ``32-bit``
        about: ``str``
        participants: Either :obj:`ChatParticipantsForbidden <pyrogram.api.types.ChatParticipantsForbidden>` or :obj:`ChatParticipants <pyrogram.api.types.ChatParticipants>`
        notify_settings: :obj:`PeerNotifySettings <pyrogram.api.types.PeerNotifySettings>`
        exported_invite: Either :obj:`ChatInviteEmpty <pyrogram.api.types.ChatInviteEmpty>` or :obj:`ChatInviteExported <pyrogram.api.types.ChatInviteExported>`
        can_set_username (optional): ``bool``
        has_scheduled (optional): ``bool``
        chat_photo (optional): Either :obj:`PhotoEmpty <pyrogram.api.types.PhotoEmpty>` or :obj:`Photo <pyrogram.api.types.Photo>`
        bot_info (optional): List of :obj:`BotInfo <pyrogram.api.types.BotInfo>`
        pinned_msg_id (optional): ``int`` ``32-bit``
        folder_id (optional): ``int`` ``32-bit``
    """

    __slots__ = ["id", "about", "participants", "notify_settings", "exported_invite", "can_set_username", "has_scheduled", "chat_photo", "bot_info", "pinned_msg_id", "folder_id"]

    ID = 0x1b7c9db3
    QUALNAME = "types.ChatFull"

    def __init__(self, *, id: int, about: str, participants, notify_settings, exported_invite, can_set_username: bool = None, has_scheduled: bool = None, chat_photo=None, bot_info: list = None, pinned_msg_id: int = None, folder_id: int = None):
        self.can_set_username = can_set_username  # flags.7?true
        self.has_scheduled = has_scheduled  # flags.8?true
        self.id = id  # int
        self.about = about  # string
        self.participants = participants  # ChatParticipants
        self.chat_photo = chat_photo  # flags.2?Photo
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.exported_invite = exported_invite  # ExportedChatInvite
        self.bot_info = bot_info  # flags.3?Vector<BotInfo>
        self.pinned_msg_id = pinned_msg_id  # flags.6?int
        self.folder_id = folder_id  # flags.11?int

    @staticmethod
    def read(b: BytesIO, *args) -> "ChatFull":
        flags = Int.read(b)
        
        can_set_username = True if flags & (1 << 7) else False
        has_scheduled = True if flags & (1 << 8) else False
        id = Int.read(b)
        
        about = String.read(b)
        
        participants = TLObject.read(b)
        
        chat_photo = TLObject.read(b) if flags & (1 << 2) else None
        
        notify_settings = TLObject.read(b)
        
        exported_invite = TLObject.read(b)
        
        bot_info = TLObject.read(b) if flags & (1 << 3) else []
        
        pinned_msg_id = Int.read(b) if flags & (1 << 6) else None
        folder_id = Int.read(b) if flags & (1 << 11) else None
        return ChatFull(id=id, about=about, participants=participants, notify_settings=notify_settings, exported_invite=exported_invite, can_set_username=can_set_username, has_scheduled=has_scheduled, chat_photo=chat_photo, bot_info=bot_info, pinned_msg_id=pinned_msg_id, folder_id=folder_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 7) if self.can_set_username is not None else 0
        flags |= (1 << 8) if self.has_scheduled is not None else 0
        flags |= (1 << 2) if self.chat_photo is not None else 0
        flags |= (1 << 3) if self.bot_info is not None else 0
        flags |= (1 << 6) if self.pinned_msg_id is not None else 0
        flags |= (1 << 11) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.about))
        
        b.write(self.participants.write())
        
        if self.chat_photo is not None:
            b.write(self.chat_photo.write())
        
        b.write(self.notify_settings.write())
        
        b.write(self.exported_invite.write())
        
        if self.bot_info is not None:
            b.write(Vector(self.bot_info))
        
        if self.pinned_msg_id is not None:
            b.write(Int(self.pinned_msg_id))
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        return b.getvalue()
