CS1440 - Friday, January 27 - Lecture 08 - Module 1

# Topics:
* [Announcements](#announcements)
* [The REPL is your code lab](#the-repl-is-your-code-lab)
* [How to Run Programs](#how-to-run-programs)
* [What does PyCharm's green "Run" button *really* do?](#what-does-pycharms-green-run-button-really-do)
* [The Current Working Directory and your code](#the-current-working-directory-and-your-code)
* [Python String Operations](#python-string-operations)
* [Reading files in Python](#reading-files-in-python)


------------------------------------------------------------
# Announcements

## Spring STEM Career Fair

*   **What**  The largest on-campus recruiting event of the year
*   **When**  2-6pm Tuesday, January 31st
*   **Where** TSC Lounge

Pre-Register for the fair and research the growing list of employers that will be attending.

https://usu.joinhandshake.com/stu/career_fairs/36881


## Save the Date! BSidesSLC on April 14, 2023

*   **What**  Cybersecurity Conference
*   **When**  Friday, April 14th - Saturday, April 15th
*   **Where** Conference Center at SLCC Miller Campus 9750 S 300 W, Sandy, UT
*   **Web**   https://www.bsidesslc.org/

Save the date! BSidesSLC 2023 coming Friday, April 14th!  Registration to open soon.

BSidesSLC is a non-profit, 501(c)(3) conference focused on cybersecurity. At this conference you can expect to meet & network with industry experts, many of whom are located throughout Utah.

Join members of the Community & Event Organizers on Discord. [Click here for the Discord invite](https://discord.com/invite/hBcnv9gb73?mc_cid=2915d94961&mc_eid=UNIQID).

If you attend the conference I will replace your *lowest* assignment score with *full credit*


# Action Items

*	Call on 2 designated questioners
*   You are in the home stretch of Assignment #1!
    *   Friday: Finish phases 3 and 4
    *   Turn it in early so there is time to fix any mistakes you discover
*	Hold a 3-minute stand-up scrum meeting with your team



# [The REPL is your code lab](../REPL.md)

Were you one of those kids who took devices apart (phones, remote controls, calculators, etc.) to learn how they worked?  And then got in trouble with your parents because you couldn't put them back into working order?

## Precautions

Python's REPL is an awesome way to ![Experiment](./assets/6.experiment.png) **experiment** with a program in a safe environment.  If you take a few precautions, there won't be any left over parts when you're done.

0.  Work within a Git repository so you can easily turn back the clock
    *   We are still a few weeks away from learning how to do this
1.  Copy your code "off to the side" and do your work in that file
    *   This has the advantage of increasing the emotional distance between you and this code
    *   It's easier to break things off if you keep the relationship casual


## Fast code reload

REPLs in some other languages have a convenient command to load/reload a file that you're working on.  Python's REPL doesn't have such a command, but it is easy to fake it with a `while` loop in the shell:

```bash
$ while python -i test.py; do echo Reloading...; sleep .4; done
```

As long as `python -i` exits **normally** this loop continues to restart the REPL.

*   Press `Ctrl-D` or run `exit()` to restart the REPL
    *   This will destroy any new variables or functions that you defined in the REPL.
*   Run `exit(1)` to quit the loop and return to the shell


The REPL in PyCharm (sorry, the *Python Console*) gives you a **Rerun** button (and the hot-key `Ctrl+F5`).


## What does this workflow look like?
 
I am interested in what makes Tic-Tac-Toe's `winner*` functions tick.  Let's bring them into our code lab and see how many extra parts we have at the end.



# [How to Run Programs](../How_to_Run_Programs.md)

Your computer's Graphical User Interface presents a few ways to run a program.  But if you look under the hood, you'll find that there is really only one way to do it.

This document will explain what happens on your computer when a program is launched and what parts the user can control.

Today's code demo:

*   [args.py](./args.py)


## Use what you know

Write a program to print either the *sum* or the *product* of its numeric arguments without crashing.

**Program Requirements**

*   Non-numeric arguments are ignored
*   Whether the sum or product is printed is controlled by the presence of the flags `-sum` or `-product` in the command line
*   It is an error if this flag is not present
*   It is also an error if *both* flags are present



# [What does PyCharm's green "Run" button *really* do?](../CLI_vs_Run_button.md)

It's just another convenient GUI mechanism to run a command line.  Unlike many other GUI program launchers, you have considerable control over the command that is run.

*demo: Set up [`args.py`](./args.py) to be run in PyCharm*



# [The Current Working Directory and your code](../How_to_Run_Programs.md#the-current-working-directory-and-your-code)

Every process running on a computer runs in the context of a directory (a.k.a.
folder) in the file system.  This affects how files are located by your
program.


## Use what you know

Modify [args.py](./args.py) to print the output of `os.getcwd()`.

*   Run the program from your current directory and note what it prints.
*   Go to the parent directory (`cd ..`) and run the program again; this time
    you'll need to give `python` the name of the directory you just came from.
*   Explain any discrepancies between the two runs of this program.



# Python String Operations

*If you know how to work with lists in Python you know how to work on Strings.*

Python's Strings are simply *lists* of characters.


## Practice

Assuming we have a string declared as `s = "Hello, World!"`, what code could you write to perform these tasks?

*   Get the length of the string `s`:
*   Get the 1st character of the string `s`:
*   Get the 3rd character of the string `s`:
*   Get the last character of the string `s`:
*   Change the last character from `!` to `?`:
*   Loop over each character in the string `s`:

See the answers in [string.py](./string.py)



# [Reading files in Python](../Reading_Files.md)

These are **four** basic operations that all programming languages allow you to perform on files.  We'll use **three** of them in this assignment:

* Open
* Read
* Write (we'll do this in a later assignment)
* Close


## Practice

*   Open `README.md` and obtain a file object
*   Print the file object
*   Read the first 10 bytes of the file into a variable
*   Read the next 20 bytes and print immediately
*   Print a few lines of text from the file, one at a time
*   Print until the end of the file using a for loop
*   Close the file object


*Question*: What do you think will happen if you try to **read** from the closed file object?

See the answers in [file.py](./file.py)



