CS1440 - Monday, March 27 - Lecture 29 - Module 5

# Topics:
* [Announcements](#announcements)
* [What is Object-Oriented Programming?](#what-is-object-oriented-programming)
* [Classification](#classification)
* [The Four Principles of Object-Oriented Design](#the-four-principles-of-object-oriented-design)
* [0. Encapsulation applied](#0-encapsulation-applied)


------------------------------------------------------------
# Announcements

## Assigned Reading: "No Silver Bullet"

*   Read the essay "No Silver Bullet", chapter 16 of the book "The Mythical Man-Month" before our meeting on Friday, March 31st and be prepared to discuss it.
*   Instructions for accessing the electronic version of this book are [here](../../Required_Reading_Schedule.md#accessing-the-mythical-man-month-for-free-through-the-usu-library)


## CyberSentinels CTF Workshop

*   **What**  Practice CTF skills for the National Cyber League competition
*   **When**  7:00pm Tuesday, March 28th
*   **Where** Huntsman Hall 322

This meeting will be to practice cyber capture-the-flag skills in preparation for the National Cyber League competition. Come learn essential tools and tricks that will greatly improve your cybersecurity CTF prowess!


## DC435 Meeting Next Week

*   **What**  T-Pot Honeypot by Allen Hill
*   **When**  7:00pm Thursday, April 6th
*   **Where** Bridgerland Technical College (1301 N 600 W, Logan)
    *   Room 840
*   [Discord](https://discord.dc435.org/)


# Action Items

*   Work on phase **2. Implementation** of this assignment *today* with the goal to complete it *tomorrow*
    *   Begin phase **3. Testing and Debugging** ASAP so you can identify and fix any problems with your assignment
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# [What is Object-Oriented Programming?](../Four_Principles_of_OO_Design.md#what-is-object-oriented-programming)

Object-Oriented Programming (OOP) is the dominant programming paradigm in use today.



# [Classification](../Four_Principles_of_OO_Design.md#Classification)

Object-Oriented programming languages are distinguished by possessing a concept
called _class_ which enables a programmer to express high-level human concepts
to a computer.



# The Four Principles of Object-Oriented Design

Assignment 5.1 is all about leveraging the advantages of OOP to our benefit.

Once you have a cleaned-up, modular version of the Fractal Visualizer you can
apply good principles of object-oriented design to take this program to the
next level.

At the end of this assignment you will have a very impressive program that is
extensible.  In fact, it will be so easy to extend this program to create new
images that you will want to tinker on it well beyond the due date!

The four principles of Object-Oriented Design are:

0. Encapsulation
1. Abstraction
2. Inheritance
3. Polymorphism



# [0. Encapsulation applied](../Four_Principles_of_OO_Design.md#0-encapsulation)

In [Sequences](./Sequences/) is a simple CLI program that prints out sequences
of numbers.  Our old friend FizzBuzz is there, along with the Fibonacci
sequence and the Pell sequences.

The code in this directory is not encapsulated.  The problem is not only is
everything mushed into one file, but that there is no separation among global
variables.  Apart from the care taken on my part there is preventing the `Fib`
part of this program from trampling all over `Pell`'s special constants.

Let's apply the principle of Encapsulation to this code and erect some fences
to keep these neighbors on good terms.



