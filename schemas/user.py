import pydantic


class Users(pydantic.BaseModel):
    id: str
    name: str
    email: str
    password: str
