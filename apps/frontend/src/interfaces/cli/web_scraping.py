import argparse
import re

from rich.console import Console
from rich.table import Table
from web_page.application.ports.file_port import FilePort
from web_page.application.ports.scraper_port import ScraperPort
from web_page.infrastructure.adapters.file_apdapter import FileTxtAdapter
from web_page.infrastructure.adapters.scraper_adapter import BeautifulSoupScraperAdapter

console = Console()

def main():
    parser = argparse.ArgumentParser(description="🚀 Scraper CLI using ScraperPort")
    parser.add_argument("url", type=str, help="URL to scrape")
    args = parser.parse_args()

    scraper: ScraperPort = BeautifulSoupScraperAdapter()
    file_txt: FilePort = FileTxtAdapter()
    
    
    console.print(f"🔍 Scraping URL: [bold blue]{args.url}[/bold blue] ...")
    result = scraper.scrape(args.url)
    # Contar párrafos usando etiquetas <p>
    html_content = result.html_content
    file_txt.save_file_txt(path="./", name_file="test.txt", content=html_content)
    # Buscar todas las etiquetas <p> en el HTML
    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", html_content, re.DOTALL)
    print(paragraphs)
    try:
        num_paragraphs = len(paragraphs)

        # Mostrar resultado en tabla
        table = Table(title="✅ Scraping result")
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        table.add_row("ID", str(getattr(result, "id", "N/A")))
        table.add_row("HTML size", f"{len(html_content)} characters")
        table.add_row("Number of paragraphs", str(num_paragraphs))
        console.print(table)
    except Exception as e:
        console.print(f"❌ Scraping error: {e}", style="bold red")

if __name__ == "__main__":
    main()