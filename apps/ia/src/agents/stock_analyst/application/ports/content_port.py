from abc import ABC, abstractmethod

from stock_analyst.application.dto.content_dto import ContentDTO


class ContentPort(ABC):
    @abstractmethod
    def analysis_content(self, path) -> ContentDTO:
        pass