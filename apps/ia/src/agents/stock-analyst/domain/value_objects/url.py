from dataclasses import dataclass

@dataclass(frozen=True)
class URL:
    value: str

    def __post_init__(self):
        if not (self.value.startswith("http://") or self.value.startswith("https://")):
            raise ValueError(f"URL inválida: {self.value}")