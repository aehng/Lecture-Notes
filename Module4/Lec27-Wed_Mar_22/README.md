CS1440 - Wednesday, March 22 - Lecture 27 - Module 4

# Topics:
* [Announcements](#announcements)
* [Code Smells](#code-smells)
* [Reading Code](#reading-code)
* [The `tkinter` big picture](#the-tkinter-big-picture)


------------------------------------------------------------
# Announcements

## Free Software and Linux Club

*   **What**  Rust: The Most Loved Programming Language Since 2016
*   **When**  6:30pm Thursday, March 23rd
*   **Where** ESLC 053, [FSLC Discord server](https://discord.gg/GKWhbVDN38)

For years the world of systems programming has been dominated by C and C++. If you wanted to write performant software that works tightly with the operating system, these languages were your only real options.

Both languages, however, are deeply flawed. Manual memory management quickly becomes a massive burden and C's refusal to check a single boundary can lead to critical, billion-dollar security issues. C++ has a lot of seemingly nice features but it inherits many ugly problems from C.

That's where Rust comes in: a new(er) systems programming language that promises memory safety without the use of a garbage collector, as well as being a remarkably elegant language that's fun to work with.


## [HackUSU](https://www.hackusu.com/) - Utah's Premiere Collegiate Hackathon

*   **What**  Build a software or hardware project to compete against other teams. All college students and high school seniors are invited!
*   **When**  4:00pm Friday, March 24 - Saturday, March 25
*   **Where** Huntsman Hall


## BSidesSLC Registration is Open!

*   **When**  Friday, April 14th - Saturday, April 15th
*   **Where** Conference Center at SLCC Miller Campus 9750 S 300 W, Sandy, UT
*   [**BSidesSLC Discord**](https://discord.com/invite/hBcnv9gb73).
*   **Cost**  
    *   General Admission $19 + taxes & fees
    *   General Admission + Electronic Badge $119 + taxes & fees
    *   [Tickets](https://www.eventbrite.com/e/bsidesslc-2023-tickets-527264701917)
*   BSidesSLC attendance replaces your lowest assignment/exam score
    *   It is good enough if you can only make it one of the days, either Friday or Saturday


# Action Items

*   You should be ready to start phase **1. Design** of this assignment *today*
    *   Continue your design work through *the end of the week*
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# [Code Smells](../Refactoring.md#code-smells)

> In computer programming, a code smell is any characteristic in the source
> code of a program that possibly indicates a deeper problem.  Determining what
> is and is not a code smell is subjective, and varies by language, developer,
> and development methodology.
>
> -- [Wikipedia](https://en.wikipedia.org/wiki/Code_smell)



# [Reading Code](../Read_Code_Like_a_Pro.md)

**Remember:** Knowing just enough is good enough

It is not actually important that you fully understand how or why the formula
involving `Z` works the way it does; this is a deep subject even for
mathematicians.

Nor do you need a firm grasp on `tkinter` or complex numbers to succeed in this
assignment.  The things that you *must* be able to understand are

*   How to identify the inputs and outputs of a block of code
*   How to identify code that is usefully contributing to the calculation, and removing dead code
*   How to re-arrange code without changing its meaning


## Document your time spent reading code in your Signature and SDP

*   Every software project begins with research.
    *   Research should be documented in phases **0: Requirements Specification** and **1: System Analysis** of your SDP.
    *   Track time spent reading code on your Sprint Signature.
*   Don't forget to reserve plenty of time for testing!
    *   For this assignment you should be doing more testing than ever before.



# The `tkinter` big picture

GUIs in general and `tkinter` in particular are big topics.  The interface of the Assignment 5 program is intentionally very simple so that your lack of knowledge about GUIs doesn't get in your way.

*   You don't need to be a pro at GUIs to complete this assignment.
*   You don't actually need to understand `tkinter` to complete this assignment.
*   When in doubt, *be very careful* around lines of code that deal with the GUI. 
    *   Test the program *often* so you will notice new bugs/crashes/glitches soon after you make them
    *   Use Git *frequently* so you can undo your small mistakes before you get **really** lost

However, many of you won't feel ready to begin until you have some baseline knowledge.  Consider this your `tkinter` crash course.


## How do I pronounce `tkinter`?

`T-K-inter`

*   This is short for "Tk Interface"
*   "Tk" is short for "Tool kit"


## What is the `tkinter` library?

`tkinter` is the standard GUI library for Python.  It is cross-platform and runs equally well on Windows, Mac and Linux.  It ain't pretty, but it works *everywhere*.  Python's `tkinter` library works by standing atop the shoulders of a GUI library written in/for another programming language called Tcl.

> Tk is a graphical user interface toolkit that takes developing desktop
> applications to a higher level than conventional approaches. Tk is the
> standard GUI not only for Tcl, but for many other dynamic languages, and
> can produce rich, native applications that run unchanged across Windows,
> Mac OS X, Linux and more.
>
> https://www.tcl.tk


### Help! The Assignment #5 starter code crashes because `tkinter` is not installed!

There are troubleshooting instructions in the [Assignment 5.0 starter code repository](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn5/-/blob/master/instructions/Tkinter.md).


## `tkinter` basic concepts

0.  `tkinter` GUIs are built from *windows* and *widgets*
    *   The application's main *window* is created by calling the `Tk()` constructor
    *   *Windows* are containers for *widgets*
    *   A typical `tkinter` program creates one main window and *packs* multiple widgets inside of it
1.  *Widgets* are interactive elements such as buttons, sliders, text boxes, menus, and so on
    *   Widgets are created by calling a constructor function named by the type of widget
    *   A widget's constructor must either be imported from the `tkinter` namespace or have its name prefixed by `tkinter.`
    *   Widgets must be *packed* into a visible Window in order to be visible to the user
2.  Once the app's windows and widgets are set up an event loop is entered which runs until the user closes the program
    *   The event loop consists of code that responds to user input events such as button clicks and keypresses
    *   In the `tkinter` framework the event loop is a method called `mainloop()`
        *   `mainloop()` returns when the user closes the application
        *   The application closes when the user closes the window through the window manager (e.g. by clicking the red 'X' button) or by calling the main window's `destroy()` method
3.  Because `tkinter` is focused on windows and widgets, it isn't
    straightforward to draw pictures pixel-by-pixel
    *   The `Canvas` widget can be used to draw lines and simple shapes
    *   A `Canvas` widget is used to display "complex" graphical elements like straight lines, curved arcs, circles, polygons and text
    *   The `turtle` graphics library you used in CS 1400 uses `tkinter`'s `Canvas` widget under the hood
4.  Our Fractal program needs to draw individual pixels instead of straight lines, curved arcs, circles, polygons, etc.
    *   A `PhotoImage` widget, placed inside a `Canvas`, enables us to manipulate individual pixels
    *   The Fractal program writes an entire row of pixels to the window at a time; this makes the program run slightly faster than plotting pixels one at a time


## TkinterDemo.py

[TkinterDemo.py](../TkinterDemo.py) shows what a complete, interactive `tkinter` app looks like.

Let's practice our code-reading skills and try to understand this unfamiliar piece of code.



