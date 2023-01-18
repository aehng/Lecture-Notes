CS1440 - Friday, January 20 - Lecture 05 - Module 0

# Topics:
* [Announcements](#announcements)
* [Stand Up Scrum Meetings](#stand-up-scrum-meetings)
* [How to Report Bugs Effectively](#how-to-report-bugs-effectively)
* [Using Modules for code organization](#using-modules-for-code-organization)
* [Organizing Code Into Modules](#organizing-code-into-modules)
* [Namespace Collision Example](#namespace-collision-example)


------------------------------------------------------------
# Announcements

## Science Unwrapped Tonight

*   **What**  Predicting Snowmageddon: Using Data Science to Design Against Disaster
*   **Who**   Dr. Brennan Bean, USU Department of Mathematics and Statistics
*   **When**  7:00pm Friday, January 20th
*   **Where** ESLC 130

Lots of snow is great for skiers and thirsty reservoirs, but can present a challenge to building designers. How do you build buildings that will safely withstand the weight of snow loads? By collecting and analyzing LOTS of data, and living with a little uncertainty, says USU statistician Brennan Bean, who will discuss the power of data science in a changing climate.

Admission is free

Refreshments and activities after


# Action Items

*	Call on 2 designated questioners



# [Stand Up Scrum Meetings](../Stand_Up.md)

Back in ye olden-times, software projects followed the Waterfall methodology.

DuckieCorp strives to be the kind of agile software shop that employs only the most trendy software development methodologies.  One such methodology is called **Scrum**, in which teams hold a brief meeting on a daily basis to talk about how their work is progressing.  

We will hold stand ups at the beginning of each class period going forward.



# Assigned Reading: [How to Report Bugs Effectively](https://www.chiark.greenend.org.uk/~sgtatham/bugs.html)

Take a few minutes and discuss these questions with your study buddies:

*   What is wrong with saying "it doesn't work"?
*   What problems arise if your description of the bug is unclear?
*   How much information should you provide in a bug report?
*   How can you tell which pieces of information are *too much*?
*   Is it helpful to suggest what you think is going wrong?  Why or why not?


## DuckieCorp Bug Reporting Best-Practices

About half of the bug reports I get from DuckieCorp interns are actually cases of *user error*.  If you follow the advice from the essay you will spare yourself embarrassment.

You will also find that this process sometimes helps you to **solve the problem yourself**.  Instead of merely reporting a problem, you can provide a complete bug **fix**.

In addition to Simon's advice, keep these guidelines in mind at DuckieCorp:

*   It is unfortunate that you are in a frustrating situation
    *   Please remember that we are people, too
    *   Patience and respect should be shown by **both sides** in **all** interactions
*   Double-check that you have been following the instructions **EXACTLY**
    *   If you haven't noticed by now, computers are **VERY** particular about what their input looks like
    *   Pay close attention to *wh ite  sp ace*, *spellign* and *CapPitALiZatIon*
*   Avoid screenshots when possible (see below)
    *   Screenshots should be resorted to only when there is **no other way** to capture details of the problem.  For example, when:
        *   A graphical user interface is broken
        *   Your program outputs a picture, but the image is incorrect
    *   If you *must* send a screenshot, learn how to take a screenshot within your OS instead of snapping a pic of your laptop with your phone
        *   Professors make fun of students who do this
            *   Windows users: press the `Print Screen` key
            *   Linux users: install and run a program called `scrot`; `Print Screen` likely works, too
            *   Mac users:
                *   `Cmd-Shift-3` takes a screenshot the entire screen
                *   `Cmd-Shift-4` select a rectangular region to screenshot
                *   `Cmd-Shift-5` pops up a GUI to help you make a screenshot


### Why are screenshots bad?

Whoever said "a picture is worth a thousand words" never tried to debug a syntax error from a JPEG.  Screenshots are unnecessary 95% of the time.  Consider:

0.  Source code is plain text
1.  Error messages are plain text
2.  Your terminal is plain text

A picture of plain text is a waste of time and bandwidth.  When reporting a bug that is **textual** in nature, it is best to send just **the text itself**.

0.  Here is a screenshot of my desktop.  There is an error message in my Python program in there... somewhere.
    *   ![](./52-too-big.png "A screen shot that is too big")
    *   There's a lot going on here!  How long did it take you to zero in on the error message?
    *   This file costs more than a quarter of a megabyte of storage.  The full-sized version was double that.
    *   Screenshots of your desktop can dox you.  (You ever hear the Tragedy of Kurt Eichenwald the Unwise?  No?  I thought not, it's not a story the Normies would tell you...)
    *   Screenshots of your desktop can dox your coworkers/users/customers.
        *   Be careful with sensitive info that just happens to be on your screen; you could violate HIPPA, FERPA, RFPA, PCI compliance, etc.
        *   Hackers have broken into organizations using information gleaned from photographs & screenshots.
1.  This is a screenshot of *just* the terminal with the Python error
    *   ![](./52-cropped.png "A screenshot cropped just to the window of interest")
    *   This file still takes up an eighth of a megabyte
    *   If I want to find this error message in my inbox again, how do I search for it?  Search tools don't find text embedded in an image.
    *   What if an important clue scrolled off the top of the window?  This image does not hold any extra context about this error.
2.  This is the error message I care about, plus the command that caused it:
    *   ```
        5.8 fadein@voyager2 ~/school/cs1440-assn0/src % python plotter.py
          File "plotter.py", line 11
            print('\x1b[0m|', end='\x1b[1;33m')
                                 ^
        SyntaxError: invalid syntax

        Tutor: It looks like you spelled python3 wrong
        ```
    *   Later, when I search my inbox for `python SyntaxError`, this will come up
    *   This is exactly what I need to diagnose the problem, told in only `238` bytes.  This is orders of magnitude less than `144,031` or `285,944` bytes.
    *   You could scroll up in the terminal and copy more text to provide more context about the problem.  Many screenfuls of text weigh less than one picture.



# Using Modules for code organization

Modular organization is used *everywhere*; pay attention and you'll begin to see it.  For example, this very lecture notes repository is organized modularly.

*   The top level of organization are *modules* that combine topics related to an assignment
    *   Modules contain documents with information that you need to succeed with the upcoming assignment
    *   Modules also hold *lectures*, corresponding to individual lessons
        *   Inside each lecture are notes and code samples 

Understanding this organization helps you to independently find answers to your own questions.

*   You should *clone* this lecture notes repository onto your own computer so you always have a copy with you.
    *   `$ git clone https://gitlab.cs.usu.edu/erik.falor/sp23-cs1440-lecturenotes.git`
*   After it is cloned, use `git pull` to *update* it after every lecture
    *   `$ git pull`
    *   This way you can read and run the programs that I write with you in class
*   You can also make a convenient study guide called `all_notes.md` with the `concatenate.sh` script provided for you
    *   The `all_notes.md` study guide can be quickly searched with the `grep` tool to find a keyword you are interested in

*Demo: clone and search the notes in the shell*


## Modules are good for programs, too

The starter code for Assignment #2 has *ten* functions spread over *eight* files.  I could have put everything into one file.  Discuss with your study buddies these questions:

*   Why do you think I organized the Assignment 2 starter code as I did?
*   What are the advantages of having your functions all together in one file?
*   What are the advantages of having your functions separated into different files?

As your programs grow in length and complexity it becomes important to separate your code into modules.  This grows out of practicing the problem-solving techniques of ![Dividing the Problem](../../Module0/assets/1.divide_the_problem.png) **Dividing the Problem** and ![Don't get Frustrated](../../Module0/assets/7.dont_get_frustrated.png) **Not Getting Frustrated**.



# [Organizing Code Into Modules](../Organizing_Code_Into_Modules.md)

There are 5 Dallins in this class.

If I say "Hey, Dallin!", who will respond?



# Namespace Collision Example

When importing identifiers into the current namespace, be aware of collisions
between locally defined identifiers and those from the imported module.

See the code in the directory [../namespace_collision](../namespace_collision)



