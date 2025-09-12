import argparse
import os
import re
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from web_page.application.ports.file_port import FilePort
from web_page.application.ports.scraper_port import ScraperPort
from web_page.infrastructure.adapters.file_apdapter import FileTxtAdapter
from web_page.infrastructure.adapters.scraper_adapter import BeautifulSoupScraperAdapter

console = Console()
load_dotenv()
base_dir = Path(__file__).resolve().parent  
project_root = base_dir.parents[2]
PATH_FOLDER = os.getenv("DATA_FOLDER_WEB")

def main():
    parser = argparse.ArgumentParser(description="🚀 Scraper CLI using ScraperPort")
    parser.add_argument("url", type=str, help="URL to scrape")
    args = parser.parse_args()
    scraper: ScraperPort = BeautifulSoupScraperAdapter()
    file_txt: FilePort = FileTxtAdapter(base_path=PATH_FOLDER)

    console.print(f"🔍 Scraping URL: [bold blue]{args.url}[/bold blue] ...")
    try:
        result = scraper.scrape(args.url)
        html_content = result.html_content
        id_file = str(getattr(result, "id", "N/A"))
        file_txt.save_file_txt(name_file=f"{id_file}.txt", content=html_content)
        paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", html_content, re.DOTALL)
    
        num_paragraphs = len(paragraphs)

        table = Table(title="✅ Scraping result")
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        table.add_row("ID", id_file)
        table.add_row("HTML size", f"{len(html_content)} characters")
        table.add_row("Number of paragraphs", str(num_paragraphs))
        console.print(table)
    except Exception as e:
        console.print(f"❌ Scraping error: {e}", style="bold red")

if __name__ == "__main__":
    main()