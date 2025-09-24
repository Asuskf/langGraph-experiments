from web_page.application.dto.path_dtop import PathDTO
from web_page.domain.entities.files import TxtFiles
from web_page.domain.entities.webpage import HTMLContent
from web_page.domain.value_objects.file_name import FileNameTxt
from web_page.domain.value_objects.path import FilePath


def to_dto_path_file(txt_file: TxtFiles) -> PathDTO:
    return PathDTO(
        path = str(txt_file.path.path),
        file_name = txt_file.file_name.value,
        html_content = txt_file.html_content.content 
    )
    
def from_dto_path_file(dto: PathDTO) -> TxtFiles:
    return TxtFiles(
        path = FilePath(dto.path), 
        file_name = FileNameTxt(dto.file_name),
        html_content = HTMLContent(dto.html_content )
    )
