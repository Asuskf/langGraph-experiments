
import re

from pydantic import BaseModel, model_validator


class FileNameTxt(BaseModel, frozen=True):
    value: str
    
    @model_validator(mode="before")
    def validate_txt_filename(cls, values):
        if not values.endswith(".txt"):
            raise ValueError("The file must have a .txt extension.")
        if re.search(r'[<>:"/\\|?*]', values):
            raise ValueError("The file name contains invalid characters.")
        return values