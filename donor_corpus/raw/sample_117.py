from enum import Enum
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models import User, Organization


class DataRoomBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class DataRoomCreateRequest(DataRoomBase):
    name: str


class DataRoomCreate(DataRoomCreateRequest):
    creator: User
    organization: Organization

    class Config:
        arbitrary_types_allowed = True


class DataRoomRole(str, Enum):
    OWNER = "OWNER"
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"


class DataRoomUserRoleRequest(BaseModel):
    user_id: UUID
    user_role: DataRoomRole

    class Config:
        use_enum_values = True


class DataRoomTeamRoleRequest(BaseModel):
    team_id: UUID
    team_role: DataRoomRole

    class Config:
        use_enum_values = True


class DataRoomUpdate(DataRoomBase):
    pass


class DataRoomInDBBase(DataRoomBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True
