from abc import ABC, abstractmethod

from web_page.application.dto.webpage_dto import WebPageDTO


class ScraperPort(ABC):
    @abstractmethod
    def scrape(self, url: str) -> WebPageDTO:
        pass