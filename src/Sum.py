from src.Expression import Expression
from src.Money import Money


class Sum(Expression):
    def __init__(self, augend, addend) -> None:
        self._augend = augend
        self._addend = addend

    @property
    def augend(self):
        return self._augend

    @property
    def addend(self):
        return self._addend

    def reduce(self, currency):
        amount = self.augend.amount + self.addend.amount

        return Money(amount, currency)
