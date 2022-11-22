#!/usr/bin/env bash
#
# archive_dotfiles.sh Version: 0.1.0
#
# A simple script to archive user listed config files, and or regular
# files. This file can be used manualy or setup as a cron job. You will need
# to populate the DOTFILES array with the files of your choice.
# This file should be used as an anacron with additional changes, an anacron
# will follow.
# This script has not been tested.

# Exit at first error (not needed)
set -e

# Array of files to be archived. Change as needed. Don't add the first file for
# the archive to this list. See documentation below for initial tar file
# creation.
DOTFILES=(.bashrc .bash_aliases .nanorc .gitconfig .tmux.conf)

# Check if folder exists, create it if it does not. You may wish to change the
# safehouse directory name.
if [ d "$HOME"/safehouse ]; then
        # Check if old archive file exists and delete it if it does
        if [ -f "$HOME"/safehouse/dotfiles.tar ]; then
                rm "$HOME"/safehouse/dotfiles.tar
        fi
elif [ ! -d "$HOME"/safehouse ]; then
        mkdir "$HOME"/safehouse
fi

# Create the initial tar file, after this we will append the files from the
# DOTFILES array.
tar --create --file "$HOME"/safehouse/dotfiles.tar "$HOME"/.vimrc > \
        /dev/null 2>&1

# Append additional files form the DOTFILES array, to the tar file
for FILE in "${DOTFILES[@]}"; do
        tar --append --file "$HOME"/safehouse/dotfiles.tar "$HOME"/"$FILE" > \
                /dev/null 2>&1
done

# Log the script run if you want, log directory must exists. You may want or
# need to change both the logfiles directory and log file name.
if [ -d "$HOME"/logfiles ]; then
        if [ -f "$HOME"/logfiles/null.log ]; then
                printf "%s %s\n" "$(date +'%Y-%m-%dT%H:%M:%S%z')" "$0" >> \
                        "$HOME"/logfiles/null.log 2>&1
        fi
fi

# exit the script
exit

