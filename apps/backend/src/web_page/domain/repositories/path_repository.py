from abc import ABC, abstractmethod

from web_page.domain.entities.files import TxtFiles


class PathRepository(ABC):
    @abstractmethod
    def save_file(self, txt_file: TxtFiles) -> None:
        pass
    
    @abstractmethod
    def get_file_by_path(self, file_path: str) -> TxtFiles:
        pass
    
    @abstractmethod
    def drop_file(self, file_path: str) -> bool:
        pass