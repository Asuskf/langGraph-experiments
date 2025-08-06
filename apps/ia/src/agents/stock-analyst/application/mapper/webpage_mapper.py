from domain.entities.webpage import WebPage
from domain.value_objects.url import URL
from domain.value_objects.html_content import HTMLContent
from application.dto.webpage_dto import WebPageDTO


def to_dto(webpage: WebPage) -> WebPageDTO:
    return WebPageDTO(
        id=str(webpage.id),
        url=webpage.url.value,
        html_content=webpage.html_content.content
    )


def from_dto(dto: WebPageDTO) -> WebPage:
    return WebPage(
        id=dto.id,
        url=URL(dto.url),
        html_content=HTMLContent(dto.html_content)
    )