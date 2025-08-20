from stock_analyst.application.dto.webpage_dto import WebPageDTO
from stock_analyst.application.mapper.webpage_mapper import from_dto, to_dto
from stock_analyst.domain.repositories.webpage_repository import WebPageRepository
from stock_analyst.domain.value_objects.html_content import HTMLContent


class ScraperUseCase:
    def __init__(self, repository: WebPageRepository):
        self.repository = repository

    def save_webpage(self, dto: WebPageDTO) -> None:
        webpage = from_dto(dto)
        self.repository.save(webpage)

    def get_webpage_by_id(self, webpage_id: str) -> WebPageDTO:
        webpage = self.repository.get_by_id(webpage_id)
        return to_dto(webpage)

    def list_webpages(self) -> list[WebPageDTO]:
        webpages = self.repository.list_all()
        return [to_dto(wp) for wp in webpages]

    def update_webpage_content(self, webpage_id: str, new_html_content: str) -> None:
        webpage = self.repository.get_by_id(webpage_id)
        webpage.update_content(HTMLContent(new_html_content))
        self.repository.save(webpage)