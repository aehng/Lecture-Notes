CS1440 - Friday, January 13 - Lecture 03 - Module 0

# Topics:
* [Announcements](#announcements)
* [Using Git at DuckieCorp](#using-git-at-duckiecorp)


------------------------------------------------------------
# Announcements

## Free Software and Linux Club

*   **What**  Linux Quick Introduction + Install Night
*   **When**  6:30pm Thursday, January 19th
*   **Where** ESLC 053, [FSLC Discord server](https://discord.gg/GKWhbVDN38)

Welcome back, penguins!  This semester FSLC will meet bi-weekly on Thursday nights at 6:30.

Our first meeting on Thursday is perfect if you are curious about Linux or are ready to take the plunge.  Bring your laptop for expert help with choosing and installing the right version of Linux for you.  There is always a risk with installing a new OS, so back up your important files first!

Dates and topics of the next few meetings:

*   Feb 2: "The Good Linux" - a dive into desktop and terminal environments for the user seeking good Linux UX
*   Feb 16: Practicing in Elixir & Erlang by building distributed, scalable, multiplayer terminal games over SSH



# Action Items

*	Call on 2 designated questioners



# [Using Git at DuckieCorp](../../Using_Git/Introduction_to_Git.md)

This is a concept that you will have exercised in the [Shell Tutor](https://gitlab.cs.usu.edu/erik.falor/shell-tutor/).

## Common questions about submitting assignments with Git

*   Can I push my code to another server besides your GitLab?
    *   Yes, as long as it is a **PRIVATE** repository that cannot be found by a search engine or browsing manually.
*   How do I make sure that my code made it to your server?
    *   Follow the instructions in the article **How to Submit Assignments** in the DuckieCorp Employee Handbook on Canvas
*   Is there a better tool to view/edit text files than `nano`?
    *   Yes; `nano` is a lowest-common denominator text editor that you can rely on as a last resort.
    *   You don't have to love it, but it'll be there if you need it.
    *   In this class I don't force you to use any particular program to write your code.  Use whatever makes you happy.
        *   VS Code
        *   PyCharm
        *   Atom
        *   Notepad++
        *   Emacs
        *   Vim
        *   Nano
        *   ~~notepad.exe~~
        *   ...whatever trips your trigger!

### What questions do you have?

*   ...
*   ...


## Using Git to clone these lecture notes

Git makes it easy for you to have your **very own copy** of the lecture notes on your own computer.

This will become important soon when we write code together in class.  It will be nice to have those files on your PC so you can *read*, *run* and *hack* in-class demonstrations.


### Run this once

To get this repository on your computer you will run:

```
$ git clone https://gitlab.cs.usu.edu/erik.falor/sp23-cs1440-lecturenotes
```


### Then, run this once after each lecture

You can keep your copy of the lecture notes up-to-date with these commands:

```
$ cd sp23-cs1440-lecturenotes
$ git pull
```

*   The structure of the files & folders in the repo on your computer is **exactly** the same as the GitLab website.
*   Practice navigating through it in the web UI and your shell using `cd` and `ls`.



