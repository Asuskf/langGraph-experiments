import os
from pathlib import Path

from web_page.domain.entities.files import TxtFiles
from web_page.domain.repositories.path_repository import PathRepository
from web_page.domain.value_objects.file_name import FileNameTxt
from web_page.domain.value_objects.html_content import HTMLContent
from web_page.domain.value_objects.path import FilePath


class FileTxt(PathRepository):
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
        
    def save_file(self, filename, data):
        final_path = f"{self.base_path}/{filename}"
        
        with open(final_path, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"File '{final_path}' saved successfully.")
        
        return TxtFiles(
            path = FilePath(path=final_path),
            file_name = FileNameTxt(value=filename),
            html_content = HTMLContent(content=data)
        )
    
    
    def get_file_by_file_name(self, filename: str) -> TxtFiles:
        final_path = f"{self.base_path}/{filename}"
        with open(final_path, encoding="utf-8") as f:
            content = f.read()
        return content
    
    
    def drop_file(self, file_name: str) -> bool:
        final_path = f"{self.base_path}/{file_name}"
        if os.path.exists(final_path):
            os.remove(final_path)
            print(f"File '{final_path}' deleted successfully.")
            return True
        else:
            print(f"The file '{final_path}' does not exist.")
            return False
    
        