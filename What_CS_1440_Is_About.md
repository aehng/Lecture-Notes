# What CS 1440 Is About

## This is not a class about programming 

*   Writing programs that work is necessary, but **not sufficient**
*   This is a class about **solving problems**
*   Programming is just a means to that end


### Let go of the notion that `Computer Science == Computer Programming`

> Computer science is no more about computers than astronomy is about telescopes. 
>
> Attributed to Edsger Dijkstra, most likely erroneously

Computer Scientists are Communications majors who happen to also communicate to
machines.

*   Machines are only **one** of your audiences
*   Don't forget that **people** read code, too!
    *   Be kind to your future self


### Don't write Python code to solve your problem

*   Instead, use Python as building material to create a new language (one that will resemble Python) that lets you describe the problem to the computer
*   Use Python to build new nouns and verbs that have enough descriptive power to explain the problem and its solution clearly *both* to the computer *as well as* to other humans

> [...] a computer language is not just a way of getting a computer to perform operations but rather that it is a novel formal medium for expressing ideas about methodology. Thus, programs must be written for people to read, and only incidentally for machines to execute.
>
> Hal Abelson


### Don't stoop down to the computer's level

Instead, raise the computer to your level.

*   Write code to the proper level of **abstraction**
    *   Programs describe both very *large* ideas as well as very *small* ideas
    *   Well-written code is organized in layers that keep big ideas together and separate from small ideas
    *   Layers are arranged along a continuum from *abstract* (e.g. "big picture") to *concrete* (e.g. little details)
*   The `main()` function should read like the Table of Contents for the solution to the problem
    *   It may resemble a to-do list composed of "big" ideas
    *   Each function that `main()` calls deals with a smaller aspect of the problem in more detail; the functions called from here deal with an even smaller slice of the problem, and on and on until you're dealing with leaf-node functions that deal in the most primitive faculties of the language. 
*   At a certain level of abstraction you'll recognize patterns and analogies that weren't apparent on a different level
    *   Whenever you face a problem, pause to consider it from each of the layers you've identified in your design
    *   You will find that problems that seem intractable at the bottom have a trivial solution a few levels up, and vice versa


## Where the Software Development Plan fits in

The Software Development Plan helps you apply the General Problem-Solving Techniques (GPST).  The 1st GPST you will learn is to "always have a plan"; the [SDP](./Module0/Software_Development_Plan.md) is literally this plan.  In it you *restate the problem* in your own words and pseudocode.  When thinking with pseudocode it is much easier to:

+   Divide your solution into pieces
+   Decide where to start
+   Notice analogies
+   Realize which corners can be safely cut and where to avoid going overboard
+   Enumerate your "known unknowns" - areas that merit experimentation
+   With a clear picture you won't get frustrated to the same degree
