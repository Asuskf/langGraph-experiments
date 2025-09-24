from pydantic import BaseModel, Field
from web_page.domain.value_objects.file_name import FileNameTxt
from web_page.domain.value_objects.html_content import HTMLContent
from web_page.domain.value_objects.path import FilePath


class TxtFiles(BaseModel):
    path : FilePath = Field(..., description="File path (must exist and be a file)")
    file_name : FileNameTxt = Field(..., description="File name")
    html_content : HTMLContent = Field(..., description="Content")
    