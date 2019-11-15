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


class PeerSettings(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0x818426cd``

    Parameters:
        report_spam (optional): ``bool``
        add_contact (optional): ``bool``
        block_contact (optional): ``bool``
        share_contact (optional): ``bool``
        need_contacts_exception (optional): ``bool``
        report_geo (optional): ``bool``

    See Also:
        This object can be returned by :obj:`messages.GetPeerSettings <pyrogram.api.functions.messages.GetPeerSettings>`.
    """

    __slots__ = ["report_spam", "add_contact", "block_contact", "share_contact", "need_contacts_exception", "report_geo"]

    ID = 0x818426cd
    QUALNAME = "types.PeerSettings"

    def __init__(self, *, report_spam: bool = None, add_contact: bool = None, block_contact: bool = None, share_contact: bool = None, need_contacts_exception: bool = None, report_geo: bool = None):
        self.report_spam = report_spam  # flags.0?true
        self.add_contact = add_contact  # flags.1?true
        self.block_contact = block_contact  # flags.2?true
        self.share_contact = share_contact  # flags.3?true
        self.need_contacts_exception = need_contacts_exception  # flags.4?true
        self.report_geo = report_geo  # flags.5?true

    @staticmethod
    def read(b: BytesIO, *args) -> "PeerSettings":
        flags = Int.read(b)
        
        report_spam = True if flags & (1 << 0) else False
        add_contact = True if flags & (1 << 1) else False
        block_contact = True if flags & (1 << 2) else False
        share_contact = True if flags & (1 << 3) else False
        need_contacts_exception = True if flags & (1 << 4) else False
        report_geo = True if flags & (1 << 5) else False
        return PeerSettings(report_spam=report_spam, add_contact=add_contact, block_contact=block_contact, share_contact=share_contact, need_contacts_exception=need_contacts_exception, report_geo=report_geo)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.report_spam is not None else 0
        flags |= (1 << 1) if self.add_contact is not None else 0
        flags |= (1 << 2) if self.block_contact is not None else 0
        flags |= (1 << 3) if self.share_contact is not None else 0
        flags |= (1 << 4) if self.need_contacts_exception is not None else 0
        flags |= (1 << 5) if self.report_geo is not None else 0
        b.write(Int(flags))
        
        return b.getvalue()
