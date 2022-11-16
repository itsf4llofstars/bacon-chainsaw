#!/usr/bin/env bash
# A script that the user can create a symbolic
# link in their path to more easly change
# a file's permessions to executable

FILENAME="$1"
EXECUTE=755

if [ "$FILENAME" ]; then
    chmod "$EXECUTE" "$FILENAME"
else
    printf "%s\n" "A command line argument filename is needed."
fi
