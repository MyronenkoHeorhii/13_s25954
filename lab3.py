from square_generator.square_generator import SquareGenerator

# =======task_1========================
import math

squares = [x * x for x in range(1, 10)]
print(squares)


# =======task_2========================
def generate_squares(start, end):
    squares = [x * x for x in range(start, end)]
    return squares


print(generate_squares(1, 10))


# =======task_3========================

squares = SquareGenerator()
print(squares.generate_squares(1, 10))

# =======task_4========================
listOfSquares = squares.generate_squares(1, 10)
roots = [math.sqrt(num) for num in listOfSquares]
print(roots)


# =======task_5========================
def generate_squares(start, end):
    squares = [x * x for x in range(start, end + 1)]
    return squares


print(generate_squares(1, 10))

# =======task_6========================
