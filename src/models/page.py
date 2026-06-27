from dataclasses import dataclass
from models.issue import Issue

@dataclass
class Page:
    url: str
    score: int
    issues: list[Issue]
