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


class ChannelAdminLogEvent(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x3b5a3e40``

    Parameters:
        id: ``int`` ``64-bit``
        date: ``int`` ``32-bit``
        user_id: ``int`` ``32-bit``
        action: Either :obj:`ChannelAdminLogEventActionChangeTitle <pyrogram.api.types.ChannelAdminLogEventActionChangeTitle>`, :obj:`ChannelAdminLogEventActionChangeAbout <pyrogram.api.types.ChannelAdminLogEventActionChangeAbout>`, :obj:`ChannelAdminLogEventActionChangeUsername <pyrogram.api.types.ChannelAdminLogEventActionChangeUsername>`, :obj:`ChannelAdminLogEventActionChangePhoto <pyrogram.api.types.ChannelAdminLogEventActionChangePhoto>`, :obj:`ChannelAdminLogEventActionToggleInvites <pyrogram.api.types.ChannelAdminLogEventActionToggleInvites>`, :obj:`ChannelAdminLogEventActionToggleSignatures <pyrogram.api.types.ChannelAdminLogEventActionToggleSignatures>`, :obj:`ChannelAdminLogEventActionUpdatePinned <pyrogram.api.types.ChannelAdminLogEventActionUpdatePinned>`, :obj:`ChannelAdminLogEventActionEditMessage <pyrogram.api.types.ChannelAdminLogEventActionEditMessage>`, :obj:`ChannelAdminLogEventActionDeleteMessage <pyrogram.api.types.ChannelAdminLogEventActionDeleteMessage>`, :obj:`ChannelAdminLogEventActionParticipantJoin <pyrogram.api.types.ChannelAdminLogEventActionParticipantJoin>`, :obj:`ChannelAdminLogEventActionParticipantLeave <pyrogram.api.types.ChannelAdminLogEventActionParticipantLeave>`, :obj:`ChannelAdminLogEventActionParticipantInvite <pyrogram.api.types.ChannelAdminLogEventActionParticipantInvite>`, :obj:`ChannelAdminLogEventActionParticipantToggleBan <pyrogram.api.types.ChannelAdminLogEventActionParticipantToggleBan>`, :obj:`ChannelAdminLogEventActionParticipantToggleAdmin <pyrogram.api.types.ChannelAdminLogEventActionParticipantToggleAdmin>`, :obj:`ChannelAdminLogEventActionChangeStickerSet <pyrogram.api.types.ChannelAdminLogEventActionChangeStickerSet>`, :obj:`ChannelAdminLogEventActionTogglePreHistoryHidden <pyrogram.api.types.ChannelAdminLogEventActionTogglePreHistoryHidden>`, :obj:`ChannelAdminLogEventActionDefaultBannedRights <pyrogram.api.types.ChannelAdminLogEventActionDefaultBannedRights>`, :obj:`ChannelAdminLogEventActionStopPoll <pyrogram.api.types.ChannelAdminLogEventActionStopPoll>`, :obj:`ChannelAdminLogEventActionChangeLinkedChat <pyrogram.api.types.ChannelAdminLogEventActionChangeLinkedChat>`, :obj:`ChannelAdminLogEventActionChangeLocation <pyrogram.api.types.ChannelAdminLogEventActionChangeLocation>` or :obj:`ChannelAdminLogEventActionToggleSlowMode <pyrogram.api.types.ChannelAdminLogEventActionToggleSlowMode>`
    """

    __slots__ = ["id", "date", "user_id", "action"]

    ID = 0x3b5a3e40
    QUALNAME = "types.ChannelAdminLogEvent"

    def __init__(self, *, id: int, date: int, user_id: int, action):
        self.id = id  # long
        self.date = date  # int
        self.user_id = user_id  # int
        self.action = action  # ChannelAdminLogEventAction

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEvent":
        # No flags
        
        id = Long.read(b)
        
        date = Int.read(b)
        
        user_id = Int.read(b)
        
        action = TLObject.read(b)
        
        return ChannelAdminLogEvent(id=id, date=date, user_id=user_id, action=action)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.user_id))
        
        b.write(self.action.write())
        
        return b.getvalue()
