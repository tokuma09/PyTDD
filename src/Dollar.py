from src.Money import Money


class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)
