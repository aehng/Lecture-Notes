# Solving Problems With Recursion

* [What is recursion, really?](#what-is-recursion-really)
* [Tips for thinking about problems recursively](#tips-for-thinking-about-problems-recursively)
* [V. Anton Spraul's "Big Recursive Idea"](#v-anton-sprauls-big-recursive-idea)
* [Practical considerations when using recursion](#practical-considerations-when-using-recursion)
* [Conquering Stack Overflow](#conquering-stack-overflow)


# What is recursion, really?

> In order to understand recursion, one must first understand recursion.


## The Droste Effect

*Recursion is characterized by repetition through self-reference*

* [The Droste Effect](https://en.wikipedia.org/wiki/Droste_effect)
* [Look at this recursion](https://www.youtube.com/watch?v=rDIos-t5Syo&feature=youtu.be&t=39s)
* [An old joke that never gets old](https://www.google.com/search?q=recursion)
* [Recursion on Wikipedia](https://en.wikipedia.org/wiki/Recursion_(computer_science))


Repetition is a fundamental technique of computation, and programming languages
typically give us many ways to express the idea of "do this thing N times" or
"do this thing until it is done".  Thus far in your studies you have been using
loops to achieve this.  Here is a Python function which uses a loop to compute
the Nth Factorial:

```python
def iterativeFactorial(n):
    print(f"At this call n = {n}")
    r = 1
    for i in range(1, n+1):
        r *= i
    return r
```


In this example the code is *explicit* about:

*   What happens at each iteration of the loop?
    +   `i` takes on a value from 1 to n inclusive
*   When does the program stop looping?
    +   When `i` becomes equal to `n+1`


But it isn't explicit about:

*   How does control go from the bottom of the loop back to the top?
    +   There's an *invisible* `goto` at the bottom of the loop

You've just come to accept that the amount of indentation controls the extent
of the loop, but you didn't have to tell the computer how to move from one
iteration to the next.

Using recursion means that we are explicit about everything that happens.

```python
def recursiveFactorial(n):
    if n <= 2:
        return n
    else:
        return n * recursiveFactorial(n - 1)
```


*   What happens at each iteration of the loop?
    +   Each time through the loop we either return `n`, or the product of `n`
        and `recursiveFactorial(n - 1)`
*   When does the program stop looping?
    +   When `n` becomes less-than-or-equal to 2
*   How does control go from the bottom of the loop back to the top?
    *   Repetition happens when we call `recursiveFactorial(n - 1)`

Instead of using the `range()` function to generate a list of numbers to loop
over, we start from `n` and count down with each successive call.


## Recursion: A beautiful and elegant way to solve all of life's problems

In the scheme of our problem-solving strategies, recursion best embodies the
strategy **Divide the Problem** by breaking a problem into do-able chunks.  Most
problems naturally contain smaller sub-problems.  Repeatedly solving these
smaller pieces is how we make progress.

Recursion means to apply a function repeatedly by calling itself from within
itself instead of using a loop to repeat the function's invocation.  With each
iteration of a loop we get one step closer to our desired solution.  Recursion
is the same, but instead of hitting the bottom of a loop we explicitly call a
routine to return to the beginning of the sequence of instructions we wish to
repeat.

In a recursive solution we use the program's call-stack as a data structure to
keep track of information needed by the computation as opposed to manually
maintaining this data.

Any iterative algorithm can be transformed into an equivalent recursive
algorithm and vice-versa, though going *from* iteration *to* recursion may
require the addition of an auxiliary data structure.  In general, a recursive
algorithm can be refactored into an iterative algorithm which uses an
explicitly managed **stack** data structure.


## When is it appropriate to use recursion?

> To iterate is human, to recurse divine. 
>   -- L. Peter Deutsch

**Q:** May we only apply recursion to problems which have the naturally
occurring property of recursion?

**A:** We can apply recursion to *any* problem for which it makes sense.

For some problems, like traversing a computer's directory structure or crawling
the web, a recursive solution just feels "natural".  At other times the
overhead of the call stack doesn't justify a recursive solution.

As with many of the things we've studied in this class, you get to make a
judgement call by weighing the pros and cons of either approach.  Knowing
*when* to do something is as important as knowing *how* to do it.


# Tips for thinking about problems recursively

*   **Start with what you know** - this means to identify the *base case(s)*.
    The base case(s) are states of the problem for which the answer to the
    problem is trivial.  In a *base case* no work needs to be done to return
    the right answer.
*   **Divide the problem** - this means to break the problem into smaller
    chunks and solve those first.  Discover operations which transform your
    current state into one that is one step closer to a base case.
*   **Reduce the problem** - add constraints to the problem such that you end
    up excluding extraneous, unnecessary details which complicate a recursive
    solution. Problems which may be divided into pieces which do not need to
    rely on each other's state are good candidates for a recursive solution;
    such recursive solutions could be run in a distributed system taking
    advantage of parallel processing.

When you realize that a `while` or `for` statement is playing two roles
(testing *and* repeating), it is easy to think about how you might separate
those tasks into two lines of code.  In this way you may easily express any
repetitive process as a *series of recursive function calls*.

On the other hand, for those problems which themselves embody recursion,
recursive solutions tend to be simpler and shorter than iterative solutions.

*   It is possible to create an iterative solution to any recursive problem.
*   To do so you must supply a data structure which fills the role of the call
    stack.
    *   But why should you do all of the extra work of keeping track of that
        information when your programming language will do it for free?



# V. Anton Spraul's "Big Recursive Idea"

## A.K.A. that weird recursion trick *they* don't want you to know

Recursion is hard to wrap your head around at first.  Be assured that learning
recursion is like riding a bicycle.  After you do it once, you'll always be
able to do it again.  Another thing that is to your advantage is that there is
a simple trick that you can employ to turn any iterative solution into a
recursive one.

In his book *Think Like a Programmer*, V. Anton Spraul introduces his **Big
Recursive Idea** (BRI):

> If you follow certain conventions in your coding, you can pretend that no
> recursion is taking place.

The BRI is to pretend that no recursion is actually taking place at all.  Until
recursive thinking becomes natural, begin by writing an iterative version of
the algorithm that works.  Then, piece by piece, transform it into a recursive
solution by creating a "middle-man" function and *tricking* it into becoming
recursive.

I'll illustrate by telling the story of two factorial functions, the
hard-working and industrious iterative factorial, and the lazy recursive one.

We begin with the industrious iterative Factorial function and verify that it
works to our satisfaction.

```python
def iterativeFactorial(n):
    print(f"At this call n = {n}")
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

>>> iterativeFactorial(0)
At this call n = 0
1

>>> iterativeFactorial(1)
At this call n = 1
1

>>> iterativeFactorial(2)
At this call n = 2
2

>>> iterativeFactorial(3)
At this call n = 3
6

>>> iterativeFactorial(4)
At this call n = 4
24

>>> iterativeFactorial(10)
At this call n = 10
3628800
```


Looks legit.  Next, we create a "middle-man" function which, true to form, is a
lazy bum who pawns the hard work off onto some sucker who will do it for less.

```python
def middleman0(n):
    print(f"I'm a lazy middle-man, and n = {n}")
    return iterativeFactorial(n)
```

The iterative function becomes annoyed that this useless middle-man is taking
credit for his hard work and complains to their boss.  The boss tells the
middle-man that in order to be a team player he must provide *some* value to
the company.

The middle-man decides that hard work is hard, but computing trivial values of
the factorial function (for inputs 0 and 1) is easy enough to not be beneath
his dignity, though he still pawns the heavy lifting off to the iterative
function.

```python
def middleman1(n):
    print(f"I'm a lazy middle-man, and n = {n}")
    if n < 2:
        return 1
    else:
        return iterativeFactorial(n)
```


The iterative function quickly realizes that the middle-man still does not add
any *real* value to the team (after all, it could already handle the trivial
base case by itself), and begins making impertinent remarks about the
middle-man function's provenance, work ethic, and worth to society at large.

Perhaps out of guilt, shame, or injured pride, our middle-man resolves to do at
least one *teensy* little bit of work by itself before foisting the rest of the
job on to the iterative function:

```python
def middleman2(n):
    print(f"I'm a lazy middle-man, and n = {n}")
    if n < 2:
        return 1
    else:
        return n * iterativeFactorial(n-1)
```

"Surely this will get everyone off my back!" the self-satisfied middle-man
function exclaims to himself.  But the other function is not impressed.
However, once the boss has seen that the middle-man is capable of doing that
one little bit of work, it's easy to see that it is perfectly capable of doing
a bit more.  This time, instead of letting the middle-man shirk its duty at the
expense of its more industrious co-worker, the boss forces the middle-man to
pawn its work onto *itself*.

```python
def middleman3(n):
    print(f"I'm a lazy middle-man, and n = {n}")
    if n < 2:
        return 1
    else:
        return n * middleman3(n-1)
```


Now you have a recursive function, and everybody lived happily ever after.


# Practical considerations when using recursion

## Wrapper functions

It is common for recursive functions to require lots of parameters.  Function
call parameters are the best way to get information into a recursive call,
preferable over global variables.   However, more parameters means added
complexity.  Many parameters must be given very particular values at the
initial recursive call or else the algorithm will return a wrong answer.

Instead of demanding that users memorize tedious details like "which parameters
take values of my choosing?" and "which parameters need to start off at 0 or
start with an empty dictionary?", you should provide a *wrapper* function.  A
wrapper function covers another function call like a wrapper over candy.
Existing only for the sake of convenience, a wrapper is a trivial function
which takes fewer parameters than the call it wraps, providing a simpler
interface to your recursive function.

Here's an example of a factorial function which takes two parameters, the
user's chosen N and an extra accumulator variable which should start at 1.
This algorithm will give the wrong answer if a value besides 1 is used in the
accumulator, so it is important to help users get this right.  The wrapper
function defined below ensures users always make the right call to
`tailFactorial()`:

```python
def tailFactorial(n, accum):
    """Tail recursive factorial algorithm: the final expression is a function call.
    Users ought not directly call this function.
    The parameter @accum should be set to 1 on the initial call.
    """
    if n < 2:
        return accum
    else:
        return tailFactorial(n-1, n * accum)


def factorialWrapper(n):
    """User-friendly interface to the tail-recursive factorial"""
    return tailFactorial(n, 1)
```


Wrapper functions are commonly used in conjunction with recursive functions
because the parameters to a recursive function carry vital information and it
is important that they do not begin with the wrong value.

As an alternative, you may use default function parameters in Python and other
languages which possess this feature.  You will want to make it clear to users
that they ought to leave this parameter alone.

```python
def tailFactorial(n, accum=1):
    """Tail recursive factorial algorithm: the final expression is a function call.
    The default parameter @accum should not be overridden by the user
    """
    if n < 2:
        return accum
    else:
        return tailFactorial(n-1, n * accum)
```


## Common recursion pitfalls

Programmers new to recursion make common mistakes while they are struggling
with the new and confusing concepts.  Be on the look out for these recursion
anti-patterns in your coding.


### Too many parameters

As explained above in the section about "Wrapper Functions", recursive
functions often require extra function parameters which were not needed in an
iterative algorithm.  This results from the recursive algorithm being explicit
about details that were implicit in the iterative algorithm.  Specifically,
details that were kept as local variables and loop indices in the iterative
algorithm are promoted to function parameters for the recursive formulation.

New programmers who sense this pattern have a tendency to promote *everything*
to become a function parameter.  This leads to an unwieldy design and more
confusion.

The rule of thumb to follow is:

> If it needs to change in order to get you closer to a base case, it should
> be a function parameter.

How do you identify variables which, by changing, gets you closer to the base
case?  Begin with V. Anton Spraul's **Big Recursive Idea** and starting at an
iterative algorithm.  As you convert it into a recursive algorithm
piece-by-piece pay strict attention to which variables are taking part in the
progression from input to base case.


### Global variables

Attempts to avoid the first pitfall often steers young programmers right into
this trap.  The trouble begins when an overwhelming temptation to simplify a
function's interface results in the storage of information outside of the
recursive function call.

When a recursive function relies on variables that were not explicitly passed
in as a parameter you lose out on one of the most useful aspects of recursion,
which is an automatically managed stack.  Bypassing your program's call stack
with global variables leads to algorithms with many subtle bugs that are
exceedingly difficult to locate and remove.  This problem only becomes worse as
the depth of recursion needed to solve the problem increases; if a recursive
function calls itself thousands of times, at which one of those calls did the
global variable take on a bad value?

As with other areas of programming you want to avoid globals at all costs.
Carefully consider what data is crucial to your algorithm and arrange for it to
ride along in a parameter.



## Head vs. Tail recursion

[Head and Tail recursion demo](./recursion/headTail.py)

Consider the differences of output when the order of the functions calls in
`rCount()` are swapped.

When the recursive call happens *after* printing `i`, the numbers appear in
ascending order.  When the recursion is the *last thing* done in the function
it is called *Tail* recursion.

When the recursive call happens *before* the `print()` in `rCount()` the output
appears in reverse order.  When the recursion happens *before* the main body of
processing in a function it is known as *Head* recursion.

It just so happens in this algorithm that the result of *head* recursion is
different from *tail* recursion, but for many algorithms the result is
unaffected by the type of recursion performed!


### Consider...

*   What's the difference to us?  Not very much, besides the result being
    backwards.  For a function such as `rFactorial()` the result does not
    change when the order of operations is reversed.
*   Is `rFactorial()` an instance of head recursion or tail recursion?  Is the
    call to `rFactorial()` the very last thing to happen in this function?  No,
    it isn't.  The multiplication of `n` with the result of the call to
    `rFactorial()` is the last thing to happen.  This function is *not* tail
    recursive.
*   How do we change the order of operations in `rFactorial()`?  By adding
    another parameter to the function that contains the partial product we can
    perform the multiplication *before* the recursive call.  We just need to
    make sure that this parameter is initialized to 1 before we call the
    function, or else we'll get a bad result.


## Mutual recursion

[Mutual recursion demo](./recursion/mutual.py)

A recursive function *may* call itself directly, but it doesn't have to.
"Mutual Recursion" happens when we have one function which calls another,
which ultimately results in the original function being called again.

Consider the functions `oddCount()` and `evenCount()`.  `oddCount()` calls
`evenCount()`, which in turn calls `oddCount()`, and so on.  

Because one function is head recursive and the other function is tail
recursive, we find an interesting pattern in the output.

* Which of `oddCount()` and `evenCount()` is tail recursive?  



# Conquering Stack Overflow

I think this is what most of you think using recursion is like:

[Look at this Blue Screen of DEATH](https://www.youtube.com/watch?v=L22keLHfEjc)

Some of you may be worried that recursion can use too much memory.  How many
recursive functions calls can a program make before this limitation becomes a
practical problem?  The answer is "it depends".

[Stack depth demo](./recursion/depthFinder.py)


#### Stack Overflow

A runtime error occurring when a program's call stack uses too much memory.

It is generally true that a series of recursive function calls which never
reach a base case will encounter an error called "stack overflow", where the
program's call stack grows so large as to exhaust all available memory on the
system.  How long this takes depends upon how much memory your computer has,
whether you're using head recursion or tail recursion as well as which
programming language you wrote the recursive routine in.


## Compilers and recursion

**Q:** Now that we've re-written the recursive factorial function in the file
[headTail.py](./recursion/headTail.py) to use tail recursion, what's the difference to us?

**A:** The function gained an extra parameter that we must remember to start
off at 1.  We can address this either with a wrapper function or with a default
parameter.  We still get the same answer, so it's not really a big difference.


**Q:** What's the difference to a compiler?

**A:** All the difference in the world!

Apart from the naturally recursive problem of compiling source code into a
program, what is the relationship between compilers and recursive programs?

You can find out what happens when we perform infinite recursion by playing
with the programs under the recursion/ subdirectory.

I have written the same program in 5 languages: Python, C, C++, Java and
Scheme.  You'll find the sources in [this directory](./recursion/song/).

To try out the Scheme program you will need to install the Chicken Scheme
interpreter.  On Debian-based Linux distributions you can install this by
running:

    $ sudo apt install chicken-bin

Or, you can download pre-built package for your OS from
https://wiki.call-cc.org/platforms



## Tail Call Optimization

**Q**: Can our compiler save us from running out of memory?
**A**: Yes! It's called "Tail-Call Optimization" (TCO).

When the very last thing which a recursive function has to do is make the call to itself, the compiler *may* treat the recursive call as a `goto` and jump back to the top of function, just as it would in an ordinary loop.  As it does so it updates the value of the function parameters, just as the variables in a for loop would be updated.

TCO happens out-of-the-box for the Scheme programming language.  In fact, TCO is a required part of the Scheme language.  As for the C language, both of the mainstream open source compilers (GCC and clang) are able to perform TCO.  The C++ compiler needs just a bit of coaxing to realize that it can safely perform TCO.

For languages without TCO, recursion should be used with care.  A deeply-recursive Python program (i.e. one that makes 1,000 recursive calls) just falls flat on its face.  Some languages such as Java and Go *intentionally* do not support TCO.  The reasons vary:

0.  Other design constraints make TCO too difficult to implement
1.  Debugging a TCO program is challenging because the call stack doesn't reflect the true state of the program (e.g. 1,000 recursive calls appear as only one call in a stack trace)
2.  Altering the call stack is something that malware can do; if the programming language legitimizes changing the call stack, then normal programs become indistinguishable from bad ones
3.  Inheritance can make it difficult for the compiler to know which method to recursively invoke

When a language or compiler performs Tail Call Optimization recursive calls occurring in tail position do not incur the penalties recursion is infamous for.  TCO gives you the best of both worlds!
