from dataclasses import dataclass
from typing import Callable


@dataclass
class Capability:
    trigger: Callable
    checks: list[Callable]
    behavior: Callable
