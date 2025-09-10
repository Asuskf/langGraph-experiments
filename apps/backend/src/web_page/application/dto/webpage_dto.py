from pydantic import BaseModel


class WebPageDTO(BaseModel):
    id: str
    url: str
    html_content: str