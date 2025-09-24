import re

from pydantic import BaseModel, model_validator


class URL(BaseModel, frozen=True):
    value: str

    @model_validator(mode="before")
    def validate_url(cls, values):
        url = values.get("value")
        pattern = re.compile(r"^https?://[^\s/$.?#].[^\s]*$")
        if not url or not pattern.match(url):
            raise ValueError(f"Invalid URL: {url}")
        return values
