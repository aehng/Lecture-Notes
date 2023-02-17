CS1440 - Friday, February 17 - Lecture 17 - Module 2

# Topics:
* [Announcements](#announcements)
* [How to Read Documentation](#how-to-read-documentation)
* [Applying Text Tools to Assignment #3](#applying-text-tools-to-assignment-3)
* [Write the `startgrep` text tool](#write-the-startgrep-text-tool)
* [Redirect a program's output with the shell](#redirect-a-programs-output-with-the-shell)


------------------------------------------------------------
# Announcements

## Monday is Presidents' Day

No classes are held on February 20.  See you on Wednesday!


# Action Items

*   *Today* you should finish phase **1. Design** of the assignment
    *   Be ready to move on to phase **2. Implementation** *early next week*
    *   Work on phase **2. Implementation** of this assignment soon with a goal to complete it by *the middle of next week*
    *   Move on to phase **3. Testing and Debugging** quickly thereafter so you can identify and fix any problems with your assignment
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# [How to Read Documentation](../How_to_Read_Documentation.md)

*   Take Stack Overflow answers with a grain of salt
    *   There can be [security implications](https://stackoverflow.blog/2019/11/26/copying-code-from-stack-overflow-you-might-be-spreading-security-vulnerabilities/)
    *   There are a lot of show-offs, too.  You might just come up with a more simple solution yourself!
    *   It can be a great way to learn a new language, though; balance its pros & cons.
*   If you ask a programming language subreddit "Where should a beginner start?" you can get advice that is overwhelming.
    *   Those folks may not understand what's *best* for you in your situation.


## What are your biggest takeaways from reading this essay?

*   There (at least) are two reasons you might be reading a technical document
    0.  Everything is on fire and I need an answer ASAP
    1.  I want to learn things b/c learning is fun
*   We should be approaching documentation and reading it regularly
*   Sites like StackOverflow & GeeksForGeeks are helpful because they have a lot of *examples*, and can be a good resource to learn what the important *jargon* is
    *   Then you know what to search in the official documentation
*   StackOverflow (and similar sites) are good resources, but take their advice with a grain of salt



# Applying Text Tools to Assignment #3

Creating the Text Tools in Assignment #2 has prepared you for this assignment.
In addition to creating a program that can help you manipulate a data set
that's too big to handle manually, you have learned basic text-processing
techniques that can be applied in other circumstances.

Take a moment with your study buddies to review the general problem-solving
techniques and identify some ways the previous assignment has prepared you
for this task:



<details>
<summary>Cool things you can do with your new text tools</summary>

0.  Measure the size of input files
1.  Count occurrences of substrings
2.  Cut out undesired columns
3.  Re-arrange input files
    *   Test that your program gives the same results **regardless** of the order of the input
    *   **EXCEPTION** the CSV header line should always be the 1st line of input
4.  Create smaller data files for debugging
    *   Debugging a ~500MB data file is tedious
    *   Craft a smaller version of the data to give your debug session a quicker turn-around
    *   This is why the starter code's `data/` directory contains so many sub-directories!

</details>


## How to "install" your text tools

TL;DR: update your shell's `PATH` environment variable to include the folder that contains `tt.py`

[Running your Python Text Tools from another directory](../Installing_the_Text_Tools.md)

These instructions are also included in the `instructions/` directory of the Assignment #3 starter code repo.



# Write the `startgrep` text tool

While it's good to know how to use tools that others have written, sometimes
you need to do something for which there is no pre-existing tool.  Being able
to build your own tools is an indispensable skill.

Assignment #3 asks you to work with an enormous data set.  Large data sets can
make verifying a program's behavior difficult because manually checking the
results takes too much time.

* How do you know whether your program is correct or not?
* If you get the wrong results, how can you locate the problem?

One approach is to test the code against a smaller data set.  You cannot
manually verify the results for 3.5 million lines of data.  But you *could*
manually verify the results for a handful of lines, or even for a few thousand.

The starter code for Assignment #2 includes example output for reduced data
sets.  To generate the smaller sets you can add a new capability to your text
tools that we'll call `startgrep`.

The `startgrep` tool works like the `grep` tool, except it only matches when
the pattern occurs at the beginning of the line.  It can be described with this
doc string:

    """print lines of files beginning with a pattern"""


[Demo: convert `cat` into `startgrep`](./startgrep.py)

As you work on assignment #3 you may face other problems for which you don't
have a prepared tool.  Now you know that you can make your own tools.



# [Redirect a program's output with the shell](../Shell_Redirection.md)

A common question asked about the text tools is "why don't they create output files?"

The reason that our text tools can't create output files is that they don't need to.  The shell can already do this for you!

Shell redirection is a technique that you can use now and later on Assignment #3.  You are gradually building skills that enable you to solve bigger and bigger problems!



