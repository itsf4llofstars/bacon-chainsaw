#!/usr/bin/env bash
# A script symbolic link in your path to more easly
# change a file's permessions to executable

FILENAME="$1"
EXECUTE=755

if [ "$FILENAME" ]; then
    printf "OK: %s %s" "$FILENAME" "$EXECUTE"
fi
