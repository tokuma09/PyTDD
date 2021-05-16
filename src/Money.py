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

    def plus(self, addend):
        return Money(self.amount + addend.amount, self.currency)

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def __eq__(self, money):
        return (self.amount == money.amount) & (self.currency
                                                == money.currency)

    def __repr__(self):
        return str(self.amount) + " " + self.currency

    def dollar(self, amount):
        return Money(amount, 'USD')

    def franc(self, amount):
        return Money(amount, 'CHF')
