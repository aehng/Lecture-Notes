CS1440 - Wednesday, March 15 - Lecture 24 - Module 4

# Topics:
* [Announcements](#announcements)
* [Refactoring a Messy Program](#refactoring-a-messy-program)


------------------------------------------------------------
# Announcements

## BSidesSLC Registration is Open!

*   **When**  Friday, April 14th - Saturday, April 15th
*   **Where** Conference Center at SLCC Miller Campus 9750 S 300 W, Sandy, UT
*   [**BSidesSLC Discord**](https://discord.com/invite/hBcnv9gb73).
*   **Cost**  
    *   General Admission $19 + taxes & fees
    *   General Admission + Electronic Badge $119 + taxes & fees
    *   [Tickets](https://www.eventbrite.com/e/bsidesslc-2023-tickets-527264701917)
*   If you attend the conference I will replace your lowest assignment/exam score with **full credit**
    *   It is good enough if you can only make it one of the days, either Friday or Saturday

![](./02-bsides-logo.png)


# Action Items


*   This Week's Assigned Reading: "The Other Face"
    *   Read the essay "The Other Face" (Chapter 15) of the book "The Mythical Man-Month" before our meeting on **Friday, March 17th** and be prepared to discuss it.
    *   Instructions for accessing the electronic version of this book are [here](../../Required_Reading_Schedule.md#accessing-the-mythical-man-month-for-free-through-the-usu-library)
*   You should be in the midst of phase **3. Testing and Debugging** *today*
    *   Continue your testing work *tomorrow*, taking care to document your test cases and their results
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Refactoring a Messy Program

I have a sample of [ugly Python code](./16-refactoring-demo/ugly.py).

This program is correct in the sense that it performs the task it is meant to do.  There are no (known) failures, faults or errors preventing it from producing good output.  However, the source code leaves much to be desired.

Take a few minutes with your study buddies to read it and make notes about what you notice.  Try to answer these questions:

*   What does this program do?
    *   You will know that you understand it if you are able to capture its essence in two or three **short** statements
*   Are there any lines of code that don't contribute to the outcome of the program?
    *   What variables or imports are unused?
*   How many passages of redundant code can you find?
*   What features make this code hard to understand?
    *   What would you change to improve the readability of this code?
    *   How would you split this program into *three* modules?


## Let's refactor this code together...

...to improve its *non-functional attributes* (this is a nice way of saying "make it easier to read")





