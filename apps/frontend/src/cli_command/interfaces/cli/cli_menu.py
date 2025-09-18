from cli_command.application.cli_service import CliService
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def show_menu():
    console.print("[bold blue]🚀 Welcome to the Scraper CLI[/bold blue]")
    console.print("1. Scrape a URL")
    console.print("2. Read a file")
    console.print("3. Delete a file")
    console.print("0. Exit")

def main():
    service = CliService()

    while True:
        show_menu()
        choice = Prompt.ask("Choose an option", choices=["1","2","3","4","0"])
        
        if choice == "1":
            url = Prompt.ask("Enter the URL to scrape")
            service.scrape_url(url)
        elif choice == "2":
            name = Prompt.ask("Enter the file name")
            service.read_file(name)
        elif choice == "3":
            name = Prompt.ask("Enter the file name")
            service.delete_file(name)
        elif choice == "0":
            console.print("👋 Bye!")
            break

if __name__ == "__main__":
    main()