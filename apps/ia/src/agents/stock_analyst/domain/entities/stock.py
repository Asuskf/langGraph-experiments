from pydantic import BaseModel, Field
from stock_analyst.domain.value_object.content_stock import ContentStock

class Content(BaseModel):
    content: ContentStock = Field(..., description="Content of stock")
    analysis: str | None = Field(None, description="Optional analysis result")