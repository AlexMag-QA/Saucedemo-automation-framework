from pydantic import BaseModel


class PostModel(BaseModel):
    id: int
    title: str
    body: str
    userId: int
