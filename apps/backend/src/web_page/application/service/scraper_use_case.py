from web_page.application.dto.webpage_dto import WebPageDTO
from web_page.application.mapper.webpage_mapper import from_dto_webpage, to_dto_webpage
from web_page.domain.repositories.webpage_repository import WebPageRepository


class ScraperUseCase:
    def __init__(self, web_repository: WebPageRepository):
        self.web_repository = web_repository

    def save_webpage(self, dto: WebPageDTO) -> None:
        webpage = from_dto_webpage(dto)
        self.repository.save(webpage)
        
    def get_webpage_by_id(self, webpage_id: str) -> WebPageDTO:
        webpage = self.repository.get_by_id(webpage_id)
        return to_dto_webpage(webpage)
    
    def list_webpages(self) -> list[WebPageDTO]:
        webpages = self.repository.list_all()
        return [to_dto_webpage(wp) for wp in webpages]