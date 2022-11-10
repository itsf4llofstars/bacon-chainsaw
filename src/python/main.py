#!/usr/bin/env python3
"""main.py file form which all other function, helper,
class files can be called from.
"""

def main(argv):
    random_year = randoms.generate_rand_int(2022, 1941)
    print(f'{random_year = }')

    random_year = get_year(1941, 2022)
    print(f'{random_year = }')


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))


