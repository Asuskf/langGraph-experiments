from stock_analyst.domain.entities.stock import Content
from stock_analyst.domain.repositories.stock_repository import StockRepository


class StockAdapter(StockRepository):

    def analyse(self, content: Content) -> Content:
        analysis_text = f"Analysis result: {content.content.value[:50]}..."
        return Content(content=content.content, analysis=analysis_text)