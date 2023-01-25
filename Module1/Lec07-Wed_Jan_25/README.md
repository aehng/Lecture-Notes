CS1440 - Wednesday, January 25 - Lecture 07 - Module 1

# Topics:
* [Announcements](#announcements)
* [The Read, Eval, Print, Loop (REPL)](#the-read-eval-print-loop-repl)
* [What is an IDE?](#what-is-an-ide)
* [Coding by context menu (and other IDE pitfalls)](#coding-by-context-menu-and-other-ide-pitfalls)


------------------------------------------------------------
# Announcements

## [HackUSU](https://www.hackusu.com/) Registration is Open

*   **What**  Register your team for the biggest nerd event of the year!!!
*   **When**  March 24th - 25th
*   **Where** https://hackusu.com

Build a software or hardware project to compete against other teams. All college students and high school seniors are invited!


# Action Items

*	Call on 2 designated questioners
*   You are ready to write/change code for Assignment #1
    *   Today: Phases 2 and 3
    *   Thursday: Phase 3
    *   Friday: Phases 3 and 4
*	Hold a 3-minute stand-up scrum meeting with your team



# [The Read, Eval, Print, Loop (REPL)](../REPL.md)

The command shell and Python's REPL share a lot in common.  Tricks you learn in one (i.e. shortcut keys, tab completion) work in the other.

## TL;DR

When in doubt, remember to use these two important functions in the REPL
whenever you need a hint:

*   `help()`
*   `dir()`



# [What is an IDE?](../What_is_an_IDE.md)

*   Open the starter code as a 'project' and not individual files within it
*   You can have one project open per PyCharm window
    *   You may need to close the currently opened project before switching over to a new one
*   Unless you are already experienced with Git, avoid using PyCharm's built-in Git tool
    *   At this point in your learning you're much more likely to get yourself into trouble with it than without



# Coding by context menu (and other IDE pitfalls)

*   What does PyCharm make of this program?
*   Are PyCharm's suggestions helpful or harmful?

```python
# main.py
class main:
    def __init__(self):
        self.state = "I'm a little confused..."

    def main(self):
        print(r)
        print(n)
        print(q)
        print(self.naem)

    if __name__ == "__main__":
        main(self)
```

As a rule, **the graders and I do NOT run your code in PyCharm**.

*   We will never see the squiggles
*   We don't judge your code by its squiggles
*   At DuckieCorp, it is more important for your code to run from the command line than to be squiggle-free in PyCharm
    *   Eventually you will learn enough about the Python language to understand what PyCharm is trying to tell you
    *   Until then, take its suggestions with a grain of salt
    *   At this stage Python's error messages (i.e. the ones that come up when you run your program) are a better guide


## Who is in charge here?

Don't bend over backwards to appease PyCharm.  It isn't as smart as you think it is.  Don't forget that *you* are the human.

*   If your program runs without emitting error messages, you can ignore the red and yellow squiggles in the editor window
    *   Often they are **not** indicators of problems in your code
    *   Most of them arise from a PyCharm misconfiguration
    *   The rest are false positives
*   In any case, you need to use your noggin to fix code problems

Students who think they are fixing "problems" pointed out by PyCharm just introduce worse bugs.  Eradicating a squiggle without really understanding its cause is [Cargo Cult
Programming](https://blog.ndepend.com/cargo-cult-programming/)



## Improper PyCharm project setup

At DuckieCorp, our software projects follow a standard file organization convention.

*   Source code belongs in a directory named `src`
*   My instructions to you belong under `instructions`
*   Your documentation goes under `doc`

PyCharm *may* assume that source code belongs in the *root* of the project (this was certainly the case in older versions, recent versions may not have this quirk).  If this is the case, PyCharm will think that Python files found under the `src/` folder belong to a package named `src`, and will suggest that you modify `import` statements to match this scheme.  **Don't do it!**

*   The starter code isn't broken.  PyCharm just made a bad suggestion.
*   Teach PyCharm where we keep our code at DuckieCorp.
    *   Right click the `src/` folder in the Project tree and *Mark directory as* **sources root**.
    *   **Never** modify a starter-code import statement to begin with `src.`



