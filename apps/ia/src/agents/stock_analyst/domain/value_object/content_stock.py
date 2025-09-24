from pydantic import BaseModel, Field, model_validator


class ContentStock(BaseModel):
    value: str = Field(..., description="The actual stock content")

    @model_validator(mode="before")
    def check_content_not_empty(cls, values):
        # In 'before' mode, values is a dict
        content = values.get("value") if isinstance(values, dict) else values
        if isinstance(content, str) and len(content.strip()) == 0:
            raise ValueError("The content cannot be empty.")
        return values

    model_config = {
        "frozen": True  # make the model immutable
    }