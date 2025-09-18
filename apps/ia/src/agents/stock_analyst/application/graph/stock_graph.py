from typing import TypedDict

from langgraph.graph import StateGraph
from stock_analyst.application.dto.content_dto import ContentDTO
from stock_analyst.application.mapper.content_mapper import to_dto_content
from stock_analyst.domain.repositories.stock_repository import StockRepository


class StockState(TypedDict):
    content = ContentDTO
def fetch_content_node(state: StockState, repository: StockRepository):
    # Llamamos al repository para obtener la entidad de dominio
    domain_obj = repository.get_analysis("AAPL")  # ejemplo con ticker fijo, se puede parametrizar

    # Convertimos la entidad de dominio a DTO
    dto = to_dto_content(domain_obj)

    # Retornamos el nuevo estado
    return {"content": dto}

def stock_analize(repository: StockRepository):
    graph = StateGraph(StockState)
    graph.add_node("fetch_content" , lambda s: fetch_content_node(s, repository))