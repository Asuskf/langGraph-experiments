from dataclasses import dataclass
import re

@dataclass(frozen=True)
class URL:
    value: str

    def __post_init__(self):
        pattern = re.compile(r"^https?://[^\s/$.?#].[^\s]*$")
        if not pattern.match(self.value):
            raise ValueError(f"URL inválida: {self.value}")