from pathlib import Path

from pydantic import BaseModel, model_validator


class FilePath(BaseModel):
    path: Path
    
    @model_validator(mode="before")
    def validate_path(cls, values):
        path = values.get("path")
        if path is None:
            raise ValueError("Path cannot be None")
        path_obj = Path(path)
        if not path_obj.exists():
            raise ValueError(f"Path does not exist: {path}")
        if not path_obj.is_file():
            raise ValueError(f"Not a valid file: {path}")
        return values