# Notes For Scripts

Note: This file is still in a rough draft fromat.

## Script

### change_mod.sh

The change_mod.sh bash script will run the chmod 755 bash command line command.
It will change the permissions of the passed filename to executable.<br>

This is more efficient way of changing a file to executable.  For information
creating a path, and symbolic link see below.<br>

### Creating a Personnal Path

We will first need to create a direcory for our path. It may be best practice<br>
to name such a directory bin. We will create the ~/bin diretory from our<br>
/home/$USER directory.<br>

```bash
$ cd ~
$ mkdir bin

Creates the /home/$USER/bin directory
```

To creat you own personal path we can add a couple of lines our .bashrc file.<br>
Open your .bashrc file with any editor, IDE you wish.<br>

```bash
$ vim ~/.bashrc

opens the .bashrc file
```

We will add our path in a manner that has Linux searching in our path first<br>
before any other path directory. Add these lines to your ~/.bashrc file.<br>

> export PATH="$HOME"/bin:$PATH
> PATH=$PATH:"$HOME"/.local/bin

The second line adds your ~/.local/bin directory to the path as well, but it<br>
adds it in manner that Linux will check it last. The first line is required the<br>
second line is not.<br>

### Create The Symbolic link

We are now going to create the symbolink from our personnal path, to the script<br>
change_mod.sh.<br>

cd into your bin directory, from your home directory you would type:

```bash
$ cd bin

moves into the ~/bin directory
```

We now want to think how to get from where we are, ~/bin, to where the<br>
change_mod.sh file is, using relative paths.. I keep my bash scripts<br>
in a directory called ~/bashscrits. So for me from the ~/bin directory to the<br>
~/bashscritps directory I have to go down one directory ../ and up one directory<br>
to the ~/bashcripts directory. ../bashscripts. To make the link we type:<br>

```bash
~/bin $ ln -s ../bashscritps/change_mod.sh ./mod

~/bin $ ls -lh

mod -> ../bashscripts/change_mod.sh
```

Now when we call mod filename from anywhere in our directory structure, Linux<br>
will see that mod is in the path and call change_mod.sh on the filename. The<br>
filename must be in the same directory from where we call mod.<br>

```bash
~/directory $ mod file.ext

The permission of file.ext are change to wxrw-xw-x
```

