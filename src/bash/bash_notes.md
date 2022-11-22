# Notes For Scripts

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

We will add our path in a manner that has Linux searching in our path first.<br>
Add these lines

