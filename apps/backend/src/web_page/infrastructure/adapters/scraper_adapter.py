from web_page.application.mapper.webpage_mapper import to_dto_webpage
from web_page.application.ports.scraper_port import ScraperPort
from web_page.infrastructure.scrapers.beautifulsoup_scraper import BeautifulSoupScraper


class BeautifulSoupScraperAdapter(ScraperPort):
    def __init__(self):
        self.scraper = BeautifulSoupScraper()

    def scrape(self, url: str):
        webpage = self.scraper.fetch_and_parse(url)
        return to_dto_webpage(webpage)