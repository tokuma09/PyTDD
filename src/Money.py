class Money():
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @property
    def currency(self):
        return self._currency

    @property
    def amount(self):
        return self._amount

    def reduce(self, to):
        return self

    def plus(self, addend):
        from src.Sum import Sum
        return Sum(self, addend=addend)

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def __eq__(self, money):
        return (self.amount == money.amount) & (self.currency
                                                == money.currency)

    def __repr__(self):
        return str(self.amount) + " " + self.currency

    @staticmethod
    def dollar(amount):
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Money(amount, 'CHF')
