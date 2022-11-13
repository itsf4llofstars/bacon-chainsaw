#!/usr/bin/env python3
"""DOC"""


def main(argv, *args, **kwargs) -> None:
    """main function"""
    if not argv[0] or not len(argv):
        sys.exit()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
