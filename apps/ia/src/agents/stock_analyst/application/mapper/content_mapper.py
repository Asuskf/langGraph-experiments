from stock_analyst.application.dto.content_dto import ContentDTO
from stock_analyst.domain.entities.stock import Content
from stock_analyst.domain.value_object.content_stock import ContentStock


def to_dto_content(content: Content) -> ContentDTO:
    return ContentDTO(
        content = content.content.value
    )

def from_dto_content(dto: ContentDTO) -> Content:
    return Content(
        content= ContentStock(dto.content)
    )