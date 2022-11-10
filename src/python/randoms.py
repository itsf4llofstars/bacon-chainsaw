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
    return random.randint(low, high)


def main(argv):
    print(f'Running: {argv[0]}')

    a_random_int = generate_rand_int(100)
    print(f'{a_random_int = }')

    a_random_int = generate_rand_int(30, 20)
    print(f'{a_random_int = }')

    random_year = get_year(1033, 2022)
    print(f'{random_year = }')


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
