from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount

    @abstractmethod
    def times(self, multiplier):
        pass

    def __eq__(self, money):
        return (self._amount == money._amount) & (type(self) == type(money))

    @staticmethod
    def dollar(amount):
        from src.Dollar import Dollar

        return Dollar(amount)

    @staticmethod
    def franc(amount):
        from src.Franc import Franc

        return Franc(amount)
