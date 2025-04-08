from pydantic import BaseModel

class TableBase(BaseModel):
    name: str
    seats: int
    location: str | None = None

class TableCreate(TableBase):
    pass

class TableInDB(TableBase):
    id: int

    class Config:
        orm_mode = True
