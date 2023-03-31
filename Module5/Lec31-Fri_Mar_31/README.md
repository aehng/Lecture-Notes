CS1440 - Friday, March 31 - Lecture 31 - Module 5

# Topics:
* [Announcements](#announcements)
* [Discussion: "No Silver Bullet" by Fred Brooks, Jr](#discussion-no-silver-bullet-by-fred-brooks-jr)
* [3. Polymorphism Applied](#3-polymorphism-applied)
* [Design Patterns](#design-patterns)
* [Factory Method Pattern](#factory-method-pattern)
* [The Strategy Pattern](#the-strategy-pattern)


------------------------------------------------------------
# Announcements

## BSidesSLC Sessions and Workshops Posted

*   **When**
    *   Friday, April 14th: Professional Growth Day
        *   Sessions from Industry Experts, CTF, workshops, lock picking, soldering circuits, and more.
    *   Saturday, April 15th: Core Skills Day
        *   Level up your skills with workshops, trainings, and networking events.
*   BSidesSLC attendance replaces your lowest assignment/exam score
    *   If you attend the conference I will replace your lowest assignment/exam score with **full credit**
        *   It is good enough if you can only make it one of the days, either Friday or Saturday
    *   Either find me at the conference or send me a selfie your conference badge
    *   *Note:* if you are enrolled in both of my classes this semester, you may replace a low score in only **one** class
*   [**BSidesSLC Discord**](https://discord.com/invite/hBcnv9gb73).


# Action Items

*   Complete phases **4. Deployment** and **5. Maintenance** *today* 
    *   Make your final push to GitLab early so you have plenty of time to **verify** your submission
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Discussion: "No Silver Bullet" by Fred Brooks, Jr.

There are people who speak of a day when computer programming as a profession
will become obsolete as technology improves to the point where humans will not
be needed to write software.

## Essence & Accident in Software Engineering

The concepts of "essence" and "accident" is borrowed from Aristotle's "Metaphysics".


#### Essence

*   Something that is inherent in a design
    *   I can write the same program in different languages - it'll look different, but have the same logic
*   Reflects your intentions (as the creator of a program) for what the program should do


#### Accident

*   Something that happens, without being intentionally designed into it
*   Syntax, curly braces, semi-colons; the fiddly details of programming


### Questions for discussion:

Take a moment to write your biggest take-away from this essay on your mud card

*   Which difficulties in programming are "essential"?
    *   ...
    *   ...
*   Which difficulties in programming are "accidental"?
    *   ...
    *   ...


## What is the gulf between the Essential and the Accidental?

Legend:
-------
* Essential  `#`
* Accidental `-`

Writing a compiler today can be done in a one-semester undergraduate class (CS 5300: Compiler Construction):
```
#####---
```

Writing the 1st FORTRAN compiler in 1953 took John Backus and his team of brilliant CS pioneers at IBM four years:
```
######################################################################---------------------------------------------------------

Note: not to scale
```


## Rebuilding a building

Modern tools and building techniques enable us to build more-or-less identical
structures much more quickly today than in the past.

Examples of buildings which were completely destroyed and then rebuilt to the
same floor plan:


### Dresden Frauenkirche

https://en.wikipedia.org/wiki/Dresden_Frauenkirche

The first time the Dresden Frauenkirche was built, it was constructed between
1726 and 1743 (17 years).

**Original**
```
######################################################################
```

It was rebuilt after WWII between 1994 and 2005 (11 years)

**Rebuild** 
```
#############################################
```


### Nauvoo Illinois LDS Temple

**Original**
* Cornerstone     April 6, 1841
* Dedicated       April 30, 1846

```
######################################################################
```

**Rebuild**
* Announced      April 4, 1999
* Groundbreaking October 24, 1999
* Dedicated      June 27, 2002

```
####################################
```


### What does "No Silver Bullet" tell us about Software Engineering?

> Program complexity depends on the language used to write it.

The complexity of solving a problem shouldn't be exacerbated through the use of
an overly complicated programming language. 


> We need to change our mentality around how programs are created. We don't
> build programs, we grow them.

In order to build even larger systems, we need to think about providing a core
of functionality and adding other features onto it gradually.  Instead of
building the whole thing all at once, we plant a seed and cultivate it.



#### Don't hold your breath for a "best" solution

> "Silver Bullet" means the perfect solution. But programming doesn't have one
> specific answer. It has lots of complicated components that work together to
> create an answer.

In Fred Brooks' career software made huge advances in usability and
productivity. His assertion is that those gains came by solving the most
obvious problems with software - so-called "low-hanging fruit".

All of the easy problems had been solved by the time he wrote this essay, and
what we are left with are the truly difficult challenges inherent in software
engineering. Instead of waiting around for a new silver bullet to, his goal is
to encourage us to work towards slow and steady progress.



#### Can AI or better programming languages save us?

You'll be relieved to note that Brooks doesn't expect to see AI putting you out
of a job.  Likewise for "Automatic" programming; if you've ever used a code
generator, you'll understand what he's talking about.  The sorts of things
which are easily tackled with this sort of automation were not the essentially
difficult parts to begin with.

What about "graphical" programming languages?  People have been anticipating and
predicting such systems to finally make programming tractable.  To which I must ask:

*   How many of you have programmed in [Scratch](https://scratch.mit.edu/)?
*   How big was your largest Scratch Sketch?
*   Was making a "big" program in Scratch easier or harder than Python?



### "Assembly industry" vs. "Process industry": what's the difference?

> First, one must observe that the anomaly is not that software progress is so
> slow, but that computer hardware progress is so fast.  No other technology
> since civilization began has seen six orders of magnitude in performance
> price gain in 30 years. In no other technology can one choose to take the
> gain in either improved performance or in  reduced costs. These gains flow
> from the transformation of computer  manufacture from an assembly industry
> into a process industry.     
>
> -- Frederick P. Brooks, Jr.

*   https://en.wikipedia.org/wiki/Discrete_manufacturing
*   https://en.wikipedia.org/wiki/Process_manufacturing

#### Assembly industry
Products are put together from parts

Examples: Automobiles, furniture, toys, smartphones, and airplanes


#### Process industry
Products are undifferentiated

Examples: oil, natural gas and salt

Computers became cheap and plentiful because microchips result from a process
industry instead of a labor-intensive assembly industry.



## Promising Attacks on the Conceptual Essence

Be sure to study this section of the essay as there are exam questions related
to this.  Indeed, much of the purpose of this course is learning about the
advances which Brooks predicted.  These advances have come to pass and are,
broadly speaking, considered to be perfectly ordinary tools and techniques in
`$CURRENT_YEAR`.



# [3. Polymorphism Applied](../Four_Principles_of_OO_Design.md#3-polymorphism)

Python achieves polymorphism via so-called "Duck Typing":

> If it walks like a duck and it quacks like a duck, then it must be a duck

If there's one thing I am a fan of, it's more ducks!

        _
    .__(.)<  - Quack!
     \___)

['Sequences' Made Polymorphic](./Sequences/)



# [Design Patterns](../Design_Patterns.md#design-patterns)

Your Assignment #5.1 program will utilize two design patterns:

*   The Factory Method pattern
*   The Strategy pattern



# The [Factory Method Pattern](../Design_Patterns.md#the-factory-method-pattern)

The idea of the Factory Method design pattern is to separate the *location of creation* from the choice of *what* to create.

See the completed [Sequences](./Sequences) demo for an example of this pattern



# [The Strategy Pattern](../Design_Patterns.md#the-strategy-pattern)

This design pattern allows your users to select an algorithm or behavior at runtime.




