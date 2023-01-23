CS1440 - Monday, January 23 - Lecture 06 - Module 0

# Topics:
* [Action Items](#action-items)
* [How to Use the Lecture Notes](#how-to-use-the-lecture-notes)
* [Using Modules for code organization](#using-modules-for-code-organization)
* [Namespace Collision Quiz](#namespace-collision-quiz)


------------------------------------------------------------
# Action Items

*   Take the "Modules and Namespace Collisions" quiz in Canvas **before the next lecture on Wednesday**
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# How to Use the Lecture Notes

*   You should *clone* this lecture notes repository onto your own computer so you always have a copy with you.
*   After it is cloned, use `git pull` to *update* it after every lecture
    *   This way you can read and run the *demo code* that I write with you in class
*   You can also make a convenient study guide called `all_notes.md` by running the `concatenate.sh` script found at the root of the repository
    *   This file is the concatenation of all daily `README.md` files
    *   It does **not** contain other Markdown files from the repository
*   `all_notes.md` can be quickly searched with the `grep` tool to find a keyword you are interested in
    *   The syntax of this command is `grep [options] SEARCH_TERM FILE...`
        *   `[options]` includes:
            *   `-i` ignore case of `SEARCH_TERM`
            *   `-n` display the line number of the match
            *   `-H` display the file name of the match
                *   This is useful when searching multiple files
            *   `--color` highlight the filename, line number and matched search term
            *   `-C N` display `N` lines of context above and below each match


## Demo: clone and search the lecture notes in the shell

0.  Clone the lecture notes onto your computer, and take steps to avoid **Gitception**:
    1.  Run `git status` to see if you're within a repository
    2.  `cd ..`  to climb up to the parent directory
    3.  Repeat until you're clear of danger
    4.  `git clone https://gitlab.cs.usu.edu/erik.falor/sp23-cs1440-lecturenotes.git`
1.  Show each line of `all_notes.md` containing "Module":
    *   `grep Module all_notes.md`
2.  Highlight each use of the word "shell" in 3 lines of context:
    *   `grep --color -C 3 shell all_notes.md`
3.  Highlight each use of the word "Python" with the filename and line number:
    *   `grep --color -n -H Python all_notes.md`
4.  Idem., but ignore case so that both "Python" and "python" are matched:
    *   `grep --color -n -H -i Python all_notes.md`



# Using Modules for code organization

There are 5 Dallins in this class.

If I say "Hey, Dallin!", who will respond?

----

Modular organization is used *everywhere*; pay attention and you'll begin to see it.  For example, this very lecture notes repository is organized modularly.

*   The top level of organization are *modules* that combine topics related to an assignment
    *   Modules contain documents with information that you need to succeed with the upcoming assignment
    *   Modules also hold *lectures*, corresponding to individual lessons
        *   Inside each lecture are notes and code samples 

Understanding this organization helps you to independently find answers to your own questions.


The starter code for Assignment #1 has *thirty-nine* functions jammed into a single file.  Discuss with your study buddies these questions:

*   How can you fact-check Erik's assertion that there are 39 functions defined in `ttt.py`?
*   What are the advantages of putting all of the functions into one file?
*   What are the disadvantages?
*   Why might it become important to separate code into modules as programs grow in length and complexity?


## How to [Organize Code Into Modules](../Organizing_Code_Into_Modules.md)



# Namespace Collision Quiz

When importing identifiers into the current namespace, you must be aware of collisions between *locally* defined identifiers and those defined in the *imported module*.  This quiz teaches you the consequences of carelessly importing things into your programs.

*   The code for the quiz is in the lecture notes repository under **Module 0** in a directory named [../namespace_collision](../namespace_collision) 
*   **This quiz is due before class on the day we discuss the results.  Once class begins the quiz is locked.**
    *   You can take this quiz twice.
    *   It is open book with no time limit, so the 2nd attempt should not be necessary.



