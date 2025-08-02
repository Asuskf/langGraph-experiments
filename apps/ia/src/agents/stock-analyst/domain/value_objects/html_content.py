from dataclasses import dataclass

@dataclass(frozen=True)
class HTMLContent:
    content: str

    def __post_init__(self):
        if not self.content.strip():
            raise ValueError("El contenido HTML no puede estar vacío")