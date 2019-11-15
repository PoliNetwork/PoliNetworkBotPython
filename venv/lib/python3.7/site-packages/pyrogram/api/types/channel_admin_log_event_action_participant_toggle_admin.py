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


class ChannelAdminLogEventActionParticipantToggleAdmin(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xd5676710``

    Parameters:
        prev_participant: Either :obj:`ChannelParticipant <pyrogram.api.types.ChannelParticipant>`, :obj:`ChannelParticipantSelf <pyrogram.api.types.ChannelParticipantSelf>`, :obj:`ChannelParticipantCreator <pyrogram.api.types.ChannelParticipantCreator>`, :obj:`ChannelParticipantAdmin <pyrogram.api.types.ChannelParticipantAdmin>` or :obj:`ChannelParticipantBanned <pyrogram.api.types.ChannelParticipantBanned>`
        new_participant: Either :obj:`ChannelParticipant <pyrogram.api.types.ChannelParticipant>`, :obj:`ChannelParticipantSelf <pyrogram.api.types.ChannelParticipantSelf>`, :obj:`ChannelParticipantCreator <pyrogram.api.types.ChannelParticipantCreator>`, :obj:`ChannelParticipantAdmin <pyrogram.api.types.ChannelParticipantAdmin>` or :obj:`ChannelParticipantBanned <pyrogram.api.types.ChannelParticipantBanned>`
    """

    __slots__ = ["prev_participant", "new_participant"]

    ID = 0xd5676710
    QUALNAME = "types.ChannelAdminLogEventActionParticipantToggleAdmin"

    def __init__(self, *, prev_participant, new_participant):
        self.prev_participant = prev_participant  # ChannelParticipant
        self.new_participant = new_participant  # ChannelParticipant

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEventActionParticipantToggleAdmin":
        # No flags
        
        prev_participant = TLObject.read(b)
        
        new_participant = TLObject.read(b)
        
        return ChannelAdminLogEventActionParticipantToggleAdmin(prev_participant=prev_participant, new_participant=new_participant)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_participant.write())
        
        b.write(self.new_participant.write())
        
        return b.getvalue()
