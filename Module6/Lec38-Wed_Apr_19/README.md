CS1440 - Wednesday, April 19 - Lecture 38 - Module 6

# Topics:
* [Announcements](#announcements)
* [What is recursion, really?](#what-is-recursion-really)
* [Tips for thinking about problems recursively](#tips-for-thinking-about-problems-recursively)
* [Learn the one recursion trick they don't want you to know](#learn-the-one-recursion-trick-they-dont-want-you-to-know)
* [Why am I making you use recursion on Assn6](#why-am-i-making-you-use-recursion-on-assn6)
* [Practical considerations when using recursion](#practical-considerations-when-using-recursion)
* [Conquering Stack Overflow](#conquering-stack-overflow)


------------------------------------------------------------
# Announcements

## Take the IDEA Survey

*   So far we're at a XX% response rate!
    *   My goal for the class is 80%
*   It's worth 25 points of extra credit
*   The survey closes 04/26/2023 at 11:59 PM


## Questions for AMA lecture - Monday, April 24th

The topic of the last lecture of the semester is **Ask Me Anything**

I'd love to hear what you'd like to learn a little more about, and what topics may pique your interest!  There is a Canvas discussion thread called **Ask Me Anything** (Canvas Sidebar -> Discussions).  There you can post questions you've been dying to ask all semester, and I will do my best to answer them in the last lecture.

You will receive **10 participation points** for posting in/responding to this thread.  If you'd rather share your question in the Discord `#AMA` channel instead of on Canvas, just post a link to your question on Discord so I can credit the participation points to you.  You are encouraged to strike up a discussion on each others' questions, and your participation will help craft our final lecture!

*The AMA thread will be locked at midnight on Friday, April 21st to give me time to put the lecture together*


# Action Items

*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team
*   You should be ready to start phase **1. Design** of this assignment *today*
    *   Continue your design work through *the end of the week*
    *   Be ready to move on to phase **2. Implementation** *early next week*



# [What is recursion, really?](../Solving_Problems_With_Recursion.md#what-is-recursion-really)

> In order to understand recursion, one must first understand recursion.



# [Tips for thinking about problems recursively](../Solving_Problems_With_Recursion.md#tips-for-thinking-about-problems-recursively)

Whenever I am faced with recursion, I apply these problem-solving strategies:

*   **Start with what you know**
*   **Divide the problem**
*   **Reduce the problem**



# [Learn the one recursion trick they don't want you to know](../Solving_Problems_With_Recursion.md#v-anton-sprauls-big-recursive-idea)

This is the finished [factorial.py](./factorial.py) program that demonstrates the Big Recursive Idea.


## Live coding activity

Use the BRI to write a recursive function that solves the problem of [making change](./making_change.py)

0.  Write a "lazy middleman" function that simply calls on the iterative function to do all of the work
1.  Make the middleman just a little less lazy by handling the base cases
2.  Force the middleman to do at just **one** step before pawning the rest of the work off
3.  And... BAM!  Now we got you right where we want you!  Replace the call to the iterative function with a recursive call to the lazy middleman function.  You're not so lazy now, huh?



# Why am I making you use recursion on Assn6?

**Why am I making you approach this assignment this way?**

Take a moment to respond to this question on your mud card with your thoughts and impressions.


<details>

<summary>A few reasons why</summary>

*   As a problem-solving technique, recursion best embodies **divide the problem**.
*   Recursion is more "dynamic"; with a `for` loop I have to know ahead of time
    how far it needs to go/how many iterations it must take.  A `while`
    loop insists that I clearly state at the top all of the exit conditions
    (though some coders prefer to sprinkle `return` or `break` statements
    throughout a loop where it makes sense.  Recursion can just "go" no matter
    how deep it needs to.
*   With recursion, each possible path in the web document can have its own
    "bottom", and each path knows how deep it is.

I want to teach you recursion to give you another problem-solving tool.  For
all of its mystery and reputation of complexity, recursion can lend itself to
very short and elegant solutions to problems which have one of these
properties:

*   The data structure underlying the problem is itself recursive
*   You can identify a trivial "base case" *and* an inductive step which
    changes a complex case into something that's closer to being the base case.


Problems with these properties include:

*   Search algorithms (i.e. chess, checkers, go, tic-tac-toe, etc.)
*   Parsing programming languages (your compiler or interpreter is recursive)
*   Traversing a recursive data structure (like your file system or the internet)

However, recursion isn't just for problems that naturally have recursive
characteristics.  *Any* iterative algorithm can be converted into an equivalent
recursive algorithm, even if the above properties don't apply.

In other words, a problem **does not** need to be essentially recursive to have a recursive solution applied to it.  Nor is it the case that a recursive problem **must** be solved with recursion.  But a recursive solution is likely the **most simple & elegant** way to solve a recursive problem.

Iteration isn't worse than recursion, nor is recursion worse than iteration.  They're just different tools that you should learn to use appropriately.

</details>



# [Practical considerations when using recursion](../Solving_Problems_With_Recursion.md#practical-considerations-when-using-recursion)

*   Wrapper functions
*   Common recursion pitfalls



# [Conquering Stack Overflow](../Solving_Problems_With_Recursion.md#conquering-stack-overflow)


*   Make a non-tail-call-optimized version of the "Song That Never Ends" program
*   Run both of them side-by-side to see the difference
*   Which compilers/languages are capable of Tail Call Optimization?
    *   Check out Java's stack trace



