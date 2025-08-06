from dataclasses import dataclass
from domain.value_objects.url import URL
from domain.value_objects.html_content import HTMLContent

@dataclass
class WebPage:
    id: str
    url: URL
    html_content: HTMLContent

    def update_content(self, new_html_content: HTMLContent) -> None:
        self.html_content = new_html_content