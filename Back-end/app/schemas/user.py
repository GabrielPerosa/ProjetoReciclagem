from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class User(UserCreate):
    id: str

    class Config:
        from_attributes = True
