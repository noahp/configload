import dataclasses

from configload import PyConfigFile


class TestConfigFile(PyConfigFile):
    key1: str = "default"
    key2: int = 123
    key3: float = 1.23
    key4: list = dataclasses.field(default_factory=list)
    key4: dict = dataclasses.field(default_factory=dict)
