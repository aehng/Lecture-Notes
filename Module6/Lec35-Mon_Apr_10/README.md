CS1440 - Monday, April 10 - Lecture 35 - Module 6

# Topics:
* [Announcements](#announcements)
* [Exception Handling](#exception-handling)
* [Two Approaches to Error Handling](#two-approaches-to-error-handling)
* [Comparing The Two Approaches to Handling Errors](#comparing-the-two-approaches-to-handling-errors)
* [Pros & Cons of Exception Handling](#pros-cons-of-exception-handling)
* [What is "Turing's Curse"](#what-is-turings-curse)


------------------------------------------------------------
# Announcements

## ACM & ACM-W Destroy the Stereotype Night

*   **When**  6:00pm Tonight
*   **Where** Old Main 326

![./03-acmw-poster.png](./03-acmw-poster.png)


## Free Software and Linux Club

*   **What**  Ruling the Modern  Web With Free and Open Source Software
*   **When**  6:30pm Thursday, April 13th
*   **Where** ESLC 053, [FSLC Discord server](https://discord.gg/GKWhbVDN38)
*   **Streaming** https://linux.usu.edu/streams

The presentation will be by Simponic on the current state of the modern web - from the perspective of the general user in addition to that of us developers (including those looking to get started). We'll discover how Free Software can be used to mitigate a lot of the webs' problems, and its role in increasing user choice, privacy, and security. I will also be showing a simple application as it would have been developed through the ages of the internet, to get a good understanding of how we got here. Maybe a little bit of NGINX RTMP stuff if there's time, since I've picked up there's some interest in that and how it's setup for the club.


## BSidesSLC Is This Week

*   Last chance to sign up!
*   If you attend the conference I will replace your lowest assignment/exam score with **full credit**
    *   It is good enough if you can only make it one of the days, either Friday or Saturday
*   Either find me at the conference or send me a selfie your conference badge
*   *Note:* if you are enrolled in both of my classes this semester, you may replace a low score in only **one** class


## Take the IDEA Survey

*   So far we're at a 22% response rate!
    *   My goal for the class is 80%
*   It's worth 25 points of extra credit
*   The survey closes 04/26/2023 at 11:59 PM


# Action Items

*   This Week's Assigned Reading: "The Mythical Man-Month"
*   Read the essay "The Mythical Man-Month" (Chapter 2) of the book "The Mythical Man-Month" before our meeting on **Monday, April 17th** and be prepared to discuss it.
    *   Instructions for accessing the electronic version of this book are [here](../../Required_Reading_Schedule.md#accessing-the-mythical-man-month-for-free-through-the-usu-library)
*   Work on phase **2. Implementation** of this assignment *today* with the goal to complete it *tomorrow*
    *   Begin phase **3. Testing and Debugging** ASAP so you can identify and fix any problems with your assignment
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team





# [Exception Handling](../Exceptions.md)

Every line of code carries a risk that something could go wrong.  Murphy's law
dictates that if something can go wrong, it *will* go wrong.  Therefore,
responsible programmers must be prepared for any unfortunate event.



# [Two Approaches to Error Handling](../Exceptions.md##two-approaches-to-error-handling)

Broadly speaking, there are two approaches to handling problems that arise as a program runs:

0.  **Easier to Ask Forgiveness than Permission** (EAFP)
1.  **Look Before You Leap** (LBYL)



# [Comparing The Two Approaches to Handling Errors](../Exceptions.md#comparing-the-two-approaches)

The [same program](../echo_server/README.md) has been written in C and Python to
contrast each languages' approach to handling errors.

Which error handling style do you find easier to read and understand?



# [Pros & Cons of Exception Handling](../Exceptions.md#pros-cons-of-exception-handling)

Like all good things in programming, the subject of exception handling is a bit
of a holy war.  Whether it's a good or bad thing is entirely up to you and how
you employ it.



# What is "Turing's Curse"?

Looking back on 30 years of programming: there's nothing new since 1983.

[OSCON 2013 talk by John Graham-Cumming](https://www.youtube.com/watch?v=hVZxkFAIziA)


<details>

<summary>TL;DW</summary>

*   There is nothing new under the sun - all of the technologies we know and
    love were invented by 1983
*   Programmers spend too much of their time on bugs
*   Unreliability is what we need to work on next.  We need to help programmers
    *   Make fewer mistakes
    *   Find their mistakes


#### Turing's Curse
There are certain things that machines, provably, are not going to be able to
do for us.  There are limits to what computers can do.

*   On the one hand, we aren't going to be able to make tools that will be able
    to solve all of our problems :(
*   On the other hand, it means that humans will still have some utility after
    the robot overlords take over the world ;)

</details>



