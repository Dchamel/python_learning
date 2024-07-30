from abc import ABC, abstractmethod


# Behavioral Patterns from SB


# Pattern Strategy
class Strategy(ABC):
    """Abstract base class for Strategies."""

    @abstractmethod
    def calc_effective_path(self, deata):
        pass


class AutoStrategy(Strategy):
    """Strategy for delivery by car"""

    def calc_effective_path(self, data):
        # calc path
        return data


class BikeStrategy(Strategy):
    """Strategy for delivery by bike"""

    def calc_effective_path(self, data):
        # calc path
        return data


class Courier:
    def __init__(self, strategy: Strategy) -> None:
        """Takes a strategy as a parameter"""
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """Access from code"""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Set up new strategy"""
        self._strategy = strategy

    def get_effective_path(self, data) -> None:
        """Calculate effective path"""
        return self._strategy.calc_effective_path(data)

# Pattern Observer

# class ShopList():
#     """Class for storing"""
#
#     def __init__(self):
#         # list of the clients
#         self._observers = []
#
#     def attach(self, observer) -> None:
#         self._observers.append(observer)
#
#     def detach(self, observer) -> None:
#         self._observers.remove(observer)
#
#     def notify(self) -> None:
#         """Notify all clients"""
#         for observer in self._observers:
#             observer.update(self)
#
#     def business_logic(self) -> None:
#         """SOme business logic"""
#         self.notify()
#
#
# class Observer(ABC):
#     """Abstract Observer class"""
#
#     @abstractmethod
#     def update(self, shop_list_object) -> None:
#         pass
#
#
# class EmailObserver(Observer):
#     def update(self, shop_list_object) -> None:
#         pass
#
#
# class SmsObserver(Observer):
#     def update(self, shop_list_object) -> None:
#         pass
#
# # Pattern
