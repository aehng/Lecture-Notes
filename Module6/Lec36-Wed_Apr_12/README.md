CS1440 - Wednesday, April 12 - Lecture 36 - Module 6

# Topics:
* [Announcements](#announcements)
* [Discussion: "The Mythical Man-Month" by Fred Brooks, Jr](#discussion-the-mythical-man-month-by-fred-brooks-jr)
* [Any final questions about Assignment 5.1](#any-final-questions-about-assignment-51)
* [Exception Best-Practices](#exception-best-practices)
* [Exceptions in Python](#exceptions-in-python)


------------------------------------------------------------
# Announcements

## Friday'S Class Is Cancelled For BSidesSLC

![./02-bsides-logo.png]

I hope to see you there!


## Take the IDEA Survey

*   So far we're at a XX% response rate!
    *   My goal for the class is 80%
*   It's worth 25 points of extra credit
*   The survey closes 04/26/2023 at 11:59 PM


# Action Items

*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Discussion: "The Mythical Man-Month" by Fred Brooks, Jr.

## What is the big idea Brooks wants to get across?

*   ...
*   ...

## Does a bigger team of programmers make a project come together faster?

*   ...
*   ...

## Do teams spend enough time testing their code?

*   ...
*   ...

## How much time does Brooks recommend a project spend in testing?

*   ...
*   ...

## What should you do if your schedule starts to slip?

*   ...
*   ...


## Key take-aways

<details>
<summary>Ideas that you must remember from this essay</summary>

*   Developers are **irresponsibly optimistic** when it comes to estimating project schedules
    *   On the other hand, some developers give up on estimations entirely and **just throw out huge numbers** without paying much thought to the matter
*   With experience you can become a **good estimator**
    *   This is helped by **gaining knowledge** both in the problem domain as well as with the tools/technologies used
*   One reason large projects exceed their schedule is **communication**
    *   As more programmers become involved, more **coordination** is needed
    *   This increases time spent in large meetings
    *   Meeting time is very expensive (programmers cost a lot per hour), and is time not spent creating code or running tests
*   System testing is **deferred** until all production is completed *(you don't have a system to test until then)*
    *   If the production schedule has slipped, **testing time is foreshortened**
    *   This is a **grave mistake**, and one that is repeated to this day
*   Brooks recommends spending up to **50% of a project's time in testing**
    *   Most projects don't plan for this and go past the due date by at least this much anyway
*   Programmers need to stiffen their backbones and tell managers & customers that **the best thing to do for a late software project is be patient**
    *   *Nothing* you do can possibly make it finish **sooner**
    *   *Anything* you do will most likely make it even **later**!
    *   Remember Brooks's Law: *Adding manpower to a late software project makes it later*

</details>



# Any final questions about Assignment 5.1?

*   The assignment is due **at midnight on Friday**
    *   This is the last assignment that you may use the **grading gift**
    *   If you want to use the grading gift, request it via email **before midnight on Sunday**

What questions do you have about this assignment?

*   ...
*   ...
*   ...



# [Exception Best-Practices](../Exceptions.md#exception-best-practices)

Follow these guidelines for best results



# [Exceptions in Python](../Exceptions.md#exceptions-in-python)

You've already been taking advantage of exceptions.  By allowing functions such as `open()` to crash your programs you are letting Python do the work of reporting errors in your code.



