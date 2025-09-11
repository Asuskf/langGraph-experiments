from abc import ABC, abstractmethod

from web_page.domain.entities.webpage import WebPage


class WebPageRepository(ABC):
    
    @abstractmethod
    def save_webpage(self, webpage: WebPage, filename: str) -> None:
        pass
    
    @abstractmethod
    def get_webpage_by_id(self, webpage_id: str) -> WebPage:
        pass
    
    @abstractmethod
    def list_webpages(self) -> list[WebPage]:
        pass
