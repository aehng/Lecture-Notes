CS1440 - Wednesday, March 22 - Lecture 27 - Module 4

# Topics:
* [Announcements](#announcements)
* [Code Smells](#code-smells)
* [Reading Code](#reading-code)
* [How will I know when to refactor?](#how-will-i-know-when-to-refactor)
* [Should I refactor *and* add functionality at the same time?](#should-i-refactor-and-add-functionality-at-the-same-time)


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



# [How will I know when to refactor?](../Refactoring.md#how-will-i-know-when-to-refactor)

If software is "grown" and not "built", then refactoring is pruning.

There are two answers to this question:

0.  If you are a **developer** the answer is *"whenever I find a code smell"*
1.  If you are a **project manager** the answer is *"whenever we can afford it"*, which is another way of saying *"never"*



# [Should I refactor *and* add functionality at the same time?](../Refactoring.md#should-i-refactor-and-add-functionality-at-the-same-time)

**No!**



