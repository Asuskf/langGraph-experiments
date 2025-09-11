from web_page.application.dto.webpage_dto import WebPageDTO
from web_page.domain.entities.webpage import WebPage
from web_page.domain.value_objects.html_content import HTMLContent
from web_page.domain.value_objects.url import URL


def to_dto_webpage(webpage: WebPage) -> WebPageDTO:
    return WebPageDTO(
        id = str(webpage.id),
        url = webpage.url.value,
        html_content = webpage.html_content.content
    )

def from_dto_webpage(dto: WebPageDTO) -> WebPage:
    return WebPage(
        id = dto.id,
        url = URL(value=dto.url),
        html_content = HTMLContent(content=dto.html_content)
    )