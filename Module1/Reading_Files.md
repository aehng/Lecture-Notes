# Reading files in Python

[Python tutorial section 7.2](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)


Many of the programs we'll be writing this semester will take as command-line arguments names of files that your program must process.

These are **four** basic operations that all programming languages allow you to perform on files.  We'll use **three** of them in this assignment:

* Open
* Read
* Write (we'll do this in a later assignment)
* Close


## `f = open()`

The `open()` function takes a file's name as a string and returns a **file object**.  The file object (which I named `f`) represents the file itself and, through it, we may perform the other file operations.

There are actually other arguments that you may give `open()`, but they are all optional and their default values are suitable for our needs.  If you're curious, you can learn more about them with the `help()` function.

When there is a problem opening the file named by the argument, `open()` raises an error which can terminate your program.  There are essentially two approaches you can take to errors:

0.  *Look Before You Leap*
    *   Avoid trouble by detecting possible problems before performing a risky operation.
1.  *It's Easier To Ask Forgiveness Than To Get Permission*
    *   Jump in with both feet and worry about the consequences later.
        *   It may be acceptable to let the program crash in the face of some problems.
        *   Or, your program may attempt to recover from errors as they occur.
    *   Python and other modern programming languages achieved this through a mechanism known as *Exception Handling*.  


### Error Handling Roadmap

*   In Assignment #0 we use the *look before you leap* approach by using the `os.access()` function.
    *   This is appropriate because the DuckieCrypt Decrypter is an *interactive* program which must remain running in the face of errors instead of crashing.
    *   The responsibility of writing a *clear* and *informative* error message in your hands.
    *   Don't overwhelm the user with extraneous details, nor hide critical information from them.  It's a tricky balance to attain!
*   In Assignment #1 you will follow the philosophy that *it's easier to ask forgiveness than to get permission* by letting the program crash in the face of an error.
    *   This best matches the behavior of the classic Unix text processing tools you will be emulating in that assignment.
    *   You don't have to spend time designing error messages because Python already supplies reasonable defaults
*   We'll learn about *handling exceptions* in later assignments.



## `f.read()`

You can read any quantity of data from a file up to the number of bytes
contained therein.  To read a particular number of bytes use the `.read()`
method, passing that number as the argument:

    tenBytes = f.read(10)
    twentyBytes = f.read(20)

It is not an error to try to read beyond the end of the file.  For example, if
you call `f.read(100)` and there are only 30 bytes available, you get those
remaining 30 bytes.

Python keeps a cursor within the file object to remember where you were at the
last time you read from the file.  Each time you call `.read()` this cursor is
advanced automatically until you reach the end of the file.

`.read()` returns the chunk of data as a String value.

When the end-of-file (EOF) is reached `.read()` returns the empty string, which
acts as a **sentinel value**.  This is the *only* time that `.read()` returns
an empty string, and is one way your programs may detect that the end of the
file has been reached.


#### [Sentinel Value](https://en.wikipedia.org/wiki/Sentinel_value)

> A special value in the context of an algorithm whose presence is a condition
> of termination


If you want to *slurp* the entire file into a variable in one go, give
`.read()` an empty argument list *or* a negative number.

*   Using the REPL, can you find a method that allows you to rewind the file to
    the beginning so as to re-read it?



## `f.readline()`

When we know that our file contains lines of text it is more convenient to read it one line at a time.  `.readline()` will read bytes from the file until it reaches an end-of-line (EOL) sequence or EOF.  `.readline()` returns a string which includes the EOL sequence.  As with `.read()`, the `.readline()` method returns an empty string `''` when the EOF is reached.

#### Protip: The EOL sequence varies by system

EOL == `"\n"` on Unix and MacOS 

EOL == `"\r\n"` on Windows

*   How will your program know when it has reached the EOF?  Try this out in the REPL.
*   What happens when you use `.readline()` on a non-text file?  Find a .png or .mp3 file and try it for yourself!
*   Because the string resulting from `.readline()` already contains the EOL sequence, printing it with `print()` causes an extra blank line to appear.  How can you prevent this from happening?


## `f.close()`

Software is limited by the OS in the number of files it can hold open at a time.  Once reached, subsequent calls to `open()` will fail until the number of open files is reduced.

After you are finished using a file it is good programming hygiene to close the file with the file object's `.close()` method.  This is something that I and the graders will be on the lookout for.

*   What is the consequence of not closing files that you are finished with?
*   Is it okay to leave a file open if you are still using it?



## Reading and printing a text file line-by-line

With these concepts we can create a *copy* program which copies a text file from from the disk, line-by-line, to the screen.

    f = open("README.md")
    for line in f:
        print(line, end='')
    f.close()

When you use an opened file object in a Python `for` loop, `.readline()` is *automagically* called for you.  The loop stops iterating when the empty string sentinel value is encountered.  This lets you process a **HUGE** file without needing massive quantities of RAM, provided each line of text in the file isn't unreasonably long.
