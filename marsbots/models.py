from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Capability:
    trigger: Callable
    checks: list[Callable]
    behaviors: list[Any]
