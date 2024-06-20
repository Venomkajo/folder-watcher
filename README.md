# Folder-watcher

### Introduction
A simple python program that checks whether the files or folders in it's directory were modified.
The program checks whether the amount of files and their names are the same as before.
It uses savefile.txt to keep track of files and folders that were in it's directory when it last ran.

### Usage

Run the python file and select an argument.
A - reads and writes to savefile
W - only writes to savefile
R - only reads the savefile without overwriting it, using a temp file

After the program finishes you can input R to run it again.
