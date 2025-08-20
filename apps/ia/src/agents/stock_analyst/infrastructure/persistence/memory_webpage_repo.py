
from stock_analyst.domain.entities.webpage import WebPage
from stock_analyst.domain.repositories.webpage_repository import WebPageRepository


class InMemoryWebPageRepository(WebPageRepository):
    def __init__(self):
        self.storage: dict[str, WebPage] = {}

    def save(self, webpage: WebPage) -> None:
        self.storage[str(webpage.id)] = webpage

    def get_by_id(self, webpage_id: str) -> WebPage:
        if webpage_id not in self.storage:
            raise ValueError(f"WebPage con ID '{webpage_id}' no encontrada")
        return self.storage[webpage_id]

    def list_all(self) -> list[WebPage]:
        return list(self.storage.values())