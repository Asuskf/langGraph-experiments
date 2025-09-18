from stock_analyst.domain.entities.stock import Content
from stock_analyst.domain.repositories.stock_repository import StockRepository


class AnalysisStockUseCase:
    def __init__(self, repositorie_stock_summary: StockRepository):
        self.repositorie_stock_summary = repositorie_stock_summary
    
    def execute(self, content_stock: str) -> None:
        content = Content(content=content_stock)
        self.repositorie_stock_summary.analyse(content)