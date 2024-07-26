from abc import ABC, abstractmethod


# Strategy Pattern from SB
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

# -----------------------------------------------------------------

# Strategy Pattern from Internet
