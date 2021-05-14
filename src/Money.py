from abc import abstractmethod


class Money():
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @abstractmethod
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

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

    @property
    def amount(self):
        return self._amount

    def __eq__(self, money):
        return (self.amount == money.amount) & (self.currency
                                                == money.currency)

    def __repr__(self):
        return str(self.amount) + " " + self.currency
