from pydantic import BaseModel, model_validator


class HTMLContent(BaseModel):
    content: str

    @model_validator(mode="before")  # Se ejecuta antes de crear el modelo
    def check_content_not_empty(cls, values):
        content = values
        if isinstance(content, dict):
            content = values.get("content")
        if not content or not content.strip():
            raise ValueError("The HTML content cannot be empty.")
        
        return values

    model_config = {
        "frozen": True  # Hace que el modelo sea inmutable
    }
