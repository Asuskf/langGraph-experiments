from web_page.application.mapper.file_mapper import to_dto_path_file
from web_page.application.ports.file_port import FilePort
from web_page.infrastructure.persistence.file_txt_repo import FileTxt


class FileTxtAdapter(FilePort):
    def __init__(self, base_path: str = "./data"):
        self.new_file = FileTxt(base_path)
    
    def save_file_txt(self, name_file: str, content: str):
        txt_file = self.new_file.save_file(name_file, content)
        return to_dto_path_file(txt_file)

