from abc import ABC, abstractmethod
from domain.entities.webpage import WebPage
from typing import List

class WebPageRepository(ABC):

    @abstractmethod
    def save(self, webpage: WebPage) -> None:
        pass

    @abstractmethod
    def get_by_id(self, webpage_id: str) -> WebPage:
        pass

    @abstractmethod
    def list_all(self) -> List[WebPage]:
        pass