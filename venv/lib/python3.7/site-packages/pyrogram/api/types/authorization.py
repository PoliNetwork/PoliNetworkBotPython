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


class Authorization(TLObject):
    """Attributes:
        LAYER: ``105``

    Attributes:
        ID: ``0xad01d61d``

    Parameters:
        hash: ``int`` ``64-bit``
        device_model: ``str``
        platform: ``str``
        system_version: ``str``
        api_id: ``int`` ``32-bit``
        app_name: ``str``
        app_version: ``str``
        date_created: ``int`` ``32-bit``
        date_active: ``int`` ``32-bit``
        ip: ``str``
        country: ``str``
        region: ``str``
        current (optional): ``bool``
        official_app (optional): ``bool``
        password_pending (optional): ``bool``
    """

    __slots__ = ["hash", "device_model", "platform", "system_version", "api_id", "app_name", "app_version", "date_created", "date_active", "ip", "country", "region", "current", "official_app", "password_pending"]

    ID = 0xad01d61d
    QUALNAME = "types.Authorization"

    def __init__(self, *, hash: int, device_model: str, platform: str, system_version: str, api_id: int, app_name: str, app_version: str, date_created: int, date_active: int, ip: str, country: str, region: str, current: bool = None, official_app: bool = None, password_pending: bool = None):
        self.current = current  # flags.0?true
        self.official_app = official_app  # flags.1?true
        self.password_pending = password_pending  # flags.2?true
        self.hash = hash  # long
        self.device_model = device_model  # string
        self.platform = platform  # string
        self.system_version = system_version  # string
        self.api_id = api_id  # int
        self.app_name = app_name  # string
        self.app_version = app_version  # string
        self.date_created = date_created  # int
        self.date_active = date_active  # int
        self.ip = ip  # string
        self.country = country  # string
        self.region = region  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "Authorization":
        flags = Int.read(b)
        
        current = True if flags & (1 << 0) else False
        official_app = True if flags & (1 << 1) else False
        password_pending = True if flags & (1 << 2) else False
        hash = Long.read(b)
        
        device_model = String.read(b)
        
        platform = String.read(b)
        
        system_version = String.read(b)
        
        api_id = Int.read(b)
        
        app_name = String.read(b)
        
        app_version = String.read(b)
        
        date_created = Int.read(b)
        
        date_active = Int.read(b)
        
        ip = String.read(b)
        
        country = String.read(b)
        
        region = String.read(b)
        
        return Authorization(hash=hash, device_model=device_model, platform=platform, system_version=system_version, api_id=api_id, app_name=app_name, app_version=app_version, date_created=date_created, date_active=date_active, ip=ip, country=country, region=region, current=current, official_app=official_app, password_pending=password_pending)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.current is not None else 0
        flags |= (1 << 1) if self.official_app is not None else 0
        flags |= (1 << 2) if self.password_pending is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.hash))
        
        b.write(String(self.device_model))
        
        b.write(String(self.platform))
        
        b.write(String(self.system_version))
        
        b.write(Int(self.api_id))
        
        b.write(String(self.app_name))
        
        b.write(String(self.app_version))
        
        b.write(Int(self.date_created))
        
        b.write(Int(self.date_active))
        
        b.write(String(self.ip))
        
        b.write(String(self.country))
        
        b.write(String(self.region))
        
        return b.getvalue()
