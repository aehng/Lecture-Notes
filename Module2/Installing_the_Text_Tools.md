# How to Install Your Text Tools

While you worked on Assignment #2 you ran `tt.py` from the `src/` directory like this:

```bash
$ python tt.py cat ../data/let3
```

This works well enough when the files you want to manipulate are nearby.  But if you want to use your own `head` tool to extract the header line from a CSV file, you might find yourself typing out a long command like this: 

```bash
$ python ../../../cs1440-assn2/src/tt.py head -n 1 ../USA_full/2021.annual.singlefile.csv > header.csv
```

You need to spell out the entire path to `tt.py` because your shell doesn't regard `tt.py` as a first-class citizen.  You don't need to do this for the programs `ls`, `cp`, `mv`, etc. because your shell already knows where to find them.  You will be able to run `tt.py` just like one of those commands if you tell your shell where to find it.


### Add `tt.py` to $PATH in a live shell session

As you learned in Lesson #2 of the Shell Tutor (`2-commands.sh`), `$PATH` is
the environment variable containing a list of directories to search for
programs.  Adding the path containing your copy of `tt.py` enables
your shell to run it just like any other command on your system.

This procedure *temporarily* puts `tt.py` on the search path:

0.  Open the shell.
1.  Change into Assignment #2's `src/` directory, where `tt.py` is located.
2.  Enter this command into the shell *exactly as written here* after the dollar sign `$` (the dollar sign represents your prompt)

```
$ PATH="$PWD:$PATH"
```

**Important!**

*   There should be *no* space around the equals sign `=`.
*   **Double quotes** `"` are used instead of single quotes `'`.  Both kinds of quotes are identical in Python, but they mean different things in the shell.
    *   The double-quotes are needed in case the variable `$PWD` contains spaces.

Until this shell session ends, `tt.py` works just like any program on your computer:

```
$ tt.py
Error: Too few arguments

Python Text Tools Usage:
========================
tt.py cat|tac FILENAME...
    Concatenate and print files in order or in reverse
...
```

If you get an error message, see the troubleshooting tips at the bottom of this document.


### Update $PATH in your shell's startup file

You can make this configuration permanent by adding In order to make your shell
always find `tt.py` after it first starts up you need to add its location to
`$PATH` in the startup file.

*   `~/.zshrc` is Zsh's startup file
*   `~/.bash_profile` is Bash's startup file if you are using **Git for Windows**
*   `~/.bashrc` is Bash's startup file if you are using Bash on Linux or Mac

0.  Open your shell
1.  Change into your project's `src/` directory containing `tt.py`
2.  Run `pwd` to print the absolute path of this directory
3.  Open your shell's startup file in a *proper* text editor (i.e. Nano or Vim, *not* Notepad or Wordpad)
4.  Add this line to the bottom of the file, replacing `<TEXTTOOLS_DIR>` with the absolute path found in step 2
    *   ```
        PATH="<TEXTTOOLS_DIR>:$PATH"
        ```


#### Test it out

0.  Do not close your current shell window!
    *   If you make a syntax error in your shell's startup file, you will not be able to start new shells!
    *   Keeping one open is your "lifeboat" until you can fix it
1.  Open a new shell
2.  Type `tt.py` and press enter.  You should see its usage message and not a "command not found" error



## Troubleshooting

### bash: tt.py: command not found
### zsh: tt.py: command not found

This error indicates either that the directory containing `tt.py` is not
correctly specified in your `PATH`, or the `tt.py` script is not executable.

*   Launch a new Shell and try again.  The shell reads its startup file
    once, and only at startup.  Changes that you make to it don't automatically
    affect instances of the shell that are already running.
*   Double-check the spelling of the path to `tt.py` within your startup file.
    *   The path to `tt.py` should end in `src`.
    *   If the path to `tt.py` on your system contains spaces, make sure it is surrounded by **double-quotes** `"`.
*   You may try entering the `src/` directory of your Assignment 2 project and run this command to mark the file `tt.py` as executable:
    *   ```
        $ chmod +x tt.py
        ```



### No such file or directory

Errors messages containing these words look like the following:

```
/usr/bin/env: 'python3': No such file or directory
```

```
bash: /c/Users/user/Desktop/cs1440-falor-erik-assn2/src/tt.py: /usr/bin/env: bad interpreter: No such file or directory
```

The remedy is to update the shebang line in `tt.py`.  The first line of `tt.py`
looks like this:

```
#!/usr/bin/env python3
```

This line tells the shell which programming language to run the contents
of that file in.  The name "shebang" is short for "hash-bang" and refers to the
first two characters of the file.

The shebang line I provided *should* work for most systems.  When it doesn't,
you'll get one of the above error messages.  If this happens to you, replace
my shebang line with the location of the Python interpreter on your system.

0.  Find your python interpreter by running `which python`.  If you need to
    specifically run your code with `python3`, use `which python3`.
1.  Replace the entire first line of `tt.py` with a new line that begins with
    `#!` followed by the path returned by `which`.  The result will look
    something like this if you're using Git+Bash on Windows:
    `#!/c/Users/user/AppData/Local/Programs/Python/Python39/python`



### Error: stdout is not a tty

If you're a Windows user you may see this error when you try to redirect the
output of `tt.py` to a file instead of the screen.

```
$ python src/tt.py head -n 10 README.md > testfile
stdout is not a tty
```

This error occurs when the Python interpreter is run through a helper program
called `winpty`.  Although you did not type out `winpty`, this helper may be
invoked as part of a command alias for the `python` command.  You can check for
the presence of this alias by running the `alias` shell command.  

```
$ alias python
alias python='winpty python'
```

When you see this output you can temporarily disable the alias in this shell
session with the `unalias` command:

```
$ unalias python
$ python src/tt.py head -n 10 README.md > testfile
```

If `unalias` fixes the problem, you should remove the alias from
`~/.bash_profile`.  You'll need to edit this file in a proper text editor.
Whenever you want to run the Python REPL from the bash shell you'll need to
remember to first type `winpty` before `python` to prevent it from hanging.


If the `alias` command reveals no alias for the `python` command, you can bring
your laptop to the instructor.

```
$ alias python
bash: alias: python: not found
```
