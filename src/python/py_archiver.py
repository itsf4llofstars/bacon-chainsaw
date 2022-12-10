#!/usr/bin/env python3
"""Python3 script that creates an archive (tar file) of user wanted files
"""
import os
import shutil
# shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])

PATH_TO_FILES: str = os.path.expanduser('~')

"""The below list should be populated by the user. If a file is not
int the path, /home/$USER then the path to the file from, /home/$USER
should be used. See FILES_LIST[0], ./config/nvim/init.vim for an example.
"""
FILES_LIST = (
    ".config/nvim/init.vim",
    ".bashrc",
    ".bash_aliases",
    ".tmux.conf",
    ".gitconfig",
    ".nanorc"
)


def main():
    # Check PATH_TO_FILES
    print(PATH_TO_FILES)

    # Check files list
    for filename in FILES_LIST:
        print(os.path.join(PATH_TO_FILES, filename))
    print()

    base_name: str = os.path.join(PATH_TO_FILES, "foobar", "test_tar")
    root_dir: str = os.path.join(PATH_TO_FILES, "ed")
    shutil.make_archive(base_name, "tar", root_dir)


if __name__ == "__main__":
    import sys

    sys.exit(main())
