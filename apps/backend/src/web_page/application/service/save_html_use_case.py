from web_page.domain.entities.files import TxtFiles
from web_page.domain.repositories.path_repository import PathRepository


class SaveHTMLUseCase:
    def __init__(self, repositorie_path: PathRepository):
        self.repositorie_path = repositorie_path
        
    def execute(self, html_content: str) -> None:
        content = TxtFiles(content=html_content)
        self.repositorie_path.save_file(content)