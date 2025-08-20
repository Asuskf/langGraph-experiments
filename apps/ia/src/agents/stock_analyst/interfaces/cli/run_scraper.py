import argparse

from stock_analyst.application.mapper.webpage_mapper import to_dto
from stock_analyst.application.service.scraper_use_case import ScraperUseCase
from stock_analyst.infrastructure.external.beautifulsoup_scraper import (
    BeautifulSoupScraper,
)
from stock_analyst.infrastructure.persistence.memory_webpage_repo import (
    InMemoryWebPageRepository,
)


def main():
    parser = argparse.ArgumentParser(description="Ejecutar el scraper para una URL dada.")
    parser.add_argument("url", type=str, help="URL a scrapear")
    args = parser.parse_args()

    # Infraestructura
    repo = InMemoryWebPageRepository()
    scraper = BeautifulSoupScraper()

    # Aplicación
    use_case = ScraperUseCase(repo)

    try:
        # Ejecutar scraping
        webpage = scraper.fetch_and_parse(args.url)
        use_case.save_webpage(to_dto(webpage))

        # Mostrar resumen
        print("✅ WebPage guardada:")
        print(f"ID: {webpage.id}")
        print(f"URL: {webpage.url.value}")
        print(f"HTML size: {len(webpage.html_content.content)} characters")

    except Exception as e:
        print(f"❌ Error: {str(e)}")


if __name__ == "__main__":
    main()