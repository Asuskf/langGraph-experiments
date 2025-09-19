from stock_analyst.application.dto.content_dto import ContentDTO
from stock_analyst.domain.entities.stock import Content
from stock_analyst.domain.value_object.content_stock import ContentStock


class ContentMapper:
    @staticmethod
    def to_dto_content(entity: Content) -> ContentDTO:
        return ContentDTO(
            content = entity.content.value,
            analysis = entity.analysis
        )
    @staticmethod
    def from_dto_content(dto: ContentDTO) -> Content:
        content_vo = ContentStock(value=dto.value)
        return Content(content=content_vo, analysis=dto.analysis)