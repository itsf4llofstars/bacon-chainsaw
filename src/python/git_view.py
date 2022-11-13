#!/usr/bin/env python3
"""DOC"""


def add_two_nums(a: int, b: int = 47) -> int:
    """
    parameters:
        a [int]: Parameter to be added.
        b [int]: Parmeter to be added. (optional) deafulted to 47

    return:
        [int]: b added to a
    """
    c: int = a + b
    return c


def main(argv, *args, **kwargs) -> None:
    """main function"""
    print(add_two_nums(int(argv[1])))
    print(add_two_nums(int(argv[1]), int(argv[2])))

    x: int = 20
    y: int = 30
    print(add_two_nums(x, y))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
