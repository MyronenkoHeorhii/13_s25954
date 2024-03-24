import abc


class SquareGenerator(abc.ABC):
    @abc.abstractmethod
    def generate_squares(self, start, end):
        squares = [x * x for x in range(start, end)]
        return squares
