from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty

from pip._internal.resolution.resolvelib import factory

# Creational Patterns from SB

# Pattern Singleton

# class SingletonMeta(type):
#     _instances = None
#
#     def __call__(self):
#         if self._instances is None:
#             self._instance = super().__call__()
#
#         return self._instance
#
#
# class Singleton(metaclass=SingletonMeta):
#     def some_logic(self):
#         pass

# Pattern Abstract Factory

# class AbstractFactory(ABC):
#     """
#     Abstract Factory interface declares a set of methods that
#     return different abstract products
#     """
#
#     @abstractmethod
#     def create_product(self):
#         pass
#
#     @abstractmethod
#     def create_provider(self):
#         pass
#
#
# class TeaFactory(AbstractFactory):
#     """Factory for creating tea-objects"""
#
#     def create_product(self):
#         return TeaProduct()
#
#     def create_provider(self):
#         return TeaProvider()
#
#
# class CoffeeFactory(AbstractFactory):
#     """Factory for creating tea-objects"""
#
#     def create_product(self):
#         return CoffeeProduct()
#
#     def create_provider(self):
#         return CoffeeProvider()
#
#
# class AbstractProduct(ABC):
#     """Each product of web-store"""
#
#     @abstractmethod
#     def some_function(self):
#         pass
#
#
# class TeaProduct(AbstractProduct):
#
#     def some_function(self):
#         return "I am a tea product"
#
#
# class CoffeeProduct(AbstractProduct):
#
#     def some_function(self):
#         return "I am a coffee product"
#
#
# class AbstractProvider(ABC):
#     """Each product of web-store"""
#
#     @abstractmethod
#     def country_list(self):
#         pass
#
#
# class CoffeeProvider(AbstractProvider):
#     def country_list(self):
#         return ["USA", "Germany"]
#
#     def some_business_logic():
#         product = factory.create_product()
#         provider = factory.create_provider()
#         print(product.some_function())
#         print(provider.country_list())
#
#
# if __name__ == '__main__':
#     some_business_logic(TeaFactory())
#     some_business_logic(CoffeeFactory())
