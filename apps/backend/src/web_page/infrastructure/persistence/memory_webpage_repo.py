
from web_page.domain.entities.webpage import WebPage
from web_page.domain.repositories.webpage_repository import WebPageRepository


class InMemoryWebPageRepository(WebPageRepository):
    def __init__(self):
        self.storage: dict[str, WebPage] = {}

    def scrape_webpage(self, webpage: WebPage) -> None:
        self.storage[str(webpage.id)] = webpage