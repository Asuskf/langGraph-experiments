from abc import ABC, abstractmethod

from web_page.application.dto.path_dtop import PathDTO


class FilePort(ABC):
    @abstractmethod
    def save_file_txt(self, path) -> PathDTO:
        pass