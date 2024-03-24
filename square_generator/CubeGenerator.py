from square_generator.square_generator import SquareGenerator


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        cubes = [x * x * x for x in range(start, end)]
        return cubes

    def generate_squares(self, start, end):
        if start >= end:
            raise ValueError("start must be less than end")

        squares = [x * x for x in range(start, end)]
        return squares
