class Franc():
    def __init__(self, amount):
        # private variable
        self.__amount = amount

    def times(self, multiplier):
        return Franc(self.__amount * multiplier)

    def equals(self, dollar):
        return self.__amount == dollar._Franc__amount

    def __eq__(self, other):
        return self.__amount == other._Franc__amount
