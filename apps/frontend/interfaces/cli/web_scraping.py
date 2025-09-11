import argparse
import re

from rich.console import Console
from rich.table import Table
from web_page.application.ports.scraper_port import ScraperPort
from web_page.infrastructure.adapters.scraper_adapter import BeautifulSoupScraperAdapter

console = Console()

def main():
    parser = argparse.ArgumentParser(description="🚀 Scraper CLI usando ScraperPort")
    parser.add_argument("url", type=str, help="URL a scrapear")
    args = parser.parse_args()

    scraper: ScraperPort = BeautifulSoupScraperAdapter()
    
    try:
        console.print(f"🔍 Scrapeando la URL: [bold blue]{args.url}[/bold blue] ...")
        result = scraper.scrape(args.url)
        # Contar párrafos usando etiquetas <p>
        html_content = result.html_content
        # Buscar todas las etiquetas <p> en el HTML
        paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", html_content, re.DOTALL)
        num_paragraphs = len(paragraphs)

        # Mostrar resultado en tabla
        table = Table(title="✅ Resultado del Scraping")
        table.add_column("Campo", style="cyan", no_wrap=True)
        table.add_column("Valor", style="magenta")

        table.add_row("ID", str(getattr(result, "id", "N/A")))
        table.add_row("HTML size", f"{len(html_content)} caracteres")
        table.add_row("Número de párrafos", str(num_paragraphs))

        console.print(table)
    except Exception as e:
        console.print(f"❌ Error al scrapear: {e}", style="bold red")

if __name__ == "__main__":
    main()