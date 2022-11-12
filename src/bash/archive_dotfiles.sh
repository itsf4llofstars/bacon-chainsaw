#!/usr/bin/env bash
# What a simple script to auto archive
# your dotfiles can look like
# Works great as a crontab call, or if you want to
# use as an anacron change the hash-bang line to
#!/bin/sh
# copy file to /etc/cron.[hourly|daily|weekly|monthly]
# do not append the .sh to a file in anacron
# If using in an anacron the full typed out expansion of "$HOME"
# will have to be used as anacron's run as root

# Exit at first error
set -e

# Array of files to be archived
DOTFILES=(.bashrc .bash_aliases .nanorc .gitconfig .tmux.conf)

# Check if folder exists, create it if it does not
if [ ! -d "$HOME"/safehouse ]; then
    mkdir "$HOME"/safehouse
fi

# Delete a previouse tar file if it exists
if [ -f "$HOME"/safehouse/dotfiles.tar ]; then
    rm "$HOME"/safehouse/dotfiles.tar
fi

# Create the initial tar file
tar --create --file "$HOME"/safehouse/dotfiles.tar "$HOME"/.vimrc

# Append additional files to the tar file
for FILE in "${DOTFILES[@]}"; do
    tar --append --file "$HOME"/safehouse/dotfiles.tar "$HOME"/"$FILE"
done

# exit the script
exit
