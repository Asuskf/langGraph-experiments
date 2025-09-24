from abc import ABC, abstractmethod

from web_page.domain.entities.files import TxtFiles


class PathRepository(ABC):
    @abstractmethod
    def save_file(self, txt_file: TxtFiles) -> TxtFiles:
        pass
    
    @abstractmethod
    def get_file_by_file_name(self, file_name: str) -> str:
        pass
    
    @abstractmethod
    def drop_file(self, file_name: str) -> bool:
        pass