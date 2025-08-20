from dataclasses import dataclass

from stock_analyst.domain.value_objects.html_content import HTMLContent
from stock_analyst.domain.value_objects.url import URL


@dataclass
class WebPage:
    id: str
    url: URL
    html_content: HTMLContent

    def update_content(self, new_html_content: HTMLContent) -> None:
        self.html_content = new_html_content