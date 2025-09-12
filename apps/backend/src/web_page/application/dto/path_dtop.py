from pydantic import BaseModel


class PathDTO(BaseModel):
    path: str
    file_name: str
    html_content: str