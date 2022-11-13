#!/usr/bin/env python3
"""Python file to watch how things interact with PyCharm
Git and GitHub
"""


def is_it_prime(number: int) -> bool:
    """Returns True if the passed number is prime."""
    chk_prime: int = 1

    while chk_prime <= (number // 2):
        chk_prime += 1

        if not number % chk_prime:
            return False

    return True


if __name__ == '__main__':
    n: int = 13

    if is_it_prime(n):
        print(f'{n} is prime')
