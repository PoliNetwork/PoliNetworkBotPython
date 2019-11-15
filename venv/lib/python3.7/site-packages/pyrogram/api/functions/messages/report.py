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


class Report(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xbd82b658``

    Parameters:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>`, :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`, :obj:`InputPeerUserFromMessage <pyrogram.api.types.InputPeerUserFromMessage>` or :obj:`InputPeerChannelFromMessage <pyrogram.api.types.InputPeerChannelFromMessage>`
        id: List of ``int`` ``32-bit``
        reason: Either :obj:`InputReportReasonSpam <pyrogram.api.types.InputReportReasonSpam>`, :obj:`InputReportReasonViolence <pyrogram.api.types.InputReportReasonViolence>`, :obj:`InputReportReasonPornography <pyrogram.api.types.InputReportReasonPornography>`, :obj:`InputReportReasonChildAbuse <pyrogram.api.types.InputReportReasonChildAbuse>`, :obj:`InputReportReasonOther <pyrogram.api.types.InputReportReasonOther>`, :obj:`InputReportReasonCopyright <pyrogram.api.types.InputReportReasonCopyright>` or :obj:`InputReportReasonGeoIrrelevant <pyrogram.api.types.InputReportReasonGeoIrrelevant>`

    Returns:
        ``bool``
    """

    __slots__ = ["peer", "id", "reason"]

    ID = 0xbd82b658
    QUALNAME = "functions.messages.Report"

    def __init__(self, *, peer, id: list, reason):
        self.peer = peer  # InputPeer
        self.id = id  # Vector<int>
        self.reason = reason  # ReportReason

    @staticmethod
    def read(b: BytesIO, *args) -> "Report":
        # No flags
        
        peer = TLObject.read(b)
        
        id = TLObject.read(b, Int)
        
        reason = TLObject.read(b)
        
        return Report(peer=peer, id=id, reason=reason)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Vector(self.id, Int))
        
        b.write(self.reason.write())
        
        return b.getvalue()
