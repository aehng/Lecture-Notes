# What is an IDE?

There are two broad (and fuzzy) categories into which the program you write your code may fall:

0.  Integrated Development Environment
1.  Text editor


**Important**!  Discussion of this topic must *not* be construed as a rule or
requirement for this class.  I am not particularly concerned with how you write
your code, provided that it

0.  Runs on the approved versions of Python
1.  Is written honestly 

It is a goal of this class to teach you how to use real-world tools and an IDE
is *the* primary tool for most professionals.  My demonstration of PyCharm is
not an endorsement for its use, nor are you required to use PyCharm or any IDE.


## Table of Contents

*   [IDEs vs. Editors](#ides-vs-editors)
*   [Advantages of IDEs](#advantages-of-ides)
*   [Advantages of Text Editors](#advantages-of-text-editors)
*   [It's your choice](#its-your-choice)
*   [Further reading](#further-reading)


This article gives a good overview of the differences between them:

*   [Migrating from Text Editors](https://www.jetbrains.com/help/pycharm/migrating-from-text-editors.html)

## IDEs vs. Editors

An editor is a program for authoring files.  An IDE is a big program that integrates several tools together; a text editor is but one tool among many offered by an IDE.

#### Integrated Development Environments (IDEs)

> An integrated development environment (IDE) is a software application that
> provides comprehensive facilities to computer programmers for software
> development. An IDE normally consists of a source code editor, build
> automation tools, and a debugger.
> 
> The boundary between an integrated development environment and other parts of
> the broader software development environment is not well-defined. 
>
> [Wikipedia](https://en.wikipedia.org/wiki/Integrated_development_environment)


Most IDEs combine these tools into one program:

0.  A *programmer's* text-editor featuring
    *   Syntax highlighting
    *   Automatic indentation and formatting
    *   Error detection/correction
    *   Language-aware search-and-replace
    *   Autocompletion
1.  Project organization and file management
2.  An integrated debugger
    *   Runs the program under development in a special debug mode
    *   Set break points
    *   Data inspection
    *   View the process's call stack
    *   Inspect different threads of execution
3.  Version control
    *   Add, commit and push your code at the click of a button
    *   Initialize and clone new projects
    *   Unified interface to several VCS's: Git, Mercurial, SVN, CVS...
4.  Automated testing
    *   Run unit tests
    *   Run integration tests
    *   Navigable test results - jump straight to broken code
5.  Build-system 
    *   Compile a large a project
    *   Recompile only changed files
    *   Bundle the built project into archive files, installers
    *   Code signing
6.  Package management
    *   Search for and install plugins for the IDE itself
    *   Search for and install plugins for the programming project/language
7.  Database Administration
    *   Manage connections to external data sources
    *   Create new databases
    *   Restore testing databases
8.  ... And so much more!
    *   Mail client
    *   Team chat
    *   Kitchen sink integration
    *   Tweet your latest bugfix

IDEs may include other features that make sense for that environment.


## Advantages of IDEs:

*   **Language-specific tools**: more helpful and insightful than tools which
    perform string-based operations.  So much so that the culture of some
    programming languages is such that the language itself is virtually
    inseperable from its IDE
*   **One-program-for-everything**: you need only learn one interface, one set of
    shortcut keys, one menu layout, etc. 
*   **Promotes laziness (the good kind)**: the tool frees you from repetitive,
    tedious and error-prone tasks
*   **It just works**: you have no need to cobble together several disjoint
    programs which were not designed to work together.  The tools in an IDE are
    made to fit together.


## Advantages of Text Editors:

*   **Programming language-agnostic**: works equally well between different
    programming languages, especially new and less-popular languages which do
    not have a dedicated IDE.
*   **Flexibility**: gives you control/responsibility over configuration
    choices.
*   **IDEs can promote the bad kind of laziness**: developers become too
    reliant on the IDE and cannot function without it; an editor doesn't rot
    your mind.
*   **Simplicity**: both conceptually simple and technically simple; most text
    editors don't need 2GB of RAM and two minutes to start up in the morning,
    and there is less that can go wrong


## It's your choice...
...don't let anybody else (including me) make up your mind for you.

Programming tools represent a very personal choice, and is the prime example of
a [Religious Issue](http://www.catb.org/jargon/html/R/religious-issues.html).

In fact, hackers' preference among [text editors](http://wiki.c2.com/?EmacsVsVi)
remains one of the longest running
[Holy Wars](http://www.catb.org/jargon/html/H/holy-wars.html) in computing.


### Seriously, just ignore the hype and choose for yourself

Most of you will enjoy PyCharm and some of you will hate it; that's okay.  So
long as your code works, nobody who's opinion matters will judge you for how
you write code.  I think you should try lots of tools for an extended period of
time to discover what works best for you.

Even if you ultimately decide that IDEs are not your thing, it is important
that you know how to use them because the company that you go to work for may
not have as liberal of a stance as DuckieCorp does.  You may be required to use
a particular IDE for certain tasks.

In my experience, a hybrid approach is quite common among coders.  In my career
I kept an IDE around for its excellent debugger even though I felt its text
editor was sub-par.  At all of the shops I've worked at the only way to
correctly build our entire product was to use the IDE's `build` button.  I
wrote my code in Vim and used the IDE to build, test and debug it.



## Further reading

More information that will give background to your understanding of this common tool-of-the-trade

*   [PyCharm IDE Essentials](https://www.jetbrains.com/help/pycharm/general-guidelines.html)
*   [Mastering PyCharm keyboard shortcuts](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html)
*   [Does Visual Studio Rot the Mind?](https://web.archive.org/web/20191005080226/http://www.charlespetzold.com/etc/doesvisualstudiorotthemind.html)
