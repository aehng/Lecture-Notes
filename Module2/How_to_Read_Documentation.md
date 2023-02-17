# How to Read Documentation
**version 1.5.1**

*Three hours of experimentation in the REPL can save you 15 minutes of reading documentation.*


## Introduction

Young Computer Science students imagine that software engineering consists of hours-long coding binges punctuated by Google searches.

The truth is that real programmers spend the largest portion of their time reading; reading code and reading technical documentation.  Although reading will be a huge part of your life as a professional programmer, no formal training on this important skill is offered.  It is assumed that you already know how to carry out research, or that you can pick it up as you go.

The organization and tone of technical documents demands different reading skills than you have used thus far.  Fortunately, these skills will grow strong with practice.  This essay gives you direction in developing these skills.  This is a document that I wish somebody had given me when I was a new programmer.



## Why Should I Read Documentation?

The obvious answer is "because I have a question", and often this is exactly what motivates you.

In a world of search engines and code-completing IDEs you may feel that research is not a good use of your time.  However, if you will spend just a little effort, you will find research to be useful and rewarding.

A programmer in need of answers approaches reading from one of two perspectives:

0.  An "itchy" reader who has an itch that needs to be scratched
1.  A "curious" reader who wants to deepen their understanding

This essay will help you get the most out of your reading in both scenarios.


### An "itchy" reader

Most often you will read documentation to answer a pressing question:

*   "I need to fix this bug ASAP"
*   "Our project is already late but needs one more important feature"

As a student you likely won't write the same program twice.  As a professional each new project will be a little different.  Ours is a fast-paced industry that is constantly changing.  The upside to never-ending novelty is that you won't become bored.  The downside is that it takes a lot of hard work just to keep up.  Are you beginning to understand why programmers spend so much time reading?

Programmers are busy people.  When deadlines are looming your research time competes with the need to push the product out the door.  When you are faced with a new problem and very little time to solve it, you cannot afford to get lost in the wikihole.  Understanding how technical documentation is organized enables you to find what you need to quickly answer the question at hand.

When scratching an itch is your reason to read, you need to:

+   Identify which document to read
+   Locate the right section of the document
+   Quickly convert what you find into working code


### A "curious" reader

You are this reader when you have one of these questions:

*   "I wonder what language this program is written in?"
*   "Why is everybody raving about this new technology?"
*   "Larry's code uses this function all the time.  I can tell it is important.  I wonder what it really does?"

When this describes you, you can afford to take a slower, more careful approach.  You can choose to read what you want.  Relaxed reading rewards you by opening doors that you didn't know existed.

Reading documentation for its own sake probably doesn't sound too fun right now, but once you are done with school and aren't forced to read things you don't care about you will find that your attitude has changed.

The same goes for writing code: the code you write for someone else is never as interesting as the code you write for yourself.  It's likely that your job will require you to work on boring, old programs written in boring, old languages using boring, old frameworks that nobody on the internet wants to talk about anymore.  You deserve to write some exciting code for yourself using the latest, greatest technologies tech influencers are buzzing about.  

But how does one get started in a new language or framework?  A tutorial will help you take your first steps, but after that the project's official documentation is the best way to explore it.  You can learn many new things by exploring APIs that you haven't yet used.  Today's curiosity will answer tomorrow's question.  When a new problem arises you will be able to propose a new solution that hasn't occurred to your peers.

When this is your motivation to read you want to meet these goals:

+   Extract important concepts
+   Learn critical jargon
+   Understand how this technology fits in to the larger picture
+   Identify the gaps in your understanding and find how to fill them



## How (Good) Documentation Is Organized

I put the word "good" in brackets because some documentation is just awful.  As you read more of it you'll come to recognize which is which.  Remember what good organization looks like so the documentation you write doesn't cause grief for others!

Whatever your motivation, knowing how documentation is organized helps you quickly get what you need.  The first thing to understand is that unlike prose or poetry, technical documentation isn't meant to be read in-order from top to bottom.  Documentation is a reference, not a linear story.

A (good) technical document roughly follows this outline:

0.  Introduction
1.  Definitions
2.  Examples
3.  In-Depth Explanation
4.  See Also

The idea behind this organization is to place the most commonly desired information near the top where it is most likely to be noticed.  Usage examples compliment dry explanations and give life to abstract explanations that tend to make one's eyes glaze over.  Links to other related documents are easy to find at the bottom of the document and point to resources that fill the gaps left in this document.

To reiterate, although sections of documentation are usually presented in this order, it **does not** follow that you read them in this order.  Good technical documentation is written to facilitate the quick retrieval of pertinent information.  By all means, skip over sections that are not likely to solve your immediate problem.  You know where to find them when you need them.

Which sections are the most helpful depends upon your motivation for reading the document:


### An "itchy" reader

If you are feeling itchy, make a beeline for the Examples section.  Your question may turn out to be a common one which the author has picked as an example.  Copy & paste what you see and you're done.  Even if your question isn't *exactly* answered with a runnable example, it may be close enough to one of the presented examples.  Combine the concrete usage example with the information in the "In-Depth Explanation" section to triangulate a snippet of code that solves your problem.

In the worst case no examples closely match your situation or no Examples section exists.  Your instinct will be to dive into the "In-Depth Explanation" section and look for something to hold on to.  But before you do that, you should ask yourself "am I sure this is even the right tool?"  Perhaps the reason no examples match your situation is because this program/tool/function/library isn't what you need at all!  Scroll down to the "See Also" section (it's almost always at the bottom) and look for pointers to other documents that may be a better fit.  As you read those documents follow their "See Also" pointers.  

After you chase down enough documents you'll either find exactly what you're looking for or end back up at the beginning.  If you came full circle, you may now read up on the "In-Depth Explanation".  But before you do that, scroll up and scan the "Definitions" section.  Much of what you see in  "In-Depth Explanation" will shoot right over your head unless you have a grip on some of the jargon that the author leans on to get their point across.  You don't need to memorize everything here - just make a mental note of what concepts the author deemed important enough to define.


### A "curious" reader

When you read for your own edification you can afford to go a bit slower and read from top-to-bottom.  It may take a few passes over the document before everything sinks in.  You can always decide if it is worthwhile to re-read the document to deepen your understanding later.

*   The **Introduction** orients you to the purpose of the technology, what problem it intends to solve, etc.
*   **Definitions** prepare you to understand the remainder of the document.
*   **Examples**, paired with the Introduction, clarify the purpose of the
    technology as well as give you an overview of how the technology fits into
    the bigger picture.
*   You'll spend the bulk of time on the **In-Depth Explanation**, but don't get carried away.  You aren't memorizing this for an exam, nor are you being called upon to perform a task.  It's okay if some of the material goes over your head.  What you are seeking is an understanding of the capabilities of the technology.  After reading the doc you can answer questions such as "can this technology perform task X?" "If I need to do X, which functions will I use?".  If all you attain is the knowledge of *where* to turn later on, then you have done enough.
*   If you have further questions or your curiosity is still unquenched, follow up with documents listed under "See Also".



## Why Not Turn to Stack Overflow for All of My Questions?

While Stack Overflow (SO) has succeeded at becoming the go-to resource for most programmers (and is far better than any site that has come before), the overall quality of answers is still lower than what can be had from the official documentation.

The reason is simple: the official documentation was either authored or approved by the creator of the technology.  Anybody with some spare time can post on SO.

Using SO is a bit of a Catch-22: you need it the most before you become an expert.  But until you are an expert you cannot judge the quality of the advice given.

SO uses a merit mechanism to ensure that the best answers float to the top and bad advice sinks to the bottom.  But much of the quality-control work is performed by the sorts of people who spend the most time on SO - folks who aren't yet experts.  Once you finally become an expert you can usually find better ways to spend your time than moderating an internet forum for free.

It is commonly the case that the highest-rated answer is either obsolete or subtly wrong; if the advice solves the immediate problem it may come at the cost of a negative consequence that escapes notice until much later.

All programmers should take SO with a grain of salt.  A good rule of thumb is to not use the top-rated answer and instead read the 2nd highest rated answer.  If that is clearly wrong, proceed to the 3rd or 4th answers.  Fall back to the top answer as a last resort.



## Tips for specific kinds of documentation

In this section I will describe features of two specific types of documentation that you may come across in this course.  I will share some tips that help you get the most out of them and how to best approach them from both reader perspectives.

0.  **Python Programming Language Documentation** describes the syntax of the Python programming language along with its standard library.
1.  **Unix Manual Pages** which document command line tools and the Unix Operating System API in the C programming language.


### 0. Python Programming Language Documentation

Part of Python's amazing success lies in its excellent documentation.  You will not encounter many other programming languages with documentation that is as approachable and comprehensive as Python's.


#### How Is Python Documentation Organized?

Python has two great libraries; one in the interactive Python REPL and one on python.org.  They are slightly different, and each have their place.


##### REPL

Built-in documentation can be had at the REPL.  This documentation is contained in the source code that is installed with Python.  The code you write and import into the REPL is documented as well.

*   You know those paragraph "comments" you were taught to write in CS 1400?  The ones that begin and end with a triple quote `"""`?  Those are not comments but are documentation!
*   A comment that begins with `#` and precedes a class or function definition is also picked up by Python's documentation system.
    *   At minimum, signatures of functions and classes are described
    *   A `/` appearing in a function signature signifies the end of *positional parameters*, a.k.a. the final *required* parameter.
*   A mini Python instruction manual is installed with Python, accessible through the `help()` function.
    *   The in-REPL documentation isn't as easy to read and navigate as the online docs, but it does exactly match *your* version of Python.


##### https://docs.python.org/3/

Beautifully-formatted, searchable and easy-to-navigate documentation exists online.

*   Make sure that you are reading the documentation that matches your installed version.  Look for a drop-down at the top of the page.
*   The main documentation page is divided into a few major sections
    *   **Tutorial** - much of what you learned in CS 1400 covers sections 1 - 9 of the Python tutorial.
        *   An itchy reader won't find this section to be terribly helpful.
        *   However, a curious reader will learn something new.  This section teaches me something new all the time!
    *   **Library Reference** - All modules of the standard library (things you can `import`) are described in great depth.
        *   Built-in functions, constants, data types (classes).
        *   The itchy reader will quickly find out why their snippet of code doesn't behave as expected.  
        *   The curious reader will learn which Python modules they can rely on to be importable on anybody's computer without needing to run `pip`.  Python's built-in debugger, unit test framework and GUI services are described here.
    *   **Language Reference** - thoroughly explains the syntax (form) and semantics (meaning) of Python.
        *   How to write Python code, down to what punctuation is needed, and where.
        *   The structure of a Python program, how variables and scope work
        *   How `import` statements work and where the modules come from.
        *   The itchy reader will find this section to be too dense and may want to skip it.  With just a little bit of patience your questions will find an answer!
    *   **Glossary** - decodes the Python jargon that you read in the rest of the docs.
    *   **Python HOWTOs** - a small collection of recipes that solve specific problems
        *   Unless your problem is very common this section may not be useful.
        *   It doesn't hurt to skim this to make sure you're not missing out.
    *   **FAQs** - frequently asked questions (with answers!)
        *   How do I convert a string to a number?
        *   Why are Python strings immutable?
        *   How do I copy an object in Python?
        *   Why is it called Python?


#### How Do I Read Python Documentation?

##### REPL

*   Accessible through the `help()` function, organized by topic and by functionality.
    *   Topics are looked up by passing `help()` a string parameter
        *   When `help()` is given a keyword as a string (usually as an uppercase string) a special page on that topic is opened.  Try running `help('topics')`.
    *   The functionality of almost any Python value can be looked up by passing it to `help()`.
        *   The only exception are string values, which are treated as names of topics.  To learn about the functionality of string objects run `help(str)`.
        *   Give `help()` an object to look up that object's usage.  For instance, `help([])` brings up the page about lists.
            *   `help()` can take the names of functions and methods.  `help([].reverse)` explains the `.reverse()` methods of lists.
*   Call `help()` with no arguments to open the help utility from the REPL.
    *   You can type the names of available modules, keywords, symbols, or topics to learn more about.
    *   Hit `ENTER` to exit the help utility and return to the ordinary REPL prompt (`>>>`).


##### https://docs.python.org/3/

*   Just point your browser here
    *   Check that you're reading the right version of documentation!


#### Python Documentation for an "Itchy" Reader

*   The REPL is your friend.
*   Learn to use `help()` to look up the docs for modules, classes, methods, built-in functions
*   Write doc strings on your own modules, classes, methods, functions, etc.
    Six months from now when you come back to this project you'll be glad that
    you did!


#### Python Documentation for a "Curious" Reader

*   The built-in `help()` documentation is a good way to begin your exploration
*   Follow up by studying the same topic in the online documentation to complete your understanding
*   Comprehensive examples are often present
*   If you want to become a Python "language lawyer", spend some time in the **Language Reference**.
*   As you read the Python docs you will encounter links labeled *PEP* accompanied by a number.  PEPs are **Python Enhancement Proposals**
    *   A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.
    *   PEPs are the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into Python. The PEP author is responsible for building consensus within the community and documenting dissenting opinions.
    *   https://www.python.org/dev/peps/



### 1. Unix Manual Pages

Beginning Unix users want to know two things:

0.  How to use a command
1.  What commands are available on the system

Man pages can answer both of these questions.  The Unix operating system includes built-in documentation that is accessed from a command-line tool named `man`.  `man` is your interface to this repository of information.

*   The documentation that comes with your system will match the software installed on your system.  Nothing is worse than wasting hours struggling with your code only to realize that the article you've been following does not describe your system.  This trap is especially relevant for users of Linux and Mac.  Both operating systems are types of "Unix" and are superficially similar, with many common commands.  However, the capabilities of these commands vary.  A Mac user reading Linux documentation will be led astray, and vice-versa.
*   If the documentation isn't found on your computer, that feature is likely not installed.
*   The version and capabilities described in the manual exactly matches the software you have available.  When searching online it is easy to find out-of-date documentation.
*   You can answer your questions even when the internet is down.  This is invaluable when you are trying to debug a network issue and can't access the Internet.

Some disadvantages of man pages include

*   The reader is assumed to be an experienced computer user who has an understanding of the C language and the organization of the Unix OS.  
*   Man pages are plain-text, and do not include images or diagrams
*   There are no clickable hyperlinks
*   It is possible (though unlikely) for outdated man pages to be left behind on a system and `man` may bring up the wrong one

Some shortcomings can be addressed by reformatting manual pages as HTML, though not all systems take the trouble to do this.

Once again, it cannot be overstated how cautiously you must regard documentation on the Web.  By Murphy's Law it will not match the software installed on your system.  This is more true when you are in a hurry.


#### How Are Man Pages Organized?

The first level of organization are chapters into which related man pages are collected.  On Linux systems the chapters are 1-9:

1.   Executable programs or shell commands
2.   System calls (functions provided by the kernel)
3.   Library calls (functions within program libraries)
4.   Special files (usually found in /dev)
5.   File formats and conventions, e.g. `/etc/passwd`
6.   Games
7.   Miscellaneous (including macro packages and conventions), e.g. `man(7)`, `groff(7)`
8.   System administration commands (usually only for root)
9.   Kernel routines [Non standard]

Other Unix systems (such as Mac OS X and BSD) follow a similar chapter scheme.

Names of pages are named `manpage(section)`.  For example, the manual page for the `ls` command is called `ls(1)` because it is in section 1.  The manual page for the `sleep` program is called `sleep(1)`; the page describing the C language `sleep()` function is `sleep(3)`.

A manual page consists of several sections.  Conventional section names include:

*   `NAME`
*   `SYNOPSIS`
*   `DESCRIPTION`
*   `OPTIONS`
*   `RETURN VALUE` OR `EXIT STATUS`
*   `ERRORS`
*   `FILES`
*   `BUGS`
*   `EXAMPLE`
*   and `SEE ALSO`.

*N.B. not every manual page contains every section.*


#### How Do I Read a Man Page?

Run `man` followed by the name of a command or function.  The chapters are scanned in order from 1-9, and first page found is opened in a terminal reader.  This poses a problem when more than one section contains a page with the same name.

For instance, both sections 1 and 2 contain a man page named `chmod` describing both a program *and* the OS kernel function written in C.  `man chmod` brings up the documentation for the program (i.e. `chmod(1)`).

To read the page `chmod(2)` give `man` the section number *before* the name of the page: `man 2 chmod`.

To read the named page in *every* section, give `man` the `-a` (*all*) option before the name of the page.  After you close one page the next is opened for you:

```
$ man -a chmod
```


#### Navigating the Pager

On most computers the manual is displayed using the `less(1)` program, the same
that is used to display the Git log.  `less(1)` is a "pager", which is a type of
program that lets your read a long text file in the terminal page by page
(unlike, say, `cat(1)`).

Use these keyboard commands to navigate in the pager:

*   <kbd>k</kbd> or <kbd>Up Arrow</kbd> to scroll up one line
*   <kbd>j</kbd> or <kbd>Down Arrow</kbd> to scroll down one line
*   <kbd>Space</kbd> scrolls down one screenful
*   <kbd>g</kbd> returns to the top of the log
*   <kbd>G</kbd> jumps to the bottom of the log, showing the oldest commit (sometimes you must press <kbd>G</kbd> twice)
*   Press <kbd>/</kbd> followed by a search term and <kbd>Enter</kbd> to find and highlight matches
    *   <kbd>n</kbd> jumps to the next match
    *   <kbd>N</kbd> jumps to the previous match
*   <kbd>q</kbd> or <kbd>:</kbd><kbd>q</kbd> to quit
*   <kbd>h</kbd> to open the help page; press <kbd>q</kbd> to go back to the log


#### Searching Man Pages

Man pages work well when you already know the name of what you're looking for ahead of time.  But what about when you're unsure what you're even looking for?  You're probably thinking "Google it"!  That *can* work, but you must be cautious, lest you find outdated or misleading information.  You can rest assured that the search problem was figured out before internet search engines were a part of every day life.  In fact, the Unix manual comes with its own search engine.  Give the `man` command the `-k` (*keyword*) option followed by a search term:

```
$ man -k chmod
```

If you're feeling fancy, you can say it in French:

```
$ apropos SEARCH_TERM
```


#### Man Pages for an "Itchy" Reader

0.  When you need info in a hurry, make a beeline for the `SYNOPSIS` section.  From this you should be able to tell whether you are in the right place.  It may even contain a brief example of how to use the program/function.
1.  Skim over the `OPTIONS`, looking for anything that resembles your solution.
2.  Scroll down to the `EXAMPLES` section; often what you need to do is such a common thing that there will be code that you can just copy & paste.
3.  If this doesn't look like the right manual page, you might be close.  Go to the very bottom and read the `SEE ALSO` section.  It will list other pages in `manpage(section)` format (e.g. `ls(1)`, `sleep(3)`, etc.).



#### Man Pages for a "Curious" Reader

When reading for exploration's sake you can spend more time on the page in total, though it is wise to break this up into multiple passes.  Remember that a man page isn't a story that should be read from front-to-back in one pass.  You can only absorb so much information at a time.  Read the document in up to three passes, and only read as much as is useful or interesting to you.

0.  A quick skim to get the 10,000 ft. overview.
    *   The same thing an itchy reader would do: read the `SYNOPSIS`, skim the `DESCRIPTION`, `OPTIONS` and `EXAMPLE` sections.
1.  A more careful reading to better understand the capabilities of the program/function.
    *   After this pass you will be able to use this concept in code.  Re-read the `DESCRIPTION` together with the `OPTIONS` until each of the `EXAMPLES` make sense to you.
    *   In `ERRORS` you will learn how and why failure can occur, and what (if anything) can be done to guard against it.
    *   `FILES` will point you to important configuration files, databases, input and output locations.
    *   Pages listed under `SEE ALSO` should be studied as far as you have the need or desire.
2.  A close reading when you are developing code.
    *   The `RETURN VALUE` or `EXIT STATUS` sections will teach you what success and failure look like for this command/function.
    *   `ENVIRONMENT` lists variables that influence the operation of this function/command.
    *   `BUGS` indicates weaknesses or shortcomings to be avoided.
    *   `AUTHORS` are who to contact when *you* find a bug.

*Updated Fri Feb 17 12:38:41 MST 2023*
