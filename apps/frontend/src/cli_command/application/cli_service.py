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
        parser = argparse.ArgumentParser(description="🚀 Scraper CLI using ScraperPort")
        parser.add_argument("url", type=str, help="URL to scrape")
        args = parser.parse_args()
        console.print(f"🔍 Scraping URL: [bold blue]{args.url}[/bold blue] ...")
        try:
            result = self.scraper.scrape(url)
            self.file_txt.save_file_txt(f"{result.id}.txt", result.html_content)
            console.print(f"✅ File saved as {result.id}.txt")
        except Exception as e:
            console.print(f"❌ Error scraping URL: {e}", style="bold red")

    def list_files(self):
        files = self.file_txt.list_files()
        table = Table(title="📂 Saved Files")
        table.add_column("File Name")
        for f in files:
            table.add_row(f)
        console.print(table)

    def read_file(self, name: str):
        content = self.file_txt.read_file(name)
        console.print(content[:500] + "..." if content else "❌ File not found")

    def delete_file(self, name: str):
        success = self.file_txt.delete_file(name)
        console.print("🗑️ File deleted" if success else "❌ File not found")
