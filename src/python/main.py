#!/usr/bin/env python3
"""main.py file form which all other function, helper,
class files can be called from.
"""
import randoms


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
    random_year = randoms.generate_rand_int(2022, 1941)
    print(f'{random_year = }')

    random_year = get_year(1941, 2022)
    print(f'{random_year = }')


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


