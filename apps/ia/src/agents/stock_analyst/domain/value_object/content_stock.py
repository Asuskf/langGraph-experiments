from pydantic import BaseModel, model_validator


class ContentStock(BaseModel, frozen=True):
    value = str

    @model_validator(mode="before")
    def check_content_not_empty(cls, values):
        content = values
        if isinstance(content, dict):
            content = values.get("content")
        if len(content.strip()) > 0:
            raise ValueError("The content cannot be empty.")
        return values
    model_config = {
        'frozen': True
    }
