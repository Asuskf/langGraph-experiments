import requests
from bs4 import BeautifulSoup
from domain.entities.webpage import WebPage
from domain.value_objects.url import URL
from domain.value_objects.html_content import HTMLContent
import uuid


class BeautifulSoupScraper:
    def fetch_and_parse(self, url: str) -> WebPage:
        response = requests.get(url)
        response.raise_for_status()  # Lanza excepción si el código no es 200

        soup = BeautifulSoup(response.text, "html.parser")
        cleaned_html = soup.prettify()

        return WebPage(
            id=str(uuid.uuid4()),
            url=URL(url),
            html_content=HTMLContent(cleaned_html)
        )