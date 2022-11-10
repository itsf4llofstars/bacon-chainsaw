"""randoms.py is used to explore Python's random module
"""
import random


def generate_rand_int(high: int, low: int = 1) -> int:
    """Generate and return a random number btween
    two user passed numbers.

    parameters:
        low (int): Random start number, inclusive. Defaults to 1
        hight (int): Random stop number, inclusive.

    returns:
        (int): Random integer between low and high, inclusive.
    """
    return random.randint(low, high)


def get_year(low, high):
    """Calls the generate_rand_int function in
    randoms.py, returns a year and prints it to
    the terminal.

    parameters:
        low (int): The lowest year for random choice.
        high (int): The highest year for random choice.

    returns:
        (int): A random year between low, high inclusive.
    """
    return randoms.generate_rand_int(high, low)


def main(argv):
    a_random_int = generate_rand_int(100)
    print(f'{a_random_int = }')

    a_random_int = generate_rand_int(30, 20)
    print(f'{a_random_int = }')


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))

