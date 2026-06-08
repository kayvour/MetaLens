from dataclasses import dataclass


@dataclass
class Issue:
    severity: str
    check: str
    message: str
