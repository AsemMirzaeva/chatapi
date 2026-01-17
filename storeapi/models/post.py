from pydantic import BaseModel  # to validate a data


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int
