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


def roll_dice(rolls: int = 1000):
    """Returns a list of the outcomes from rolling two 6 sided
    dice based off randomly choising the outcome from the porbability
    that outcome will occur. Best if used with a counting function.

    Args:
        rolls (int, optional): Number of rolls to simulate. Defaults to 1000.
    """
    outcomes = random.choices(
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        [1/36, 1/18, 1/12, 1/9, 5/36, 1/6, 5/36, 1/9, 1/12, 1/18, 1/36],
        k = rolls
    )
    return outcomes


def count_outcomes(outcomes):
    pass


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
