from pydantic import BaseModel, Field
from web_page.domain.value_objects.html_content import HTMLContent
from web_page.domain.value_objects.url import URL


class WebPage(BaseModel):
    id: str = Field(description="id webpage")
    url: URL
    html_content: HTMLContent
