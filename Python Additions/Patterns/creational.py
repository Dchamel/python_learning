from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty, ABCMeta

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

# Pattern Builder

# class AbstractBuilder(ABC):
#     """Abstract Builder Class"""
#
#     @abstractmethod
#     def product(self):
#         pass
#
#     @abstractmethod
#     def build_part_1(self):
#         pass
#
#     @abstractmethod
#     def build_part_2(self):
#         pass
#
#     @abstractmethod
#     def build_part_3(self):
#         pass
#
#
# class HouseBuilder(AbstractBuilder):
#     """House Builder Class"""
#
#     def __init__(self):
#         self.reset()
#
#     def reset(self):
#         self._house = House()
#
#     @property
#     def product(self):
#         """Get instance of object"""
#         house = self._house
#         self.reset()
#         return house
#
#     def build_part_1(self):
#         self._house.add('Walls')
#
#     def build_part_2(self):
#         self._house.add('Roof')
#
#     def build_part_3(self):
#         self._house.add('Flat')
#
#
# class House():
#     def __init__(self):
#         self.parts = []
#
#     def add(self, part):
#         self.parts.append(part)
#
#     def list_parts(self):
#         print(self.parts)
#
#
# class Director:
#     """Director Class that manage building stages"""
#
#     def __init__(self):
#         self._builder = None
#
#     @property
#     def builder(self):
#         return self._builder
#
#     @builder.setter
#     def builder(self, builder):
#         self._builder = builder
#
#     def build_product(self):
#         self.builder.build_part_1()
#         self.builder.build_part_2()
#         self.builder.build_part_3()

# Pattern Factory

class Worker(metaclass=ABCMeta):
    @abstractmethod
    def who_i_am(self):
        pass


class SimpleWorker(Worker):
    def who_i_am(self):
        print('I am a worker')


class Developer(Worker):
    def who_i_am(self):
        print('I am a developer')


class DevOpsMan(Worker):
    def who_i_am(self):
        print('I am a DevOpsMan')


class WorkersFactory:
    registred_workers = {
        None: SimpleWorker,
        'developer': Developer,
        'dev_ops': DevOpsMan
    }

    @classmethod
    def create_worker(cls, worker_type=None):
        worker_cls = cls.registred_workers[worker_type]
        return worker_cls()


if __name__ == '__main__':
    w1 = WorkersFactory.create_worker()
    w1.who_i_am()
    w2 = WorkersFactory.create_worker('dev_ops')
    w2.who_i_am()
