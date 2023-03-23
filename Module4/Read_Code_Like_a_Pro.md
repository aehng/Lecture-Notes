# Read Code Like a Pro

Software Engineering education gives students the wrong expectation about the importance of writing code.  I don't mean to say that writing code *isn't* important; rather, there are other activities that will consume far more of your time that aren't taught in school.

*   [Why Would I Want To Read Code?](#why-would-i-want-to-read-code)
*   [Why Is Reading Code So Hard?](#why-is-reading-code-so-hard)
*   [Tips For Reading Source Code](#tips-for-reading-source-code)
*   [What Is The Best Order To Read Source Code?](#what-is-the-best-order-to-read-source-code)
*   [Further Reading](#further-reading)


## Why Would I Want To Read Code?

### Reading code written by others will super-charge your education

Compared to how you study natural languages, the way we teach you to write programs is backward.  As Trisha Gee points out

> What is the first thing you do when you learn a programming language?  You write a "Hello, World!" application.  **You write it down!**  You would never do that if you were learning a foreign language.  You don't write down "Buenos dias!".  It's not the first thing you do when you're learning Spanish.  We're always talking about *writing* code; we don't value the skill of *reading* code.
>
> [Trisha Gee: Reading Code Is Harder Than Writing It - SCL Conf 2019](https://youtu.be/zV079g7Irks?t=112)

What is the value of the skill of reading code?  If the only code you ever saw were the programs that you wrote yourself, how on earth could you ever improve?  Through reading code you will learn many techniques, tricks and idioms that would never have occurred to you.  Some of the tricks are good things that you will borrow, and the rest should be shunned.  But all of them will be things that you would not otherwise encounter in textbooks, tutorials or videos.

If you wanted to become a fiction author and write mystery novels, you would be mad to start without first reading a bunch of mysteries.  Being well-read is the mark of the mature, capable author.  Why do programmers think we can ply our trade in a state of semi-literacy?

Perhaps the line of reasoning might go like this: "Programming is different from writing fiction because I can get instant feedback from the computer.  The computer is the only audience that matters".

The truth of the matter is that successful programs are written primarily for a human audience.


### Maybe *want* is a strong word...

Whether you want to do it or not, you will be reading a lot of code as a professional software engineer.

Something that surprised me when I started my first programming job is that we don't actually spend much time creating new code.  Far more effort is spent *maintaining* software (which is a euphemism for fixing problems in the software).  When new code is written, it typically isn't a brand-new product, but rather the addition of a new feature to an existing codebase.  This is especially true for entry-level software engineers; the heavy responsibility for designing and writing a brand-new program is put into more experienced hands.

Whether you role is fixing bugs or improving an existing product, a considerable amount of time will be devoted to *learning* the system.  Only after thoroughly understanding the relevant portions of the codebase will you feel confident enough to change it.  (And don't forget to leave plenty of time afterward for testing your changes!)

There are many ways to learn how a software system works, none of which are commonly taught in a Computer Science curriculum:

*   Reading documentation
    *   Studying UML diagrams
    *   Examining user manuals
    *   Reading technical design documents
*   Working through training materials intended for end-users
*   Running the software and experimenting with its features, capabilities and limitations
*   Consulting more experienced programmers who have worked on it before
*   Talking to end-users about what problems the software helps them solve, and how they interact with it
*   Reading the source code
    *   Reading the software change log
    *   Skimming through the version control history log (e.g. `git log`)

Of these activities, reading source code is perhaps the most challenging, the most time-consuming, and the most important.  At the end of the day, the source code is the *only* written description of the system that you can trust.

As a professional programmer you will spend more time **reading** code than **writing** it.  This is in opposition to the expectation your education is giving you now, where you spend the overwhelming majority of your time writing new programs from scratch.  In his book "Clean Code", Uncle Bob Martin states:

> Indeed, the ratio of time spent reading vs. writing code is well over 10:1. We are *constantly* reading old code as part of the effort to write new code.

My own experience agrees with this ratio.  However, my experience also informs me that many programmers don't follow his advice, and pay the price by writing awful code that gets thrown out, over and over again.


## Why Is Reading Code So Hard?

Your first clue is the fact that we call a program's text **code**, as though our goal in programming is to encrypt a secret.

This is the Quick Sort algorithm described in pseudocode:

```python
function quicksort(array):
    less, equal, greater = three empty arrays
    if length(array) > 1
        pivot := select any element of array
        for each x in array
            if x < pivot then add x to less
            if x = pivot then add x to equal
            if x > pivot then add x to greater
        quicksort(less)
        quicksort(greater)
        array := concatenate(less, equal, greater)
    return array
```

This is what (a part of) Quick Sort looks like in ARM assembly language (ARM is the type of CPU your phone or tablet has):

```nasm
quicksort:
    push {r2-r5,lr}                                   @ save registers
    sub r2,#1                                         @ last item index
    cmp r1,r2                                         @ first > last ?
    bge 100f                                          @ yes -> end
    mov r4,r0                                         @ save r0
    mov r5,r2                                         @ save r2
    bl partition1                                     @ cutting into 2 parts
    mov r2,r0                                         @ index partition
    mov r0,r4                                         @ table address
    bl quicksort                                      @ sort lower part
    add r1,r2,#1                                      @ index begin = index partition + 1
    add r2,r5,#1                                      @ number of elements
    bl quicksort                                      @ sort higter part

 100:                                                 @ end function
    pop {r2-r5,lr}                                    @ restaur  registers
    bx lr                                             @ return

partition1:
    push {r1-r7,lr}                                    @ save registers
    ldr r3,[r0,r2,lsl #2]                              @ load value last index
    mov r4,r1                                          @ init with first index
    mov r5,r1                                          @ init with first index
1:                                                     @ begin loop
    ldr r6,[r0,r5,lsl #2]                              @ load value
    cmp r6,r3                                          @ compare value
    ldrlt r7,[r0,r4,lsl #2]                            @ if < swap value table
    strlt r6,[r0,r4,lsl #2]
    strlt r7,[r0,r5,lsl #2]
    addlt r4,#1                                        @ and increment index 1
    add    r5,#1                                       @ increment index 2
    cmp r5,r2                                          @ end ?
    blt 1b                                             @ no loop
    ldr r7,[r0,r4,lsl #2]                              @ swap value
    str r3,[r0,r4,lsl #2]
    str r7,[r0,r2,lsl #2]
    mov r0,r4                                          @ return index partition
100:
    pop {r1-r7,lr}
    bx lr
```

Makes perfect sense, right?  Back in the day when everybody wrote programs in assembly language, calling your job "coding" was accurate.  This is what Quick Sort looks like in Python:

```python
def quicksort(array):
    less, equal, greater = [], [], []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        less = quicksort(less)
        greater = quicksort(greater)
        array = less + equal + greater
    return array
```

<details>
<summary>Click to see the pseudocode again</summary>

```python
function quicksort(array):
    less, equal, greater = three empty arrays
    if length(array) > 1
        pivot := select any element of array
        for each x in array
            if x < pivot then add x to less
            if x = pivot then add x to equal
            if x > pivot then add x to greater
        quicksort(less)
        quicksort(greater)
        array := concatenate(less, equal, greater)
    return array
```

</details>

Although modern programming languages have come a long way since the "good old days", it's not all sunshine and roses.  These are a few of the challenges that you face when studying a body of code much bigger than "Hello, World".  This is not an exhaustive list.

0.  Code is often written without any regard for a human who may have the misfortune of looking at it again in the future.
    *   Thoughtlessly written code is downright hostile to the reader
1.  Computer code is unlike any other type of writing that you've been trained in
    *   It isn't structured like a reference work
    *   It doesn't flow like prose
    *   Nor is it elegant and full of feeling like poetry
    *   There are many details to keep track of:
        *   Variables (their scope, their values at each point in time)
        *   Modules, classes, functions defined in the project and how they rely upon each other
2.  The program may be written in a programming language that you are not familiar with, presenting you with two large tasks at once:
    1.  Learning an unfamiliar system
    2.  Learning a new programming language
3.  The coding style may hinder your understanding
    *   Every programmer develops their own personal style, and it is highly unlikely that you'll like their style
    *   The authors employ idioms that you have not encountered before
    *   Even if it's written in a language that you know, style differences can make it feel like an entirely new language
    *   Poorly named variables, functions, classes are used throughout
    *   Clumsy formatting slows you down
    *   Distracting comments that are outdated, inaccurate, contradictory
    *   Large chunks of commented out code
4.  The program uses libraries that you've never even heard of...
    *   ...or outdated versions that are drastically different from what you've used
5.  You may be unsure of the purpose of the program
    *   Your mental model of the system does not remotely match the code that is before you
    *   Perhaps you can't figure out how to build & run the program to see how it works
6.  You may not know where to start reading (where does the computer begin execution?)
    *   The flow of the program jumps around a lot, especially across lots and lots of files
    *   The code is disorganized (files/functions/classes are too long)
7.  Lack of (up-to-date) documentation

In short, reading unfamiliar code is a lot of hard work!  The good news is that reading code is a skill that gets stronger with time and experience.


## Tips For Reading Source Code

Over the years I've learned some tricks that have helped me counter the difficulties mentioned above.  If you employ these habits now, you will soon be at home in a big project.

0.  Get the code into a version control system (such as Git) if it isn't already
    *   If it is in version control, skim the messages for commits that affect the part of the program I'm interested in.  Look for important events:
        *   What bugs have been fixed in the part of the program I'm workin on?
        *   What major changes/improvements have occured?
1.  Browse the program's code in an IDE
    *   IDEs have powerful navigation and search capabilities
    *   As much as I love Vim, sometimes I have to break down and use an IDE to take advantage of these tools, especially for a huge program
2.  Identify the main entry point(s)
    *   In some languages (typically the compiled ones), look for a function/method named `main()`
    *   In dynamic languages like Python, Ruby, Perl and JavaScript you'll have to do your best to find files that aren't obviously filling the role of a library or "package"
3.  `grep` the source code for keywords, error message strings, names of important functions and classes
    *   If the program has a GUI, search for text that appears on buttons and controls that you are interested in, then look for the code that is run when you click on it
    *   If the program has a CLI, search for the part of the program that parses the command line arguments, and find the code that handles interesting options
4.  Run the program in the debugger
    *   Step through the main function and learn how the program starts itself up
    *   Set a breakpoint in a part of the program that you are interested in, and run the program, trying to trigger it
    *   Inspect variables to learn what data is available at that point in the program
    *   Read the call stack to learn how the program got there
5.  Run the suite of tests
    *   I prefer *integration tests* to *unit tests* for this purpose
        *   I find that unit tests are too fine-grained to be helpful at the beginning when I'm still getting oriented
        *   Once I have a good grasp on the overall system, unit tests help me understand the expectations of the specific area I will work in
6.  Refactor the code and rewrite it in my own style
    *   I don't do this with the intention of submitting it or even showing it to anybody else
    *   By rewriting it in my own style, I force myself to really think deeply about it
    *   By "fixing" portions that I don't like I come to understand why it was written the way it was
    *   Once I understand it, I revert it back to its original form before doing my *real* work
7.  Change the program in some fun way to put your mental model to the test
    *   If the program has a splash screen, disable it or make it say something different
    *   Make a button pop up a new dialog box when clicked, instead of or in addition to its normal function
    *   Add a new option to a menu, or add a new command-line option
    *   Cause the program to print a new message to prove that line of code was reached
    *   When you are able to reliably make these changes work, you are well on your way to understanding how the whole program works
8.  Take notes and draw diagrams
    *   Make a UML class diagram of the important pieces
    *   Keep track of important classes, functions, variables
9.  Explain that the program does to your rubber ducky
    *   Use your notes and diagrams to make your case
    *   Make predictions about what should happen in certain situations, then test it!
10. Ask an AI Chatbot what the code does
    *   This works best with short passages of code - presently, a Chatbot won't be able to understand an entire program (or even an entire file)
    *   Paste the code into the prompt and ask questions like
        *   "explain this program to me in simple terms"
        *   "translate this program into pseudocode"
        *   "what is the purpose of variable 'X'?"


## What Is The Best Order To Read Source Code?

Source code is not linear like a book that has a first page and a last page.  Its organization is like a hypertext document that, from its a beginning, can go off in any direction and turn back onto itself, and have many different endings.

As such, there are many ways you can read code.  Here are two methods that are on opposite ends of a spectrum.


### Top-Down, depth-first

0.  Find the *main entry-point* (e.g. `main()` in Java, C++, etc., `if __name__ == '__main__'` in Python)
1.  Make note of which libraries are imported
2.  Notice what data types and constants are declared here
3.  Read through the main function once, paying attention to which variables are used and which functions are called
4.  Starting from the first called function, find where it is implemented and repeat this process

[Tutorial: Reading Code](https://www.youtube.com/watch?v=cPVu9AJ8gGw)


### Bottom-Up

0. Find a file or a class that seems interesting to you at the moment.  Quickly read over it until you have a big-picture understanding of what it is meant to accomplish.
1. Scan through each function/method in the file or class looking for "leaf nodes", functions that which call no other functions or which do not call other functions in the project
2. After you have a reasonable understanding of the fine details of the system, back up and look for higher-level functions which call the lower-level functions
3. Proceed until your understanding of the fine details meets up with the big-picture understanding you got in the 1st step



## Further Reading

* http://wiki.c2.com/?TipsForReadingCode
* http://wiki.c2.com/?ReadGreatPrograms
* https://selftaughtcoders.com/how-to-quickly-and-effectively-read-other-peoples-code/
* https://blogs.msdn.microsoft.com/alfredth/2012/08/16/how-to-read-code/
* https://github.com/aredridel/how-to-read-code/blob/master/how-to-read-code.md


*Updated Thu Mar 23 12:09:36 MDT 2023*
