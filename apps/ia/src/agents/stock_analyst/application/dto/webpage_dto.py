from dataclasses import dataclass


@dataclass
class WebPageDTO:
    id: str
    url: str
    html_content: str