from web_page.domain.repositories.webpage_repository import WebPageRepository


class FileHTMLRepository(WebPageRepository):
    def save_webpage(self, webpage, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(webpage.content)
        print(f"Archivo '{filename}' guardado correctamente.")