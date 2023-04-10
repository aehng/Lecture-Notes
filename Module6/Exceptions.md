# Exception Handling

*   [Two Approaches to Error Handling](#two-approaches-to-error-handling)
*   [Comparing The Two Approaches](#comparing-the-two-approaches)
*   [Pros & Cons of Exception Handling](#pros-cons-of-exception-handling)
*   [Exception Best-Practices](#exception-best-practices)
*   [Exceptions in Python](#exceptions-in-python)
*   [More reading](#more-reading)


Every line of code carries a risk that something could go wrong.  Murphy's law
dictates that if something can go wrong, it *will* go wrong.  Therefore,
responsible programmers must be prepared for any unfortunate event.


## Two Approaches to Error Handling

Broadly speaking, there are two approaches to handling problems that arise as a program runs:

0.  **Easier to Ask Forgiveness than Permission** (EAFP): Accept that things
    can and will go wrong, but that they are actually infrequent occurrences.
    Instead of dealing with problems as they come, group the cleanup code
    together in one, out-of-the-way location.  The main flow of the productive
    code is clear and easy to see.
1.  **Look Before You Leap** (LBYL): before proceeding on to the next statement
    in the program first check that the previous statement was successful.
    Errors are detected and handled immediately as they occur.  The resulting
    code is 50% productive and 50% error handling, all mixed together.
    Readability is hampered as it can be difficult to discern which lines of
    code progress the program toward its goal and which lines are present to
    clean up any messes that may occur.


### Easier to Ask Forgiveness than Permission (EAFP)

EAFP is achieved by the mechanism of exception handling.  In Python, this
facility is used with the `try/except/finally` keywords that precede an
indented block.

Like all nice things in programming it was [first developed in LISP](https://www.joelonsoftware.com/2003/10/13/13/)
in the 1960's.  Exception handling is common in recent high-level and
Object-Oriented programming languages.  It is seen as an improvement over the
older style of error handling characteristic of code from the 70's and 80's and
which is still common in languages such as C which don't have exceptions.  In
modern languages exception handling is the accepted practice that most folks
will expect you to use.

Exception handling lets you just write your code together in one paragraph and
handle the various problems at the bottom of the function.  Typically, the
function that causes a problem is responsible for dealing with its aftermath.
However, exception handling allows for errors to "bubble up" the call chain to
an outer function that is equipped to handle the problem.  Instead of handling
errors instantly as they come up, you have the option leave it to a part of the
program which is dedicated to cleaning up messes.


### Look Before You Leap (LBYL)

Lower-level programming languages (such as C, Pascal and Go) tend to follow the
LBYL philosophy, making error handing very explicit.

The alternative style, LBYL, is achieved by surrounding every line of code in
an `if/else` block to can handle the errors as they come.  The trouble with
this approach is that your error handling code is mixed in with the main idea
that the function embodies.  Reading this code is a bit confusing because you
are constantly switching between code that gets you closer to your goal, and
code that cleans up any messes that may occur.

Here is a snippet of C code that illustrates what
error-handling-mixed-in-with-the-main-idea looks like so you can appreciate how
convoluted it can make things.  This bit of code is a classic; it is from
[Hobbit's original implementation](https://seclists.org/bugtraq/1995/Oct/28) of
the `netcat` tool.

*Small tangent: Netcat is a very useful program; you should look it up if you
haven't heard about it before.  There are many versions of it out there, but I
think Hobbit's original source code is a great read.  You'll learn some cool C
tricks and get some insight into the mind of a member of the 90's hacker scene.
/tanget*

As you read this code don't worry too much about the weird syntax, variable and
function names.  Instead notice how the programmer has to write an `if`
statement after each assignment to test whether the assigned value is non-zero
or non-negative.  The functions `bail()` and `holler()` print error messages to
the screen; `bail()` also causes the program to quit.  There's even a `goto` in
there for good measure.  Very old-school!


```c
/* doconnect :
   do all the socket stuff, and return an fd for one of
	an open outbound TCP connection
	a UDP stub-socket thingie
   with appropriate socket options set up if we wanted source-routing, or
	an unconnected TCP or UDP socket to listen on.
   Examines various global o_blah flags to figure out what-all to do. */
int doconnect (rad, rp, lad, lp) {
    int nnetfd = socket (AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (nnetfd < 0)
        bail ("Can't get socket");
    if (nnetfd == 0)		/* if stdin was closed this might *be* 0, */
        goto newskt;		/* so grab another.  See text for why... */

    rr = setsockopt (nnetfd, SOL_SOCKET, SO_REUSEADDR, &x, sizeof (x));
    if (rr == -1)
        holler ("nnetfd reuseaddr failed");		/* ??? */

    rr = setsockopt (nnetfd, SOL_SOCKET, SO_REUSEPORT, &x, sizeof (x));
    if (rr == -1)
        holler ("nnetfd reuseport failed");		/* ??? */

    if (lad || lp) {
        x = (int) lp;
        /* try a few times for the local bind, a la ftp-data-port... */
        for (y = 4; y > 0; y--) {
            rr = bind (nnetfd, (SA *)lclend, sizeof (SA));
            if (rr == 0)
                break;
            if (errno != EADDRINUSE)
                break;
            else {
                holler ("retrying local %s:%d", inet_ntoa (lclend->sin_addr), lp);
                sleep (2);
                errno = 0;			/* clear from sleep */
            } /* if EADDRINUSE */
        } /* for y counter */
    } /* if lad or lp */

    if (rr)
        bail ("Can't grab %s:%d with bind",
                inet_ntoa(lclend->sin_addr), lp);
```


## Comparing The Two Approaches

Compare the two approaches by reading [two sets of
programs](./exceptions/README.md) written in C and Python.  These demo programs
implement an Echo client & server.  An Echo server receives messages from a
client program and sends them right back.  These two pairs of source code
implement the exact same programs using the same underlying functionality; the
C client can talk to the Python server and vice-versa.

Which error handling style do you find easier to read and understand?


## Pros & Cons of Exception Handling

Like all good things in programming, the subject of exception handling is a bit
of a [holy war](http://www.catb.org/jargon/html/H/holy-wars.html) with
passionate supporters and detractors.  Whether it's a good or bad thing is
entirely up to you and how you employ it:

### Exception Handling Pros

+   Exceptions separate error-handling code from the normal program flow and thus make the code more readable, robust, and extensible
+   Because `return` cannot be used from constructors, throwing an exception is the only clean way to report an error when initializing an object (i.e.  from a class's `__init__()` method in Python)
+   Exceptions are hard to ignore, unlike error codes
+   Exceptions are easily propagated from deeply nested functions
+   Exceptions can be, and often are, user defined types that carry much more information than an error code
+   Exception objects are matched to the handlers by using the type system


### Exception Handling Cons

-   Exceptions break code structure by creating multiple invisible exit points that make code hard to read and inspect
-   Exceptions easily lead to resource leaks, especially in a language that has no built-in garbage collector nor `finally` blocks
    -   This warning does not apply to Python
-   Learning to write Exception-safe code is hard
-   Exceptions are expensive and break the promise to pay only for what we use
    -   By "expensive" I mean that raising an exception costs more in CPU time and memory than not doing so
-   Exceptions are hard to introduce to legacy code


## Exception Best-Practices

-   Exceptions are easily abused for performing tasks that belong to normal program flow.
    -   Don't use exceptions for ordinary occurrences.
    -   There's a reason why they're called "exceptions" and not "ordinaries".
-   Don't adopt the habit of **Pokemon exception handling** (Gotta catch them all!).  Pokemon exception handling is when you write a bare `Except` statement which doesn't catch a specific type of exception.
    -   Instead, be as precise as possible when handling exceptions
    -   At the very least you will be able to write more helpful error messages
    -   Not all errors are created equal; while some can't be recovered from (i.e. out of memory, crucial file is missing or inaccessible), some can be mitigated
    -   Adopting a "one-size-fits-all" mentality defeats the purpose of this helpful language feature; you might as well call `sys.exit()` any time something doesn't go right in your program
-   Don't adopt the habit of *swallowing* exceptions:
    ```
    try:
        # Risky Buisiness up in here
        ...
    except:
        # Did something go wrong?  I'll never tell!
        pass
    ```
    -   Swallowing exceptions is bad because it masks the fact that the program is failing
    -   The underlying problem is not being addressed and worse, it might *never* be addressed because no indication of trouble is apparent
    -   The problem will continue to happen and nobody will be aware
    -   I've seen this *so* many times in production code.  When we confronted the problem and actually fixed the bug, the whole program *magically* became much faster.  Who knew that continually raising exceptions in a tight loop was detrimental to performance?


## Exceptions in Python

You've already been taking advantage of exceptions.  By allowing functions such as `open()` to crash your programs you are letting Python do the work of reporting errors in your code.

Exception handling will let you exert more control over the situation and prevent your program from crashing.  You can even recover from some kinds of errors.

As always, the official Python documentation is your best resource.

*   [Exceptions](https://docs.python.org/3/library/exceptions.html)
*   [Traceback](https://docs.python.org/3/library/traceback.html), a library that prints the stack trace of your program



Here is a passage of code that carries the possibility of raising an exception.  Can you count all of the ways this can fail?

```python
fname = None
f = open(fname)
print("You'll only see this message when everything is OK")
print(f)
f.close()
```

The provided filename may

0.  Refer to a directory instead of a file
1.  Name a file which does not exist
2.  Exist but the user lacks permission to access it
3.  Not be a string nor a non-negative integer
4.  Be a non-negative integer but refer to an invalid file descriptor (try passing arbitrary numbers to `open()`...)

Try finding values for `fname` that cause each of these problems on your computer.


### Being a try-hard

When a passage of code carries the possibility of raising an exception, create a `try/except` block.  Like other control structures in Python, the code contained within is indented by four spaces.

```python
fname = None
try:
    f = open(fname)
    print("You'll only see this message when everything is OK")
    print(f)
    f.close()
except:
    print(f"Well, opening {fname} didn't work for some reason")
```

This code doesn't crash.  However, the new error message is less informative than the stack trace; we know that opening `fname` "didn't work", but we can't tell *why*.  All errors are indistinguishable from each other.  We can do better.


### Get specific about your failures

Following `except` with the name of an exception class lets us select which code is run in response to particular types of errors.  Multiple types of exceptions may be selected by naming their types in a tuple.  In this example I treat `TypeError` and `ValueError` identically:

```python
fname = None
try:
    f = open(fname)
    print("You'll only see this message when everything is OK")
    print(f)
    f.close()
except PermissionError:
    print(f"I am not allowed to access {fname}")
except IsADirectoryError:
    print(f"Turns out that {fname} is a directory; weird!")
except (TypeError, ValueError):
    print(f"{fname} is not open()'s type of input")
except:
    print(f"Well, opening {fname} didn't work for some reason")

```

This approach lets us choose how we respond to an error.


### Tell me how you really feel

This version gives a distinct error message in *most* cases.  We can capture the exception object in a variable for further inspection by using the `as` keyword following the type of exception:


```python
fname = None
try:
    f = open(fname)
    print("You'll only see this message when everything is OK")
    print(f)
    f.close()
except PermissionError as e:
    print(f"I am not allowed to access {fname} because '{e}'")
except IsADirectoryError as e:
    print(f"Turns out that {fname} is a directory, see? {e}")
except (TypeError, ValueError) as e:
    print(f"{fname} is not open()'s type of input because '{e}'")
except:
    print(f"Well, opening {fname} didn't work for some reason")
```


### Order of Operations

In your first programming class you learned that the order that conditions are
written in `if` statements makes a difference.  This version of "Warmer and
Colder" has a bug that makes it unwinnable; it only ever says that a guess is
`Freezing` or `Absolute Zero`:

```python
 1	import random

 2	n = random.choice(range(1, 11))
 3	while True:
 4	    guess = input(f"[{n}] Guess the number between 1 and 10: ")
 5	    if not guess.isdigit():
 6	        print("That is not a number!")
 7	        continue

 8	    diff = abs(int(guess) - n)

 9	    if diff < 9:
10	        print("Freezing")
11	    elif diff >= 10:
12	        print("Absolute Zero")
13	    elif diff < 7:
14	        print("Cold")
15	    elif diff < 5:
16	        print("Lukewarm")
17	    elif diff < 3:
18	        print("Warm")
19	    elif diff < 2:
20	        print("Burning Hot!")
21	    elif diff == 0:
22	        print("You got it!")
23	        break
```

The error is that the test on line 9 is too general; it is true both when the
guess is spot-on and far away.  Because the program takes the first branch that
matches, control never reaches the winning test on line 21 and traps the player
in an infinite loop.

Exceptions are matched in the order their handlers are written, so care must be
taken so that a general test doesn't prevent a specific one from matching.
Python's exceptions are a family of objects related by inheritance.  An
`except` clause matches the type of exception specified *along with its
subclasses*.

Here is the [hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
of Python exceptions.  At the top of Python's exception family tree is a class
called `BaseException`.  Beneath it comes the `Exception` class.  Because
every Python exception descends from these two classes, you should put their
handlers at the very end of the list of exceptions. 

In this example the handler for `BaseException` comes first.  As a
consequence, this program only gives a vague error message:

```python
fname = None
try:
    f = open(fname)
    print("You'll only see this message when everything is OK")
    print(f)
    f.close()
except BaseException as e:
    print(f"Some error occurred: '{e}'")
except Exception as e:
    print(f"Well, opening {fname} didn't work for some reason: '{e}'")
except PermissionError as e:
    print(f"I am not allowed to access {fname} because '{e}'")
except IsADirectoryError as e:
    print(f"Turns out that {fname} is a directory, see? {e}")
except (TypeError, ValueError) as e:
    print(f"{fname} is not open()'s type of input because '{e}'")
```

All of the handlers following `except BaseException` are dead code that will
never be run, and no users will ever see their messages.  If you want to catch
`Exception` or `BaseException`, they need to be handled at the *end* of the
exception handling list.  A bare `except:` clause with no named exception or
variable catches `BaseException` and any descendants.  It is a syntax error to
put it anywhere besides the final position of the handler list.

You can use knowledge of the [exception
hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
to simplify exception handling logic.  If I wanted to treat `PermissionError`
and `IsADirectoryError` the same way I could combine them into one handler
with a tuple, as I did with `TypeError` and `ValueError`:

```python
except (PermissionError, IsADirectoryError) as e:
    print(f"I cannot access {fname} because '{e}'")
```

Or, I could rely on the fact that these are both subclasses of `OSError` and
write one handler:

```python
except OSError as e:
    print(f"The OS does not allow access to {fname} because '{e}'")
```

This is a good approach only when the response to both errors is identical.
If they demand different actions, you need to write separate handlers.


### Run this code or else!

The trouble now is that the final two lines of code are run even when they are not appropriate.  There are two ways to fix this:

0.  Move those two lines up into the `try` block
1.  Append an `else` clause to the `try/except` block which is executed when **no** exception occurs:

```python
fname = None
try:
    f = open(fname)
    print("You'll only see this message when everything is OK")
    print(f)
    f.close()
except PermissionError as e:
    print(f"I am not allowed to access {fname} because '{e}'")
except IsADirectoryError as e:
    print(f"Turns out that {fname} is a directory, see? {e}")
except (TypeError, ValueError) as e:
    print(f"{fname} is not open()'s type of input because '{e}'")
    exit(7)
except:
    print(f"Well, opening {fname} didn't work for some reason")
else:
    print(f"w00t! Nothing went wrong this time!")
```


### Finally, the last example

A `finally` clause may be added to contain code that should **always** run, regardless of any previous success or failure.

```python
fname = None
try:
    f = open(fname)
    print("You'll only see this message when everything is OK")
    print(f)
    f.close()
except PermissionError as e:
    print(f"I am not allowed to access {fname} because '{e}'")
except IsADirectoryError as e:
    print(f"Turns out that {fname} is a directory, see? {e}")
except (TypeError, ValueError) as e:
    print(f"{fname} is not open()'s type of input because '{e}'")
    exit(7)
except:
    print(f"Well, opening {fname} didn't work for some reason")
else:
    print(f"w00t! Nothing went wrong this time!")
finally:
    print("Big gulps, huh?  Welp, see ya later!")
```


### Raising exceptions in your own code

You don't have to only react to exceptions; you can sling them yourself!

As you saw in Assignment 4.1, the `raise` keyword along with the name of a class that derives from `Exception` any time you want to signal a problem that you cannot handle yourself.

The complete list of built-in exceptions is [here](https://docs.python.org/3/library/exceptions.html#concrete-exceptions)

The constructor for these classes take a string which is the message intended for whomever/whatever handles the error.

This also means that you can create your very own exception classes in situations where the defaults are insufficient.  Just define a child class of `Exception` (no imports necessary; this class is in the default namespace):

```python
class Derp(Exception):
    pass

raise Derp("I derped!")
```


## More reading

* https://www.codeproject.com/Articles/38449/C-Exceptions-Pros-and-Cons
* https://www.joelonsoftware.com/2003/10/13/13/
* https://softwareengineering.stackexchange.com/a/139179

*Updated Sun Apr  9 20:54:56 MDT 2023*
