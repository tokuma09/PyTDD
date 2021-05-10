class Dollar():
    def __init__(self, amount):
        # private variable
        self.__amount = amount

    def times(self, multiplier):
        return Dollar(self.__amount * multiplier)

    def equals(self, dollar):
        return self.__amount == dollar._Dollar__amount

    def __eq__(self, other):
        return self.__amount == other._Dollar__amount
