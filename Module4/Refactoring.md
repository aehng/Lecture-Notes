# Refactoring

* [What is Refactoring?](#what-is-refactoring)
* [Non-functional requirements](#non-functional-requirements)
* [Code Smells](#code-smells)
* [How will I know when to refactor?](#how-will-i-know-when-to-refactor)
* [Should I refactor *and* add functionality at the same time?](#should-i-refactor-and-add-functionality-at-the-same-time)



## What is Refactoring?

> The process of restructuring existing computer code without changing its external behavior.

*   [Wikipedia: Code Refactoring](https://en.wikipedia.org/wiki/Code_refactoring)
*   [Sourcemaking.com: Refactoring](https://sourcemaking.com/refactoring)


As programs evolve, we must reconsider our earlier design decisions.  With the benefit of hindsight, you will find better ways of doing the same thing.  Until you have a working system in front of you, you might not *really* know what it is you want to make.

At its heart refactoring is to improve the *non-functional* aspects of the code base


### What's the point of making big changes to code *without* changing its externally-observable behavior?

For one thing, readability makes a difference.  I once worked on a program that contained a serious bug that *should* have been obvious.  The code computed the volume of liquid in a tank using a straightforward formula from a high-school math class.  The bad line of code was right before our eyes, and had been there for years.

When we finally got a customer report about a discrepancy in the program's behavior (i.e. a **failure**), our first-line technical support expert was able to trace it down to a **fault**, but couldn't see the **error** (he correctly located the function responsible for the bad output, but couldn't explain what it was doing wrong).

I was pulled in to help, and was quickly embarrassed when I, too, failed to locate the error.  The failing function was brief, but its combination of poorly-chosen variable names with an over-reliance on globals made understanding very challenging.  I brought the code up on my desktop and ran it through the debugger.  Because I couldn't tell what was going on, that was no use.

Finally, I decided to rewrite the function.  With the help of a mathematics reference book I discovered the volume formula that the code implemented.  By renaming the variables in the code to match my math book, the problem immediately jumped out to me.  In its original, unreadable form, the bug existed for years before it was ever noticed.  The problem foiled my debugging attempts until I re-wrote it to be readable.


### What tools and techniques can we leverage to make broad, sweeping changes to a code base *without* changing its behavior?

*   Git - to bravely make changes without consequence
*   Rubber ducky - to identify your unknown-unknowns
*   Coaching center - bounce ideas off other people's heads
*   Experimentation with the REPL



## Non-functional requirements

Broadly speaking, *non-functional requirements* are aspects of a program which
are difficult to measure, or which aren't spelled out in the specification.
These things are often considered to be non-functional requirements:

*   Speed, memory usage, runtime performance in general
*   Number of lines of code
*   Number of variables
*   Number of functions
*   Number of classes
*   Number of parameters to functions, number of methods or data members in a class
*   How easy it is to extend the code
*   How readable the code is
*   How easy it is to locate and fix bugs in the code

These are all important things that may relate to the performance and operation
of a system, but they often take a backseat to the set of capabilities that the
customer expects.  Often these non-functional requirements are considered as
*quality requirements* of the system.

* [Wikipedia: Non-functional requirement](https://en.wikipedia.org/wiki/Non-functional_requirement)



## Code Smells

> In computer programming, a code smell is any characteristic in the source
> code of a program that possibly indicates a deeper problem.  Determining what
> is and is not a code smell is subjective, and varies by language, developer,
> and development methodology.
>
> -- [Wikipedia](https://en.wikipedia.org/wiki/Code_smell)


*   [Code Smells](https://blog.codinghorror.com/code-smells/)
*   [A catalogue of Code Smells](https://sourcemaking.com/refactoring/smells)
*   [Python Code Disasters](https://github.com/sobolevn/python-code-disasters.git)


The following lists are derived from [A catalogue of Code Smells](https://sourcemaking.com/refactoring/smells).

In your study of the Assignment #5.0 starter code have you come across these odors?

0.  **Magic Numbers**
    *   These are literal values used in critical places without any context or meaning
    *   "Does the `256` right here have anything to do with the `256` over there?"
1.  **Global Variables**
    *   Used to avoid passing a parameter into a function
    *   Used to return an extra value from a function
        *   There are better ways to meet both of these needs! (this does not apply to global `CONSTANTS`)
2.  **Poorly-named** Identifiers
    *   Variable names should strike a good balance between brevity and descriptiveness
    *   Short variable names are okay in some situations:
        *   `i` or `j` as a counter in a brief `for` loop
        *   Variables from well-known math formulae should match the textbook (i.e. `a`, `b` and `c` are familiar in a quadratic or Pythagorean formula)
        *   Otherwise, short names should be avoided
    *   Variables with really, really long names make code harder to read
    *   Variables that override or "shadow" other identifiers
        *   Builtin Python functions such as `input`, `len`, `list`, `max`, `min` and `sum` are especially susceptible to this
3.  **Bad** Comments
    *   Comments are the *condiments* of code; a small amount can enhance your meal, but too much ruins it
    *   Strive to write clear, self-documenting code that speaks for itself; when a line needs an explanatory comment to be understood, it indicates that identifier names were poorly chosen
4.  **Too many** Arguments
    *   Seen when more than a handful of parameters are passed to a function/method
    *   Parameters are passed in but never used
5.  Function/Method that is **Too Long**
    *   Too many lines of code typically happens because the function/method has too many different responsibilities
    *   Generally, a method longer than a dozen lines should make you ask yourself "can I split this into smaller, more focused pieces?"
6.  **Redundant Code**
    *   A repeated statement which doesn't have an effect the second time
    *   Ask yourself whether it makes any difference to be run more than once.
    *   ```python
        i = 7
        print(i)
        i = 7
        ```
7.  **Complex** Decision Trees
    *   Too long or deeply nested trees of `if/elif/else`
    *   Are all of the branches truly necessary?
    *   Can all of the branches be reached?
    *   Has every branch been tested?
8.  **Spaghetti Code**
    *   Heaps of meandering code without a clear goal
    *   Functions/objects used in inconsistent ways
    *   Many variables are used to keep track of
    *   Conditional statements with long, confusing Boolean expressions
    *   Boolean expressions expressing double negatives; ex. `if not undone: ...`
    *   Code that makes you say "It would be easier to rewrite this than to understand it"
9.  **Dead Code**
    *   Modules that are imported but never used
    *   Variables that are declared but never used
    *   Lines that are *never* run because they are placed in an impossible-to-reach location
        *   Code that follows a `return` statement
            *   ```python
                return value
                value += 1
                ```
        *   Blocks of code guarded by an impossible-to-satisfy logical test
            *   ```python
                two_bee = True
                if two_bee and not two_bee:
                    print("If can you see this message, it is time to get a new CPU")
                ```
            *   ```python
                counter = 100
                while counter < 0:
                    print(f"T minus {counter}...")
                    counter -= 1
                ```
    *   Functions that are defined but never called *may* or *may not* be dead code
        *   In **Code Libraries** it is normal to define functions that are not meant to be used in the library itself
            *   It is okay to keep these functions
        *   As an **Application** evolves, calls to some of its functions may be removed until only the function's definition remains
            *   Some programmers may keep these functions "just in case" they are needed again
            *   We don't do this at DuckieCorp because we have Git; if we ever need to recover that function, we can find it in the repo's history


<details>

<summary><h3>What can you do about these smells?</h3></summary>

0.  **Magic Numbers**
    *   Replace literals with CONSTANTS that have descriptive names
    *   Consult the documentation (if you're lucky) to learn what `256` means in its context
    *   Give the same number used in different contexts *different* names; the
        important thing is what `256` represents, not its actual value.
1.  **Global Variables**
    *   Passing parameters enables us to understand the flow of data into a function
    *   Returning values enables us to understand the flow of data out from a function
    *   When a global is used to enable a function to return more than one value (a necessary concession in some languages), make sure this is thoroughly documented.
2.  **Poorly-named** Identifiers
    *   Identifier names should strike a good balance between brevity and descriptiveness
    *   Consider a new name that is
        *   More accurate
        *   More descriptive
        *   Brief
    *   Rename identifiers that clash with language built-ins
3.  **Bad Comments**
    *   Write code that speaks for itself
        *   Rename variables and/or functions so the code becomes self-documenting
    *   Rewrite or remove comments that are incorrect or serve no useful purpose
    *   Delete obsolete remarks that no longer accurately describe the situation
    *   Delete blocks of commented-out code that the last guy didn't dare to throw away
        *   Big blocks of commented-out code clutters up the file and makes it hard to find what is important now
        *   This is why we use version control now
    *   Retain comments that explain *why* something is done in a particular way when they are still relevant
        *   Comments explaining *how* the code works are probably not necessary
    *   Programmers sometimes vent their frustration with snarky or vulgar comments; these add no value, are unprofessional and embarrassing, and only serve to demoralize maintainers
        *   When the author of a cringey rant didn't sign their screed, you can look them up with `git blame`
4.  **Too many** arguments
    *   Remove unused parameters; look for cases where placeholder values such as `False`, `None`, `NULL` or `0` are passed in
    *   Use default values for common cases
    *   Accumulate many parameters into one dictionary or object
5.  Function/Method that is **Too Long**
    *   Generally, a method longer than a dozen lines should make you ask yourself "can I split this into smaller, more focused pieces?"
    *   Does the method embody many disparate ideas?  Split into more focused pieces (divide the problem)
    *   When one method deals both with little nitty-gritty details *and* big-picture concepts, move the big-picture stuff up to the caller
6.  **Redundant Code**
    *   Remove extra lines of code that have no effect on the outcome
7.  **Complex** Decision Trees
    *   Are all of the cases really necessary?  Combine common cases into one branch.
    *   Handle the most likely cases earlier; in some languages this is actually faster but, more importantly, it is easier to read because what the developer is likely looking for comes first.
    * Use Boolean algebra to simplify complicated conditions into an equivalent but simpler form
8.  **Spaghetti Code**
    *   Learn what the code is trying to achieve
        *   Write Pseudocode with your Rubber Ducky
    *   Rewrite it with the end goal in mind
9. **Dead Code**
    *   Delete import statements that bring in modules that are never used in the program
    *   IDE's sometimes underline or highlight unused variables to draw your attention
    *   Use the editor's search feature to see if the only hits you find are in comments
    *   Delete statements that appear *after* a return statement (some languages treat this as a compile-time error)
    *   Delete statements occurring in an impossible-to-reach branch of an `if` statement
    *   Remove unreachable loops (i.e. `while i > 0` when `i` is always negative)
    *   Delete functions which are defined but never called (except when in a code library)

</details>

**Always test the code after cleaning it up to make sure that your changes actually make it better!**


## How will I know when to refactor?

There are two answers to this question:

0. If you are a **developer** the answer is *"any time I find a code smell"*
1. If you are a **project manager** the answer is *"when we can afford to"*,
   which is a long way of saying *"never"*

As an employee of DuckieCorp you have been tasked with taking a client's
project to the next level.  Getting there means adding new features and
possibly fixing bugs. Instead of starting from scratch and building the program
"the right way" you start from a working prototype that was hastily put
together.

*   For this assignment, it is desirable to begin from the starter code because
    the program is doing computations which you don't fully understand - it is
    easier to change an already existing program than trying to make a new one.
*   In other cases you will join a project that has been in progress for many
    years (or decades), and which is the combined effort of many developers.  A
    project of this scope may have cost hundreds of man-years of combined
    effort and is "too big to fail"; it would be far too expensive to scrap it
    and start over the "right way".

In either case, the deficiencies in the existing code base are obvious to
developers who desire to make things better. The project managers (PMs) who
decide how to allocate scarce development resources regard the state of the
source code as a case of "if it ain't broke, don't fix it".

From the perspective of the PMs, the re-writing working code from scratch
carries too many large risks:

*   Introducing new bugs
*   Re-introducing old bugs
*   Added delays
*   No guarantee that the new code won't become a mess of its own
*   The end-users will not appreciate the changes because they see the finished
    program, not the source code


The Project Managers' calculation goes like this:

*   In the worst case refactoring fails, wasting valuable time.
    The customer is upset that no improvements have been delivered.
*   In the best case your work produces neither new features nor performance
    boosts, upsetting the customer who expects results.

Thus the risks of refactoring completely outweigh having a cleaner code base.

Explaining that refactoring will lead to better productivity in the future or a
reduction of bugs in subsequent updates is a tough sell when considered against
these obvious and immediate risks.  Before you can get the go-ahead to refactor
it is imperative to provide assurances to project management that your efforts
cannot result in expensive and time-consuming setbacks.



## Should I refactor *and* add functionality at the same time?

(For example, within the same Git commit?)

**No!**

*   This can only increase the likelihood of introducing new bugs.
*   Either **refactor** the code or **enhance** the product.
    *   Never try to do both at the same time, it *never* turns out well.

Math analogy: You can only solve for one variable at a time.

*   Doing more things at once increases the likelihood that something goes
    wrong, and prevents you from conclusively indentifying the source of the
    problem.
    *   This is assuming that the problem has but *one* cause.  It could have
        arisen from *any* combination of the changes you made.
*   The increased complexity makes it harder to undo your mistake.


*Updated Wed Mar 22 13:03:32 MDT 2023*
