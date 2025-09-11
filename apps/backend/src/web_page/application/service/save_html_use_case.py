from web_page.domain.entities.webpage import HTMLContent
from web_page.domain.repositories.webpage_repository import WebPageRepository


class SaveHTMLUseCase:
    def __init__(self, repositorie_web_page: WebPageRepository):
        self.repositorie_web_page = repositorie_web_page
        
    def execute(self, html_content: str, filename: str) -> None:
        content = HTMLContent(content=html_content)
        self.repositorie_web_page.save_webpage(content, filename)