
from web_page.domain.entities.webpage import WebPage
from web_page.domain.repositories.webpage_repository import WebPageRepository


class InMemoryWebPageRepository(WebPageRepository):
    def __init__(self):
        self.storage: dict[str, WebPage] = {}

    def save_webpage(self, webpage: WebPage) -> None:
        self.storage[str(webpage.id)] = webpage

    def get_webpage_by_id(self, webpage_id: str) -> WebPage:
        if webpage_id not in self.storage:
            raise ValueError(f"WebPage with ID '{webpage_id}' not found")
        return self.storage[webpage_id]

    def list_webpages(self) -> list[WebPage]:
        return list(self.storage.values())