from pydantic import BaseModel


class ContentDTO(BaseModel):
    content: str