CS1440 - Friday, March 24 - Lecture 28 - Module 4

# Topics:
* [Announcements](#announcements)
* [The `tkinter` big picture](#the-tkinter-big-picture)
* [Python Code Disasters](#python-code-disasters)


------------------------------------------------------------
# Announcements

## [HackUSU starts this afternoon!!!](https://www.hackusu.com/)

*   **When**  4:00pm Friday, March 24 - Saturday, March 25
*   **Where** Huntsman Hall

Good luck to everyone!


## CyberSentinels CTF Workshop

*   **What**  Practice CTF skills for the National Cyber League competition
*   **When**  7:00pm Tuesday, March 28th
*   **Where** Huntsman Hall 322

This meeting will be to practice cyber capture-the-flag skills in preparation for the National Cyber League competition. Come learn essential tools and tricks that will greatly improve your cybersecurity CTF prowess!


# Action Items

*   *Today* you should finish phase **1. Design** of the assignment
    *   Be ready to move on to phase **2. Implementation** *early next week*
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



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



# [Python Code Disasters](https://github.com/sobolevn/python-code-disasters.git)

Get the code:

```bash
git clone https://github.com/sobolevn/python-code-disasters
```

With your neighbors discuss what you find to be problematic with these examples and why:

*   `python-code-disasters/python/my_first_calculator.py`
*   `python-code-disasters/python/genpassword.py`
*   `python-code-disasters/python/send_email.py`
*   `python-code-disasters/python/sql_bids.py`
*   `python-code-disasters/python/akinator.py`



