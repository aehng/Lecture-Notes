# Redirect a program's output with the shell

A common question students have about Assignment #1 is "why don't the Text Tools create output files?"

It seems that the capability of combining many files into a single one would be an obvious feature of the `cat` text tool, yet it can only print output to the console.

The reason that your text tools can't create output files is that they don't need to.  The shell is able to take output produced by a command-line program and *redirect* it into a file instead of the screen.

## Table of Contents

*   [Terminology](#terminology)
*   [Redirect standard output into a new file with `>`](#redirect-standard-output-into-a-new-file-with-)
*   [Appending standard output into an existing file with `>>`](#appending-standard-output-into-an-existing-file-with-)
*   [Redirecting standard output to a file *and* the console at the same time](#redirecting-standard-output-to-a-file-and-the-console-at-the-same-time)
*   [In summary](#in-summary)


## Terminology

### Standard Input (`STDIN`)

*   The default source of a command line program's input received by calling such functions as `input()` in Python or by using `System.in.read()` or `Scanner(System.in)` in Java
*   Ordinarily `STDIN` comes from the terminal's keyboard
    *   Identified as a process's **0th** open file on most operating systems
*   Can be changed by the shell to be a file or another program


### Standard Output (`STDOUT`)

*   The default destination of a command line program's ordinary output produced by calling such functions as `print()` in Python or `System.out.println()` in Java
*   Ordinarily, `STDOUT` goes to the terminal's screen
    *   Identified as a process's **1st** open file on most operating systems
*   Can be changed by the shell to be a file or another program


### Standard Error (`STDERR`)

*   The default destination of a command line program's error messages output produced by calling such functions as `print(..., file=sys.stderr)` in Python or `System.err.println()` in Java
*   Ordinarily, `STDERR` goes to the terminal's screen
    *   Identified as a process's **2nd** open file on most operating systems
*   Can be changed by the shell to be a file or another program



## Redirect standard output into a new file with `>`

`>` is the output redirection operator.  When it appears in a command line the
shell will create a new file *or* overwrite an existing file with whatever a
program emits on its standard output.

Command lines using redirection have this form:

    $ command [argument ...] [> filename]


The output goes into a newly-created file called `filename` instead of the
console.  You won't see the ordinary output of `command`, though error messages
written to `STDOUT` may still be printed on the console.

You don't have to do anything special in your code to handle the `> filename`
that appears on the command line.  The shell will remove this from the argument
list before your program begins.


### Examples

Now the `cat` text tool can create one big file out of many:

```
$ python src/tt.py cat data/names8 data/ages8 data/colors8 data/verbs8 > data/long
$ python src/tt.py wc data/names8 data/ages8 data/colors8 data/verbs8 data/long
     9	     9	    70	data/names8
     9	     9	    28	data/ages8
     9	    17	   113	data/colors8
     9	    10	    67	data/verbs8
    36	    45	   278	data/long
    72	    90	   556	total
```

Use `grep` to trim the `data/long` file down such that it contains only lines
of text containing the letter `e`, redirecting these lines into a new file.

```
$ python src/tt.py grep e data/long > data/trimmed
```

With another command you can overwrite `data/trimmed` and replace its
contents with lines containing the letter `a`:

```
$ python src/tt.py grep a data/long > data/trimmed
```


## Appending standard output into an existing file with `>>`

The `>>` operator appends output to a file instead of overwriting it.

    $ command [argument ...] [>> filename]


If the output file doesn't exist the shell will create it.  

Use `>>` to build up a large file by running multiple commands separately.


### Examples

You can use `grep` a few more times to append lines from `data/long` into
`data/trimmed` which contain the other vowels, building a larger file each
time:

```
$ python src/tt.py grep e data/long >> data/trimmed
$ python src/tt.py grep i data/long >> data/trimmed
$ python src/tt.py grep o data/long >> data/trimmed
$ python src/tt.py grep u data/long >> data/trimmed
```


## Redirecting standard output to a file *and* the console at the same time

If you want a process's `STDOUT` to be directed to a file *and* the console at
the same time, you simply think like a plumber and add a `tee` to the flow.

The pipe operator `|` redirects standard output from one program to
become the standard input of another program.

The Unix program `tee` copies its `STDIN` to both the console (its `STDOUT`)
and a file named as its argument:

    $ command [argument ...] | tee output.txt

`tee` is a standard tool in Linux and Mac, and is installed with Git+Bash on Windows, so you can try this today:

    $ grep o data/long | tee data/only-o

When your own `grep` tool is finished, you will be able to substitute it for the "real" `grep`:

    $ python src/tt.py grep o data/long | tee data/only-o


## In summary

*   The redirection operator `>` sends a program's `STDOUT` to a file
*   The pipe operator `|` sends a program's `STDOUT` to another program's `STDIN`
*   The `tee` program copies its `STDIN` to two outputs: the console (`STDOUT`) *and* a file named by its argument
