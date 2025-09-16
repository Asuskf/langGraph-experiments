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

class CliService:
    def __init__(self):
        self.scraper = BeautifulSoupScraperAdapter()
        self.file_txt = FileTxtAdapter(base_path=PATH_FOLDER)

    def scrape_url(self, url: str):
        console.print(f"🔍 Scraping URL: [bold blue]{url}[/bold blue] ...")
        try:
            result = self.scraper.scrape(url)
            html_content = result.html_content
            id_file = str(getattr(result, "id", "N/A"))
            self.file_txt.save_file_txt(name_file=f"{id_file}.txt", content=html_content)
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
            console.print(f"❌ Error scraping URL: {e}", style="bold red")

    def read_file(self, name: str):
        content = self.file_txt.read_file_txt(name)
        console.print(content[:500] + "..." if content else "❌ File not found")

    def delete_file(self, name: str):
        success = self.file_txt.drop_file_txt(name)
        console.print("🗑️  File deleted" if success else "❌ File not found")
