
import re

from pydantic import BaseModel, model_validator


class FileNameTxt(BaseModel, frozen=True):
    value: str

    @model_validator(mode="before")
    def validate_txt_filename(cls, values):
        # Si values es un dict (como normalmente lo será)
        filename = values.get("value")
        
        # Validación de extensión
        if not filename.endswith(".txt"):
            raise ValueError("The file must have a .txt extension.")
        
        # Validación de caracteres inválidos
        if re.search(r'[<>:"/\\|?*]', filename):
            raise ValueError("The file name contains invalid characters.")

        # Debe devolverse un dict con el campo value
        return values