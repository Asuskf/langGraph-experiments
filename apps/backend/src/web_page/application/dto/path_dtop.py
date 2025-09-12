from pydantic import BaseModel
from web_page.domain.value_objects.file_name import FileNameTxt
from web_page.domain.value_objects.html_content import HTMLContent
from web_page.domain.value_objects.path import FilePath

class PathDTO(BaseModel):
    path: str
    file_name: str
    html_content: str