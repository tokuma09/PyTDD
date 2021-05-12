from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @abstractmethod
    def times(self, multiplier):
        pass

    def __eq__(self, money):
        return (self._amount == money._amount) & (type(self) == type(money))

    @staticmethod
    def dollar(amount):
        from src.Dollar import Dollar

        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        from src.Franc import Franc

        return Franc(amount, 'CHF')

    @property
    def currency(self):
        return self._currency
