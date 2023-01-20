from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class BehaviorDocument:
    name: str
    type: str
    data: dict


@dataclass
class CheckDocument:
    type: str
    data: dict


@dataclass
class Capability:
    trigger: Callable
    checks: list[Callable]
    behaviors: list[Any]


@dataclass
class CapabilityDocument:
    name: str
    trigger: str
    behaviors: list[BehaviorDocument]
    checks: list[CheckDocument]
    requiredPowers: list[str]


@dataclass
class Personality:
    name: str
    behaviors: list[BehaviorDocument]
    capabilities: list[Capability]
