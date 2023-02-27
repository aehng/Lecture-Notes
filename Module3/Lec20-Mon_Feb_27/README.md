CS1440 - Monday, February 27 - Lecture 20 - Module 3

# Topics:
* [Announcements](#announcements)
* [Introduce Assignment #4: Bingo! UML Design](#introduce-assignment-4-bingo-uml-design)
* [Retrospective: Assignment #3](#retrospective-assignment-3)
* [What you need to gain from assignments](#what-you-need-to-gain-from-assignments)
* [A solution to Assignment #3](#a-solution-to-assignment-3)
* [UML: Multiplicity Constraints](#uml-multiplicity-constraints)
* [UML: Inheritance ("is a" relationships)](#uml-inheritance-is-a-relationships)
* [Real-world UML class diagrams](#real-world-uml-class-diagrams)


------------------------------------------------------------
# Announcements

## Assigned Reading: "Passing the Word"

*   Read the essay "Passing the Word" (Chapter 6) of the book "The Mythical Man-Month" before our meeting on **Friday, March 3rd** and be prepared to discuss it.
*   Instructions for accessing the electronic version of this book are [here](../../Required_Reading_Schedule.md#accessing-ebooks-for-free-through-the-usu-library)


# Action Items

*   Work on phase **0. Requirements Analysis** of the new assignment *today*
    *   Wrap it up *tomorrow*
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Introduce Assignment #4: Bingo! UML Design

In this assignment you will practice Test Driven Development and use UML as a design tool.


## What program should I use to make my UML class diagram?

I don't really mind which drawing program you use to create your UML class diagrams so long as your diagrams:

0. are legible
1. represent correct UML, at least as far as was discussed in class

One tool that's free and easy to get started with is https://diagrams.net/.  Detailed instructions are found in the starter code repo as well as in UML.md under the heading [How do I draw a UML class diagram?](../UML.md#how-do-i-draw-a-uml-class-diagram)



# Retrospective: Assignment #3

**Traffic jams**

Take one sticky note of each color.  Identify up to **three** things that
affected your progress on the Big Data assignment:

0. __Pink__: Things that **stopped** your progress (pretend these are red)
1. __Yellow__: Times you realized you were going **slow**
2. __Green__: Full speed ahead! ideas or techniques that helped you **go**

Describe each event and roughly when it happened to you.

There were 12 days from *Monday, Feb. 13th* to *Friday, Feb. 24th*



# What you need to gain from assignments

The point of programming assignments isn't to write a perfect program.
In fact, I *hope* that you make a lot of mistakes along the way.  

*You must make mistakes in order to learn*

The purpose of assignments is to exercise your *problem-solving skills* to gain
experience.  I want you to make your mistakes with me so you don't make them
in front of your boss and co-workers.

This is why I teach you skills and techniques such as

*   Regular scrum meetings
*   Actively asking questions instead of passively listening
*   Using Git
*   The Python REPL and debugger
*   Rubber Duck debugging
*   UML Class Diagrams

These tools reduce the risk of making mistakes, freeing you to have learning
experiences.

But this can only work if you have plenty of time to fail a few times.
Starting late leaves only enough time to get it right the first time.  If you
must get it right the first time you miss out on most of the value of the
assignment.

*The more times you fail, the better you will learn*



# A solution to Assignment #3 

## This is only *one* way to solve Assignment #3

This is not the only valid way write this program, and it's far from the best
way to solve the problem.

I don't want you to feel bad if your solution is longer than mine.  If your
program works, you succeeded in solving the problem and should feel proud!

A good program is exactly as long as it needs to be to solve the problem at
hand.  No more, no less.

A short program is evidence that the author possesses a clear understanding of
the problem.  When more time is allocated to studying and preparing for an
assignment, fewer lines of aimless code are written.  Programs become cleaner
because your ideas are expressed more forcefully and directly.

![Planning > Programming](./34-planning.png "Weeks of programming can save you hours of planning.")

Once you have begun writing a program you have locked yourself into a
particular way of doing it.  Are you ready to be that committed to your
"solution"?  Are you sure that you haven't glossed over some important detail
that will save you from writing paragraphs of convoluted code?




# [UML: Multiplicity Constraints](../UML.md#multiplicity-constraints)

In some systems it is important to document the number of objects that participate in relationships.

A multiplicity constraint indicates how many times an object from one class can be associated with objects of another class



# [UML: Inheritance ("is a" relationships)](../UML.md#inheritance-is-a-relationships)

The Inheritance relationship enables your code to capture the idea that two objects aren't exactly the same, but are similar enough to share common elements and methods.

We'll cover this idea in much more depth in a future module.

For now it is enough to understand that inheritance expresses the idea that one kind of class is a kind of another class.



# [Real-world UML class diagrams](https://www.uml-diagrams.org/class-diagrams-examples.html)

I show these examples of UML class diagrams to give you an idea of what a UML class diagram that describes part of a real-world program looks like.  Your diagrams do not need to be this complex or detailed!  Our Bingo Card Generator is far more simple than these systems.

It takes *many* UML class diagrams to fully describe a real-world system.  

The Unified Modeling Language defines other kinds of diagrams besides class diagrams.  A class diagram describes only one aspect of a system.  Other diagrams are used to explain how various parts of the system interact with each other while the program is running, and some are used to describe all of the ways a user might use a system, etc.


## Diagrams of interest:

*   Illustration of dependencies, public/private access modifiers, data types
    *   [Sentinel HASP Classes of Aladdin Package](https://www.uml-diagrams.org/software-licensing-class-diagram-example.html)
*   Illustration of associations, multiplicity constraints
    *   [Online Shopping](https://www.uml-diagrams.org/examples/online-shopping-domain-uml-diagram-example.html)
        *   This diagram uses the *composition* symbol for some of its associations; we won't be that strict in Bingo!
*   Illustration of associations, multiplicity constraints, relationship descriptions
    *   [DICOM Model of the Real World](https://www.uml-diagrams.org/dicom-real-world-uml-class-diagram-example.html)


### Symbology Glossary

*   `+` indicates *public* accessibility
*   `-` indicates *private* accessibility
*   `#` indicates *protected* accessibility
*   `^` denotes an *inherited* member
    *   This data member belongs to this class because it inherits from an ancestor class
*   `/` denotes a *derived* member
    *   This member's value is computed from other members
*   Open (white) diamond indicates an "Aggregation" association
    *   The diamond is attached to the "parent" class
    *   Instances of the child class may exist independently of its parent, and may be attached to other parents/aggregates
        *   For example Cars & Wheels
        *   Wheels can be removed from one car and attached to another, or may be kept in the garage until the weather improves
*   Closed (black) diamond indicates an "Composition" association
    *   The diamond is attached to the "parent" class
    *   Instances of the child class may **not** exist independently of its parent 
        *   For example, you and your brain
        *   You cannot live without your brain, and vice-versa



