#!/usr/bin/env python3
"""main.py file form which all other function, helper,
class files can be called from.
"""
import randoms as rand

def main(argv):
    print(f'Running: {argv[0]}')

    rand_num = rand.generate_rand_int(100)
    print(f'{rand_num = }')

    rand_num = rand.generate_rand_int(1000, 100)
    print(f'{rand_num = }')

    rand_year = rand.get_year(1900, 1999)
    print(f'Year: {rand_year}')


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
