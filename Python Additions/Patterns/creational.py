from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


# Creational Patterns from SB

# Pattern Singleton

class SingletonMeta(type):
    _instances = None

    def __call__(self):
        if self._instances is None:
            self._instance = super().__call__()

        return self._instance


class Singleton(metaclass=SingletonMeta):
    def some_logic(self):
        pass
