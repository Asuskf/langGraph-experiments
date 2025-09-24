from typing import TypedDict

from langgraph.graph import StateGraph
from stock_analyst.application.mapper.content_mapper import ContentDTO, ContentMapper
from stock_analyst.domain.repositories.stock_repository import StockRepository


class StockState(TypedDict):
    content: ContentDTO


def analyse_node(state: StockState, repository: StockRepository):
    entity = ContentMapper.from_dto_content(state["content"])
    analysed_entity = repository.analyse(entity)
    dto = ContentMapper.to_dto_content(analysed_entity)
    return {"content": dto}

def build_stock_graph(repository: StockRepository):
    graph = StateGraph(StockState)
    graph.add_node("analyse", lambda s: analyse_node(s, repository))
    graph.set_entry_point("analyse")
    graph.set_finish_point("analyse")
    return graph.compile()