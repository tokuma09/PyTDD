from abc import ABCMeta, abstractmethod


class Expression(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def reduce(self, currency):
        pass
