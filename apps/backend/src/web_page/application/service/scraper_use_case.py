from web_page.application.dto.webpage_dto import WebPageDTO
from web_page.application.mapper.webpage_mapper import from_dto_webpage, to_dto_webpage
from web_page.domain.repositories.webpage_repository import WebPageRepository


class ScraperUseCase:
    def __init__(self, web_repository: WebPageRepository):
        self.web_repository = web_repository

    def scrape_webpage(self, dto: WebPageDTO) -> None:
        webpage = from_dto_webpage(dto)
        self.repository.save(webpage)
 