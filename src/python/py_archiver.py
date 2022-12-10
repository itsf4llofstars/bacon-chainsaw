#!/usr/bin/env python3
"""Python3 script that creates an archive (tar file) of user wanted files
"""
import os

path_to_files: str = os.path.expanduser('~')

"""The below list shoudl be populated by the user. If a file is not
int the path, /home/$USER then the path to the file from, /home/$USER
should be used. See files_list[0], ./config/nvim/init.vim for an example.
"""
files_list = [
    ".config/nvim/init.vim",
    ".bashrc",
    ".bash_aliases",
    ".tmux.conf",
    ".gitconfig",
    ".nanorc"
]


def main():
    pass


if __name__ == "__main__":
    import sys

    sys.exit(main())
