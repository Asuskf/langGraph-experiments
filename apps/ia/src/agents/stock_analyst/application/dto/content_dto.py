from pydantic import BaseModel, Field


class ContentDTO(BaseModel):
    value: str = Field(..., description="Stock content")
    analysis: str | None = Field(None, description="Optional analysis result")