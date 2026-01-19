from pydantic import BaseModel  # to validate a data


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    id: int

class CommentIn(BaseModel):
    body: str
    post_id: int

class Comment(CommentIn):
    id: int 

class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]