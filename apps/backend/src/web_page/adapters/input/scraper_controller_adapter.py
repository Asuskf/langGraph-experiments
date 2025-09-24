from web_page.application.dto.webpage_dto import WebPageDTO
from web_page.application.ports.scraper_port import ScraperPort
from web_page.application.service.scraper_use_case import ScraperUseCase


class ScraperControllerAdapter(ScraperPort):
    def __init__(self, use_case: ScraperUseCase):
        self.use_case = use_case

    def scrape_and_save(self, url: str) -> WebPageDTO:
        return self.use_case.save_webpage(url)