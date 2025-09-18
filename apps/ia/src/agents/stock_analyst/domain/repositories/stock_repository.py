from abc import ABC, abstractmethod

from stock_analyst.domain.entities.stock import Content


class StockRepository(ABC):
    @abstractmethod
    def analyse(self, content: Content) -> Content:
        pass