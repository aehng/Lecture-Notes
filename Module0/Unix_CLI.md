# Unix command line basics

This document introduces important concepts and terminology, but using the command line is a skill.  Reading alone is not sufficient to learn a skill; you must **do**.  Using the command line effectively is simply a matter of practice.  The very best way to train you would be to sit beside you and talk you through it until you have mastered it.  Since that is not possible, I offer the next best thing, an [automated shell tutorial](https://gitlab.cs.usu.edu/erik.falor/shell-tutor/).

After installing Git on your computer, install and run through this tutorial.  You'll be hacking in no time!


## Table of Contents

*   [Jargon](#jargon)
*   [The Language of the Command Shell](#the-language-of-the-command-shell)
*   [Elementary Shell commands](#elementary-shell-commands)
*   [Changing directories](#changing-directories)
*   [Dotfiles](#dotfiles)


## Jargon

#### Terminal or Console

*   An interactive program which displays and reads textual information to and from a user.
    *   Typically a black screen with white text, or a white screen with black text.
*   A "virtual" terminal is a re-creation in software of a physical device called a "dumb terminal".

![DEC_VT100_terminal.jpg](assets/DEC_VT100_terminal.jpg "A classic DEC VT100 physical terminal")


#### Shell

*   A text-based user interface
*   Accepts commands from a user, checks for syntax errors, then passes them on to the Operating System kernel
    *   Thus, it serves as a layer of protection around the OS kernel, hence the name
*   A shell runs within the context of a terminal; the terminal reads the keyboard and sends the user's text to the shell.  The shell's output is displayed on the terminal's grid of characters.
*   shell **:** terminal **::** webpage **:** browser
*   Two popular shells are **Bash** and **Zsh**


#### Bash

*   `/usr/bin/bash`
*   The **B**ourne **A**gain **SH**ell
*   An evolution of Steve Bourne's original shell program `sh`
*   A flagship Open Source program of the GNU movement
*   The most popular and widespread shell on Linux systems


#### Zsh

*   `/usr/bin/zsh`
*   The Z Shell; no clever meaning, the name just looks cool
*   Inspired by David Korn's influential `ksh`
*   Created by Paul Falstad while studying at Princeton; also open source
*   A popular alternative to `bash`; is now the default shell on Mac OS X


### Which shell should I use?

*   Use whatever is the default on your computer.
*   Syntax-wise, both shells are similar.
    *   Every command you see me run works equally well in both shells.
    *   You won't notice the differences until you become a CLI power-user.
*   I personally prefer `zsh`, but I won't try to convert you ;)


#### Directory

A.K.A. "folder"; a container for files and other directories.


#### Current working directory

The directory a program is currently running in.

Commands that use files and directories will look in the current directory first.


#### Subdirectory

A directory within another directory; a directory that is a "child" of another
directory.


#### Parent directory

The directory that contains a subdirectory.


#### Prompt

Text printed by the shell before the cursor to signal that the shell is ready
to accept your command.

The prompt displays useful information such as the current username, the name
of the computer running the shell, and the shell's current working
directory.


#### Command

An instruction entered by the user to be executed by the shell.

A command may be

0.  The name of an external program installed on the computer
1.  A function that is built-in to the shell and does not exist as a program
    outside of the shell itself
2.  An alias to another command
3.  A keyword that introduces a logical construct such as `if`, `else`, `for`,
    `while`, `until`, `case`, `select`, `function`, etc.

Not all of the commands that you run execute programs that are sitting out on
the hard drive.  Many commands are actually functions built into the shell
itself.  The distinction between external and built-in commands doesn't usually
matter, but remembering that it is there can prevent confusion later.


#### Argument

Extra information given to a command from the command line.

Arguments may refer to objects on a computer system such as the names of files,
directories, user names, or host names.

Sometimes arguments look like integers, floats, or other complicated
structures.  However, they are **always** received by the program as an array
of strings.  It is the program's job to convert argument strings into other
data types when needed.


#### Option (also: Switch, Flag)

A fancy name for an argument that modifies a program's behavior, and that
**does not** represent a file, directory, user name, etc.

In some programs the mere presence or absence of an option is enough to modify
the program's behavior.  These are often referred to as "boolean options" or
"flags", though the former term has long since been abused into being a synonym
for "option".

Some options take arguments of their own.


### A word on "standard" arguments

*   It is a Unix tradition that options begin with a dash `-` or a double-dash `--`
    *   This tradition has been carried over to Microsoft PowerShell
    *   The reason for this is that people *usually* don't give files names starting with `-`
*   In MS-DOS and `cmd.exe` on Windows options start with a front-slash `/`

Over the years much ink has been spilt debating over the *right* way to write command-line arguments.  Should options be short and easy to type?  Should they be long and descriptive?  Many standards have been proposed.  They are all equally invalid.

![XKCD: Standards](./assets/standards.png)


### Common command-line options

Nevertheless, some options mean the same thing to many different programs:

*   `--help` or `-h`
    Print a help message that explains how to use the program
*   `--verbose` or `-v`
    Produce more output than usual
*   `--version`, `-version`, sometimes `-V`
    Report the version number of the program and exit

Look before you leap and read the command's documentation before trusting this list.


## The Language of the Command Shell

The command shell is a simple programming language.  Unlike the other languages
you are familiar with, this language is designed to be fast and easy to type
interactively.

*   Command names tend to be brief
*   Very little punctuation is used
*   There is only one data type: String
*   Ease-of-use shortcuts such as tab completion are built-in to the interpreter

Shell commands follow this syntax:

    command [argument ...]


Commands, like functions in Python, may take arguments.  The square brackets
surrounding `argument ...` in the example above indicate an *optional* portion.
The ellipsis means that there may be more arguments beyond the first one.  All
together, this example means "_command_ takes zero or more arguments".

Unlike Python and Java, parentheses do not surround the argument list and
commas do not separate arguments.  White space separates commands and arguments
from each other.  If one argument needs to contain white space, surround it in
quote marks (either single `'` or double-quotes `"`).

Arguments are given by the shell to the command as a list of *strings*.  It is up
to the command to decide how many arguments it needs as well as the meaning of
each argument.  For example, if an argument should be regarded as an integer,
it is the responsibility of the command to convert that string into its numeric
form.


### Elementary Shell commands

*n.b. These commands are covered in much more depth in the Shell Tutor*

**TASK**                         |  **COMMAND**
---------------------------------|-------------------------------------------
Print arguments to screen        |  `echo [ARG0 ARG1...]`
List files                       |  `ls`
Print file to screen             |  `cat [FILE0 FILE1...]`
Clear the screen                 |  `clear`
Reset the terminal               |  `reset`
View the manual for a command    |  `man COMMAND`
Display the type of a command    |  `type COMMAND`
Copy target file to destination  |  `cp TARGET DEST`
Move target file to destination  |  `mv TARGET DEST`
Delete file(s)                   |  `rm FILE0 [FILE1...]`
Change Directory                 |  `cd [DIR]`
Make a new directory             |  `mkdir DIR0 [DIR1...]`
Remove an empty directory        |  `rmdir DIR0 [DIR1...]` (only works on empty dirs)


## Changing directories

The `cd` command changes your working directory.  In the examples below the '$'
represents your prompt.  Don't type the '$'; type the text that follows.

Go to the "parent folder"; move up one level, leaving the directory you are
presently in

    $ cd ..


_Protip_: The tilde `~` character is shorthand for your home directory.

Return to your home directory regardless of your current location

    $ cd ~

Go to a directory under your home named 'workspace':

    $ cd ~/workspace

You can quickly return to your home by running `cd` with no arguments:

    $ cd


## Dotfiles

Files whose names begin with `.` are ordinarily hidden from file listings in
Unix programs such as `ls`.

    $ ls
    src/  data/  doc/  README.md


This isn't actually a super-13337 way to hide your secrets.  One can simply
give `ls` the `-a` flag to display *ALL* files, even hidden ones.

    $ ls -a
    .  ..  .git/  .gitignore  src/  data/  doc/  README.md


The fact that these files are hidden from view arises from a bug in the first
Unix system.  This bug proved to be a handy way to hide configuration files and
was promoted into a feature.

Dotfiles are configuration files used by many applications on Unix-like
systems.  Dotfiles contain plain text and can be edited with an ordinary text
editor.  Upon startup a Unix application will search for its configuration by
looking for a specific file under a handful of common directories on the
computer.  Reconfiguring a program is as simple as saving a file with the right
name in the right place.  This is in contrast to a centralized, system-wide
settings repository such as the Windows Registry which presents a unified
interface but requires special-purpose software to manage.

Git and SSH are two programs you will use this semester whose behavior is
governed by dotfiles.



### Which dotfile does my shell use?

*   **Zsh** is configured by the file `~/.zshrc`
*   **Bash** is configured by the file `~/.bashrc`

_Fun fact_: The **rc** in the filename stands for *run commands*.  It is another tradition carried over from the early days of computing.  From Brian Kernighan and Dennis Ritchie, as told to Vicki Brown:

> There was a facility that would execute a bunch of commands stored in a file; it was called runcom for "run commands", and the file began to be called "a runcom". rc in Unix is a fossil from that usage.
>
> https://kb.iu.edu/d/abnd


Some people regard **rc** as an abbreviation for "resource", and refer to a program's startup files as *resource files*.



### Which shell am I using?

*   The path of the shell program you are currently running is stored in a variable called `$SHELL`.
*   You can what it says with this command:
    *   ```
        $ echo $SHELL
        ```
*   The important part is the *last word* that you see; it should be either one of `bash` or `zsh`.
    *   If you see something else, contact the instructor.



### Warning: Don't lock yourself out of your shell!

Before I tell you how to add things to your shell's configuration file, I need to warn you that it is possible to render your shell inoperable with a poorly-written dotfile.  The dotfile is one of the first things your shell encounters as it starts up.  A syntax error or bad command can cause the shell to crash before you even have a chance to see the error message.

There is an easy way to avoid this from happening - leave a shell running in one terminal window while you edit your configuration file in another.  That shell is your **lifeboat**.  *Do not exit the lifeboat until you have seen a new shell successfully launch and stay running!*

_Fun fact_: you can play a silly prank on your friends by hiding the `exit` command somewhere in their shells' dotfiles!  I accept no responsibility for what happens to you if you actually try this.


### What to put in your dotfile

You can include any commands that you would like to run upon opening a new terminal.  Anything that you can do at the command line is fair game inside this file.  The commands are run just the same as when you type them yourself.

Just like Python, comments begin with a pound sign `#`.

You can nerf dangerous commands by defining **aliases** that make the shell automatically run the *safe* version of the command when you attempt to run the dangerous one.  For example, the commands `cp`, `mv` and `rm` can destroy or overwrite files without warning.  Each of these commands takes an `-i` option that prompts you for confirmation before doing something permanent.  These aliases cause the shell to add this option when you run these commands:

    # protect me from myself
    alias rm='rm -i'
    alias cp='cp -i'
    alias mv='mv -i'


You'll see me make lots of spelling mistakes at the command line that my computer ignores.  This works with aliases; I *teach* my shell my most common typos so that it knows what I mean:

    # because I don't psell wrods gud...
    alias cs=cd
    alias ecoh=echo
    alias ehco=echo
    alias gti=git
    alias pyhton=python
    alias scd=cd
    alias sl=ls


Your shell can greet you when you log in:

    echo "    .--."
    echo "   |o_o |   Welcome home, $USER"
    echo "   |:_/ |   Right now it is"
    echo "  //   \ \  $(date)"
    echo " (|     | )"
    echo "/'|_   _/'\"
    echo "\___)=(___/"


This my Zsh prompt.  When you copy this, don't leave off the double quotes!

    PROMPT="$ZSH_VERSION %(?..%F{white}%K{red}%?%k%f %S)%B%F{green}%n%f@%F{red}%B%M%f%(?..%s) %~ %# "

One nice thing is that the status code of a failed command shows up in red, and the username and hostname are printed in standout mode.  This makes it more obvious when the previous command doesn't work.

This is my Bash prompt.  It is like the Zsh prompt without the failure code trick:

    PS1="\V \[\e[1;32m\]\u\[\e[0m\]@\[\e[1;31m\]\h\[\e[0m\] \w \$ "



### Creating dotfiles on Windows

Programs following the Unix tradition (e.g. git) still use dotfiles even when
they are modified to run on Windows.  In the Windows OS the concept of "file
extension" is very important, and filenames consisting only of an extension are
regarded as being invalid.  Many native Windows tools will "helpfully" refuse
to save a file without a proper name, rename the file for you, or add another
filename extension (such as `.txt`) to your dotfiles.  These filename changes
will cause Unix-style programs to fail to load their configuration.

The easiest thing to do is to not use Windows tools and instead use the `nano`
editor to manage your dotfiles.  For example, you can control which files `git`
will ignore by editing a dotfile called `.gitignore` using `nano`:

    $ nano .gitconfig


*Updated Wed Jan 11 17:27:11 MST 2023*
