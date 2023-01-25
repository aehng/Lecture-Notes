# How to Run Programs

Your computer's Graphical User Interface presents a few ways to run a program - by clicking an icon, by choosing a menu item, etc.  But if you look under the hood, you'll find that there is really only one way to do it.

This document will explain what happens on your computer when a program is launched and what parts the user can control.

* [Processes vs. Programs](#processes-vs-programs)
* [The Current Working Directory (CWD) and your code](#the-current-working-directory-cwd-and-your-code)
* [Absolute vs. Relative paths](#absolute-vs-relative-paths)
* [Command line arguments and your code](#command-line-arguments-and-your-code)


## Processes vs. Programs

*   A program is code sitting in a file.
*   Once a program has been launched it is called a *process*.
*   Multiple processes can exist that are running the same program.



## The Current Working Directory and your code

#### Current Working Directory (CWD)

The directory a process is running in.

Every process running on a computer runs in the context of a directory (a.k.a.
folder) in the file system.  For some processes it is easy to see what its CWD
is:

*   The shell displays its CWD in its prompt
*   The CWD of a file explorer is the folder that it currently has open
*   For processes with an **Open File** dialog (web browsers, word processors,
    media players) the CWD is often the directory that this dialog opens on.

The CWD governs which files the process can see and how it can access them.

The CWD is inherited by child processes.  This means that when one process (the
parent) starts another process (the child), both processes share the same
current directory.  This explains how the `ls` command works in the shell:

0.  The prompt of the command shell indicates your CWD.
1.  `ls` is the child process of the shell, so its current directory is the
    same as the shell's.
2.  Therefore, `ls` shows what files are in the CWD.


## Absolute vs. Relative paths

Files on a computer are located by their *path*.


#### Path

A string that specifies a location in a hierarchical file system as a sequence of directories leading from the beginning or the "root".

The "root" of the file system differs based on your OS:

*   Unix-derived OSes (Linux, Mac OS) - there is a single root directory is named `/`.  **Every** file and folder is located along a *path* with `/` at its root.
*   Windows - Each disk drive has its own "root" directory.  The name of a root directory combines the *drive letter*, a colon, and a backslash `\`.
    *   Ex. `C:\`, `E:\`


Names of directories and files are separated from each other with a *file separator* character.

#### File Separator

*   The character which delimits directories and files from each other in a path
*   A filename *cannot* contain a file separator character
    *   Windows uses **backslash** `\`
    *   Unix-derived OSes (Linux, Mac OS) use **frontslash** `/`


There are two kinds of paths: **Absolute** and **Relative**.

### Absolute path

A path that contains *absolutely* all of the information needed to locate a file or directory.

An absolute path tells a process how to locate a file anywhere on the system at any time *regardless* of its current working directory.


Examples:

*   `C:\Users\Erik Falor\Desktop\New Text Document.txt`
*   `/home/fadein/1440`


### Relative path

An incomplete path specification which must be combined with a process's CWD to locate a file or directory.

A relative path is added to a process's current directory to form an absolute
path.  This lets a process locate a file in a location relative to its CWD.

Examples:

*   `..\..\Old Text Document.txt`
*   `../data/rot7.txt`


### Laziness and paths

Every time your computer uses a file it **needs** an absolute path.  Because
every process on your computer already has a CWD you are not obligated to
always spell out an absolute path; relative paths are automatically combined
with the CWD for you by the Operating System.


### File path best practices by example

Unless I go out of my way to tell you otherwise, please *never* hard code paths
into your programs.  The reason for this is illustrated below:


#### Bad:

    f = open("C:\\Users\\Mr.CoolGuy\\school\\cs1440\\homeworks\\cs1440-falor-erik-assn4\\data" + sys.argv[1])

*Problem*: This directory doesn't exist on the graders' computers, so your
program will always fail for them.  They must edit your code in order to simply
run the program.


#### Bad:

    f = open("../data/" + sys.argv[1])

*Problem*: This program only works when I launch it from `src/` or some other
sibling directory to `data/`.  The graders must open your program in an editor
to figure out where it's looking for files.


#### Bad:

    filename = input("Gimme the name of a file: ")
    if os.access("../" + filename, os.R_OK):
        f = open("../" + filename)
        for line in f:
            pass
    else:
        print("Unable to access ", filename)

*Problem*: This snippet of code only works when data files are stored at a path
that is up one level from the CWD.  If you run this program from a different
location on the computer it will unexpectedly fail to find its files.

Although this code does check whether a file is accessible before attempting to
open it, it still imposes an expectation about the location of the file on the
user.  While this program won't crash, it also doesn't help the user correct
the problem.  When the user investigates they find that the file indeed exists
at the specified path *and* is accessible.  The error message doesn't indicate
that the program expects to find files in a location relative to where the
program started.  To understand why the program doesn't work as expected the
user is forced to read the source code.


#### Good:

    f = open(sys.argv[1])

*Virtues*: Short and sweet.  Leave the details of where files are to the user,
who knows best.


### Rule of thumb: don't hard-code assumptions about files and directories

Write programs such that the user is fully responsible for specifying the path
to input files.  Your program should *not* encode any information about files
or directories on your computer.  It is too much information (TMI) and makes
your program less portable.



## Command line arguments and your code

Nearly all programming languages present a process's command line arguments as
an array or list of strings.  In Python, arguments are accessible in a list
variable named `sys.argv`.

### `sys.argv`

The process's argument vector (*vector* is a synonym for *array*)

`sys.argv` is a list variable named `argv` located in the `sys` module.  Before
your program can use the `sys.argv` list you must import that module:

```
import sys
```

The zeroth element of `sys.argv` is *always* the name of the command as run
from the command line; the name of the Python program itself.  Any following
elements are the white space-separated words that followed the name of the
command.

Each process on your computer was started as a command line command, even if it
was launched from an Icon or a Menu.  Graphical User Interfaces are simply a
quick way to run commands without typing them out.

This means that every process, regardless of how it was started, has
*something* in its arguments array.


### `sys.argv` is just a list of strings

The arguments vector is truly simple.  Don't overcomplicate things.

*   If you know how lists work, you know enough to use `sys.argv`
*   If you know how strings work, you know enough to use `sys.argv`


### Running programs from the command line

We've been using the `git` command line tool in the Bash command shell.  Bash
is a Unix-style [command line interface](../../Module0/Unix_CLI.md) which gives
users a uniform way to control the operation of a computer system.

Programs started from the command line can be given extra information at the
time they are started in the form of *command line arguments*.  This is
analogous to passing arguments in a function call.


### Use what you know

Write a program to print either the *sum* or the *product* of its numeric arguments without crashing.

**Requirements**

*   Non-numeric arguments are ignored
*   Whether the sum or product is printed is controlled by the presence of the flags `-sum` or `-product` in the command line
*   It is an error if this flag is not present
*   It is also an error if *both* flags are present
