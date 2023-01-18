# Software Development Plan

*Adapted from Introduction to Programming using Python by Y. Daniel Liang, section 2.13*

Assignments in this course are larger and more complex than in CS 1400.

You will be given around two weeks per assignment (a.k.a. a *sprint*).  You are given this much time because I sincerely believe that you need all of it.

You should spend more time *designing* your program than *writing* it.  It is perfectly normal to not write a single line of code during the first week of an assignment.  When you focus on designing a good solution before coding it, you encounter fewer bugs and experience less confusion.

This table gives an idea of how you ought to spend your time:

| Project Phase                | Portion of effort
|------------------------------|------------------
|0. Requirements Specification | 20%
|1. Design                     | 30%
|2. Implementation             | 15%
|3. Testing and Debugging      | 30%
|4. Deployment                 | 5%
|5. Maintenance                | ∞

*   In a real world project, **Phase 5: Maintenance** completely dominates the others; it can last years or decades!
    *   Obviously, you can't experience that in this short time we have together in this class.
*   For best results, apply this advice over the whole two-week sprint.
    *   Do not expect a good outcome if you procrastinate and try to cram this in to one or two days.



## Phase 0: Requirements Specification
*(20% of your effort)*

**Important - do not change the code in this phase**

Requirements specification is the process where you come to understand the problem that the software will address, and document what the system needs to do.

Rewrite the requirements *in your own words*.  Define what a good solution will look like so you know when you are done.  Make a list of things that you already know how to do, and a list of what you *don't* yet know how to do.  This highlights your "known knowns" and "unknown unknowns".

![Knowns-Unknowns.png](assets/Knowns-Unknowns.png "known knowns vs. unknown unknowns")

As you restate the problem in your own words, identify data that will be used by the program and think about how they may be represented in the programming language.  Consider how the data *flows* through the program.

Does the program get input from the user?  If so, does it come from interactive prompts, command-line arguments, a file or from the internet?  It helps to start by considering what the output should look like, and then figure out what input leads to that output.

Identify any non-trivial algorithms you will need to create to convert the inputs into outputs.  Do not design them yet; that is for the next phase.


### Deliverables

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).



## Phase 1: Design
*(30% of your effort)*

**Important - do not change the code in this phase**

This will be the longest part of your plan.

In this phase you devise a process for obtaining the *output* from the *input*.  Decompose the problem into simple, manageable functions, then design each function individually.

Describe how your functions will process data by sketching them in **pseudocode**.  Do not write real code now; you will make many mistakes.  Mistakes are a critical part of your journey; you cannot write a good program without them.  But, it is easier to throw away *pseudocode* than runnable code.  This is why you must resist the urge to write *real* Python code now!  At first the pseudocode will be vague; incrementally refine it until it is nearly as detailed as *real* code.

This is an example of what pseudocode looks like:

```python
def rotate_lower(c, n)
    """
    Input: "c" - a lowercase character
           "n" - an integer [0..26]
    Output: "c" rotated by "n" positions.

    This function will return a bad result if "n" is negative or greater than 26.
    The caller is responsible for avoiding this.
    """
    o = c converted to integer
    if the letter represented by (o + n) comes after 'z'
        return (o + n - 26) converted to char
    else (o + n) falls within the alphabet
        convert (o + n) to char and return

def rotate_upper(c, n)
    The same as rotate_lower(), but checks against capital 'Z' instead of 'z'

def rotate(c, n)
    """
    Input: "c" - a lowercase character
           "n" - an integer [0..26]
    Output: When "c" is alphabetic, return it rotated by "n" positions.
            Otherwise, return "c" unchanged

    Values of "n" that are too large or too small will cause errors.
    The caller is responsible for avoiding this.
    """
    if c is lowercase
        return rotate_lower(c, n)
    if c is uppercase
        return rotate_upper(c, n)
    if c is a symbol or a digit
        return c unchanged
```

When your pseudocode is suitably detailed, on paper (or a whiteboard) pretend to call your functions to learn what they will do.  Consider both good and bad inputs.  It is not a bad thing for your functions to return a bad result or crash; it is only bad when they do this *unexpectedly*.  Keep notes of these thought experiments so you can revisit them after you write these functions for real.

Example:

*   `rotate('a', 2)` returns `c`, because that is two characters after lowercase `a`
*   `rotate('A', 2)` returns `C`, because that is two characters after uppercase `A`
*   `rotate('Z', 2)` returns `B`, because two characters after uppercase `Z` is past the end of the alphabet, so it wraps back around to the beginning
*   `rotate('0', 2)` returns `0`; this algorithm only rotates letters, not digits
*   `rotate('A', 36)` is an error; this algorithm only rotates up to 26 positions.  It doesn't matter what is returned in this case because it should not be used in this way. 

Pseudocode is closer to plain English than it is to working Python code, and lacks important details like syntax.  Indentation is used to aid readability.  Because you did not spend much effort making it runnable, you can discard it without remorse and rewrite a better version.


### Deliverables

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   [ ] Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them in **Phase 3: Testing and Debugging**


## Phase 2: Implementation
*(15% of your effort)*

**Finally, you can write code!**

Implementation is when you translate your design into a runnable program in a real programming language.

This is the only part of the software development process focused on writing real code in a programming language.

You will know you are ready for this when your pseudocode is nearly as detailed as a real program.

0.  Copy pseudocode into your Python files.
1.  Function signatures are easy to convert into proper Python syntax.
2.  Comment out the pseudocode, adding the `pass` statement where needed.
3.  This results in a valid program that runs without errors; at this stage your program doesn't do anything, not even crash.
4.  Gradually replace pseudocode with equivalent Python statements.
    *   Watch for the two signs which confirm that you have made a good design:
        1.  Your pseudocode is easily translated into Python.
        2.  This phase goes by faster than **Phase 1: Design**.

While you are learning a new programming language this phase *will* be slow and difficult.  With experience you will spend less time in this phase.

### Deliverables

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan, etc.



## Phase 3: Testing and Debugging
*(30% of your effort)*

Testing ensures that the source code meets the project's requirements.

In the real-world, an independent team of software engineers who are not involved in the design and implementation of the product may perform testing.  Unfortunately, you do not have a team of testers at your disposal.  You'll just have to do this yourself!

Broadly speaking, there are two kinds of tests:

0.  Small tests that exercise functions in *isolation*
1.  Large tests to demonstrate that all of the functions work well *together*

Write *good* and *bad* test cases to catch *false positives* and *false negatives*.  Use the good/bad examples devised in **Phase 1: Design** to prove that each function performs as expected.  It is not a bad thing for a function to crash or give a wrong answer.  It is bad when this happens *unexpectedly*.  You may discover mistakes in your design and/or implementation.  When you fix these bugs, devise new test cases to detect these bugs should they return.

This document should contain step-by-step instructions that a non-technical user could follow to satisfy themselves that your program is correct.

Explain the entire process from launching the program, entering inputs, and interpreting the results.

### Deliverables

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.



## Phase 4: Deployment
*(5% of your effort)*

Deployment makes the software available for use. Depending on the type of the software, it may be installed on each user’s machine or installed on a server accessible on the Internet.

At DuckieCorp **deployment** means submitting your homework.  Don't leave this to the last moment!  Leave yourself plenty of time to fix any problems that come up.

### Deliverables

*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.



## Phase 5: Maintenance
*In the real world, the duration of this phase completely dominates the others.  For assignments in this class, spend a few minutes writing thoughtful answers to the questions provided.*

Despite the fact that you don't really get to experience this phase of the process in this course, **maintenance** is the most important (and longest) part of the software life cycle.

Maintenance is concerned with updating and improving the product.  A software product must continue to perform and improve in an ever-evolving environment.  This requires periodic upgrades of the product to fix newly discovered bugs and incorporate changes.

You are invited to think about parts of your program that won't stand the test of time.  You know where these are - they're the bits of code that you aren't 100% sure how or why they work.

### Deliverables

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.


*Updated Wed Jan 18 13:12:05 MST 2023*
