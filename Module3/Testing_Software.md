# Testing Software

* [Software Dependability](#software-dependability)
* [Failures vs. Faults vs. Errors](#failures-vs-faults-vs-errors)
* [How to Test Software](#how-to-test-software)
* [Types of Software Tests](#types-of-software-tests)


## Software Dependability

Trustworthiness of a computer system such that reliance can justifiably be
placed on the service it delivers.  Dependability can be measured in different
ways:

* Is the software *available*?
* Is the software *reliable*?
* Is the software *safe*?
* Is the software *secure*?


#### Available
Available software is functional and ready for use a high proportion of the
time.

Example: If a system responds to 99/100 requests at random intervals it is 99% available.


#### Reliable
Reliable software remains ready and functional over a long period of time.

Example: A system may crash for six minutes every hour.  Its availability is
90% even though it can only reliably run for ~54 minutes at a stretch.


#### Safe
A safe system avoids or prevents catastrophic consequences from happening to
the environment.

Example: If our regularly crashing system doesn't harm any people or other
systems when it crashes, it can be considered safe.  If it trips the circuit
breaker when it crashes it is unsafe because its crashes affect other systems
in its local environment.


#### Secure
A secure system prevents unauthorized access and/or handling of information.

Example: A system which refuses to return sensitive data in response to
unauthenticated requests is secure.


## Failures vs. Faults vs. Errors

The terms error, fault and failure are often used interchangeably, but do have
different meanings:


#### Software failure

Runtime behavior that is not expected.  A failure is the unacceptable departure
of a program operation from program requirements.



#### Software fault

A software defect that causes a failure to occur.



#### Software error

A specific problem in the code, the design, or requirements that lead to the
unexpected behavior.  A bug.  An error is usually a programmer action or
omission that results in a fault.

Not all errors cause a program to misbehave or fail to meet their user's
expectations.  In other words, code can be incorrect in ways that don't cause
noticeable problems to users.

* A software error == bug
* A software error != software failure



### What's the difference between these terms?

Consider this function `double()`, which ostensibly doubles its input value:

    # pre: n is a number
    # post: return the product of n multiplied by 2.
    def double(n):
        result = n * n
        return result


Upon running `double(3)` we find that it actually returns 9, but the post
condition says it should return 6.  Our expectation was not met, therefore this
software failed.

* The result `9` represents a *failure*.
* The failure is due to the *fault* at line 2 of `double` where `*` was used instead of `+`.
* The *error* is a typo (Erik typed `*` instead of `+` by mistake).


### Why have three different names for a "Bug"?

To communicate how precisely you know what the problem is.

*   *Failure* means you can tell something is wrong but you don't know the
    cause.
    +   "Users are complaining that program gives results that are *way* too
        large!"
*   *Fault* means you know what is causing the failure, but don't yet know why
    it's wrong.
    +   "I've narrowed the problem down to the `double()` function.  It is
        returning a value that is a lot larger than expected"
*   *Error* means you know why the fault occurred.
    +   "I found the bug!  Erik squared the input parameter instead of adding
        it with itself.  Maybe he was distracted by a passing firetruck?"

You could ask "But why did Erik make that typo?", but that gets into human
factors and is out of the scope of the present discussion.

*Adapted from an answer on [Stack Overflow](https://stackoverflow.com/a/47963772)*



## How to Test Software

Software testing is how developers *validate* and *verify* a system.  Through
testing developers try to uncover software failures.  Software testing should

*   Be systematic
*   Be repeatable
*   Cover whatever is being tested

Don't get you're hopes up too high, though:

> Testing shows the presence, not the absence of bugs
>
> -- Edsger W. Dijkstra
> [http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1969.PDF](http://homepages.cs.ncl.ac.uk/brian.randell/NATO/nato1969.PDF) p. 16


### Verification and validation (V&V)

The process of determining whether the requirements for a system or component
are complete and correct, the products of each development phase fulfill the
requirements or conditions imposed by the previous phase, and the final system
or component complies with specified requirements.

*Companies that hire from USU have been known to quiz applicants on these two
concepts!*


#### Verification

This process aims to answer the question "is my program doing the thing right?"

> The process of evaluating a system or component to determine whether the
> products of a given development phase satisfy the conditions imposed at the
> start of that phase.
>
> IEEE Standard Computer Dictionary

A verified program performs its functions correctly and without error.


#### Validation

This process aims to answer the question "is my program solving the right
problem?"

> The process of evaluating a system or component during or at the end of the
> development process to determine whether it satisfies specified requirements.
>
> IEEE Standard Computer Dictionary

A valid program meets the customer's needs as described by their requirements
and specifications.


Validation and verification are subtly different.  It is possible for an
program to be verifiable even if it isn't a valid solution to the customer's
problem.

Suppose I set out to write a function to find the area of a circle:

```python
def area(radius):
    PI = 3.141592653589793
    return 2.0 * PI * radius
```

Validation asks "is my code doing the right thing?"

This function is not valid because it returns the circumference instead of the
area.  It does compute the circumference correctly and we can *verify* that
there is no error in the code.  But the fact that it computes the circumference
correctly is immaterial because it isn't doing the right thing to begin with;
it is an *invalid* solution to the problem at hand.

Now consider this function:

```python
def circumference(radius):
    PI = 3.2
    return 2.0 * PI * radius
```

It is "valid" because it at least purports to compute the circumference.  But
it fails to do it right.  This failure should be noticed during the process of
verification.



### Where does debugging fit in to this scheme?

The process of finding the causes of software failures and then correcting
those errors.

-   **Testing**: what is wrong?
-   **Debugging**: why is it wrong, and how may I fix it?

Debugging happens *after* software testing uncovers failures.  We don't debug
to find failures, we test to find failures.

Once failures are discovered through testing debugging may be used to uncover
the *faults* and *errors* giving rise to the failure.



###  I'm sold. How do I test?

There are many different methods for software testing which vary by:

-   what they try to verify
-   how to approach the testing activity
-   which kinds of errors that they can uncover


Remember that no testing method will uncover all possible types of errors in
all programs.  By saying "this software is bug-free" you are asking your
listener to trust that you have proved a negative (*hint: you haven't*).

The key to testing is to wisely choose one or more testing methods that are
appropriate to the kind of software you are building, and pursue them until you
are sufficiently confident that you have validated and verified the software.



## Types of Software Tests

As you can see, there is a lot of jargon surrounding this topic.  This is a glossary of the most important terms you need to know.

#### Test Case

Inputs, conditions, and expected outputs of a piece of software.


#### Test Suite

A collection of test cases, related to a function or feature.


#### Manual Testing

Human testers run through a test suite looking for unexpected behavior.


#### Automated Testing

The test suite is a program which can detect unexpected behaviors, and may be
run by a computer.


#### Unit Testing

Fine-grained test cases designed to exercise the fundamental units of your
program; most often this means testing individual functions/methods.


#### Integration Testing

Testing two or more parts of a system together with a focus on detecting
unexpected behavior in the interactions between the parts.


#### System Testing

Testing the entire software system as a whole - at the opposite end of the
granularity spectrum from Unit Testing.  The most integrated of tests.


#### Non-Functional Testing

Tests with a focus on the non-functional aspects of a system (did the system
become slower, less usable, stable, or secure?), rather than on the measurable
functionality that a Unit Test would cover.


#### Regression Testing

Ensuring that a new software change hasn't created new problems or
re-introduced old problems.


#### Smoke or Sanity Testing

A quick, cursory test to make sure that the important aspects of a system are
stable, and that the system may be subjected to more thorough testing.  (e.g.
did the build succeed without errors, does the program even launch, did that
fix work or make things seriously worse, etc.)

Some sources make a distinction between these two types of testing, but for our
purposes we'll just consider these to be simple, informal tests.
