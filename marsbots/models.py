from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class CapabilityDocument:
    name: str
    type: str
    data: dict


@dataclass
class ModifierDocument:
    type: str
    data: dict


@dataclass
class Command:
    trigger: Callable
    modifiers: list[Callable]
    capabilities: list[Any]


@dataclass
class CommandDocument:
    name: str
    trigger: str
    capabilities: list[CapabilityDocument]
    modifiers: list[ModifierDocument]
    requiredPowers: list[str]


@dataclass
class Character:
    name: str
    capabilities: list[CapabilityDocument]
    commands: list[Command]
