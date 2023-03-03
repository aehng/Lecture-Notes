CS1440 - Friday, March 03 - Lecture 22 - Module 3

# Topics:
* [Announcements](#announcements)
* [Discuss Brooks' "Passing the Word"](#discuss-brooks-passing-the-word)
* [Software Testing Jargon Activity](#software-testing-jargon-activity)
* [Validation vs. Verification](#validation-vs-verification)
* [Types of Software Tests](#types-of-software-tests)
* [How Gamers Killed Ultima Online's Virtual Ecology (~8 mins)](#how-gamers-killed-ultima-onlines-virtual-ecology-8-mins)


------------------------------------------------------------
# Announcements

## Spring break is next week

Enjoy your time off!


## BSidesSLC Student Scholarship

As a way to get more people excited about cybersecurity, we will be awarding *complimentary registration* (non-electronic badges) to a limited number of student applicants. Be sure to submit your application between February 18 and March 18 at 11:59 PM MT!

*   **Due**   Saturday, March 18
*   **Where** [Google Docs Form](https://docs.google.com/forms/d/e/1FAIpQLScGA4stAQJASrG63AU-Ejh3Dl3T9GVuQvWp1LvpccDegsVTuw/viewform?mc_cid=f5a09fe30c&mc_eid=9b0796ddc7)
*   **Terms**
    - Failure to follow instructions will result in disqualification.
    - All submissions must be in English. Sorry we can not support other languages at this time.
    - Students do not need to provide proof of enrollment unless contacted by BSidesSLC for potential award. 
    - Passes awarded as part of this Scholarship program are non-transferable and may not be sold, exchanged or redeemed for any cash value.
    - All Scholarship recipients are responsible for their own travel, food, and lodging.


# Action Items

*   *Today* you should finish phase **1. Design** of the assignment
    *   Be ready to move on to phase **2. Implementation** *early in the week after Spring Break*
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Discuss Brooks' "Passing the Word"

<details>
<summary><strong>What is the big idea Brooks wants to get across?</strong></summary>

*   Documentation is an important part of a healthy and complete programming
    product.
*   The manual should be written with the end-user in mind; Explain what the
    user will see, no more, no less

</details>


<details>
<summary><strong>How does this concept relate to the "Programming Product" we discussed in "The Tar Pit"?</strong></summary>

*   A program without a manual isn't a "Product"

</details>


<details>
<summary><strong>Who (or what) is the intended audience of our programs?</strong></summary>

*   People are, just as much as machines

</details>


<details>
<summary><strong>What are advantages of defining a system formally before creating it?</strong></summary>

*   System has a unified purpose, less rough edges
*   Some careful thought was spent on it

</details>

<details>
<summary><strong>What are advantages of using an implementing of a system as its own formal definition?</strong></summary>

*   Offers a final answer to obscure questions
*   Spend less time on documentation, more time on writing code

</details>

<details>
<summary><strong>What is the value of Flow-Charts?</strong></summary>

*   Despite being invented by real-life wizard John von Neumann, they lost much
    of their utility by the time structured programming languages were created
*   Despite their visual similarity, UML class diagrams *are not* flow-charts.
    *   A flow chart describes the flow of control in a running program.
    *   UML Class diagrams, apart from the distinction between dependency and
        associations, don't have too much to say about the runtime behavior of
        programs.

</details>



# Software Testing Jargon Activity

*   Split into groups based upon the color of paper you picked up as you walked in
    *   Discuss your topic within your group for a few minutes
    *   After the time is up, split up and form *new* groups which are a *mixture* of the former Blue and Red groups
    *   Teach your counterparts from the opposite group about your topic


<details>
<summary>Blue Group: Dependability</summary>

## [Software Dependability](../Testing_Software.md#software-dependability)

Laprie J.C. (1992) Dependability: Basic Concepts and Terminology. In: Laprie
J.C. (eds) Dependability: Basic Concepts and Terminology. Dependable Computing
and Fault-Tolerant Systems, vol 5. Springer, Vienna

> **Dependability** is defined as the trustworthiness of a computer system such
> that reliance can justifiably be placed on the service it delivers [Car 82].
> The service delivered by a system is its behavior as it is perceived by its
> user(s); a user is another system (human or physical) which interacts with
> the former.
>
> Depending on the application(s) intended for the system, different emphasis
> may be put on different facets of dependability, i.e. dependability may be
> viewed according to different, but complementary, properties, which enable
> the attributes of dependability to be defined:
>
> * with respect to the readiness for usage, dependable means **available**;
> * with respect to the continuity of service, dependable means **reliable**;
> * with respect to the avoidance of catastrophic consequences on the
>   environment, dependable means **safe**;
> * with respect to the prevention of unauthorized access and/or handling of
>   information, dependable means **secure**.


## Explain the following in your own words

0.  What does **available** mean to you?
    *   Usable in multiple ways
        *   If I can't use it, it's not available to me
        *   Undocumented code may be unavailable
        *   JS code isn't available to a Python user (you'd have to translate it first)
    *   downloaded & installed
    *   If the amazon cloud is down, that cloud app is **not** available
1.  Give an example of software that needs to be **available**
    *   Canvas
    *   Your OS
    *   Your browser
2.  How does **reliable** differ from **available**?
    *   Reliable code is consistent
    *   Reliable code must be consistently available
    *   Think of the uptime - how long does it run before crashing
3.  Devise an example illustrating the difference between **reliable** and **available**.
    *   If you're lactose intolerant, milk is always *available*, but you won't have a *reliable* experience if you drink it
4.  How does **safe** differ from **secure**?
    *   Safe software doesn't destroy things if/when it crashes
    *   Secure software keeps external bad actors out
    *   Secure software prevents unauthorized users from performing certain actions
5.  Devise an example illustrating the difference between **safe** and **secure**.
    *   If malware causes your *web browser* to crash, resulting in a minor inconvenience, it is **safe** but not **secure** (unauthorized user made it crash, but nothing was permanently damaged as a result).
    *   If malware causes your Bluetooth-connected *insulin pump* to crash, resulting in a trip to the ER, it is **unsafe** as well as **insecure**

</details>



<details>
<summary>Red Group: Failures, Faults and Errors</summary>

## [Failures vs. Faults vs. Errors](../Testing_Software.md#failures-vs-faults-vs-errors)

Laprie J.C. (1992) Dependability: Basic Concepts and Terminology. In: Laprie
J.C. (eds) Dependability: Basic Concepts and Terminology. Dependable Computing
and Fault-Tolerant Systems, vol 5. Springer, Vienna

> A system **failure** occurs when the delivered service no longer complies
> with the **specification**, the latter being an agreed description of the
> system's expected function and/or service.  An **error** is that part of the
> system state which is liable to lead to subsequent failure: an error
> affecting the service is an indication that a failure occurs or has occurred.
> The adjudged or hypothesized cause of an error is a **fault**.
>
> The development of a dependable computing system calls for the *combined*
> utilization of a set of methods which can be classed into:
>
> * **fault prevention**: how to prevent fault occurrence or introduction;
> * **fault tolerance**: how to provide a service complying with the
>   specification in spite of faults;
> * **fault removal**: how to reduce the presence (number, seriousness) of
>   faults;
> * **fault forecasting**: how to estimate the present number, the future
>   incidence, and the consequences of faults.
>
> Fault prevention and fault tolerance may be seen as constituting
> dependability **procurement**: how to *provide* the system with the ability
> to deliver a service complying with the specification; fault removal and
> fault forecasting may be seen as constituting dependability **validation**:
> how to *reach confidence* in the system's ability to deliver a service
> complying with the specification.


## Explain the following in your own words

0.  What is a **failure**?
    *   Software doesn't meet specifications (or expectations)
    *   The user experiences this
1.  What is a **fault**?
    *   The cause of the failure
    *   The underlying problem
    *   The developer will be able to find this (hopefully)
2.  What is an **error**?
    *   The specific part of the program that gives rise to a fault
3.  What is the **specification** of a piece of software?
    *   A document describing in great detail what the
4.  How do **failures** and **errors** differ from **faults**?
    *   Failures are externally manifested to the users
    *   A fault is what I think went wrong
    *   An error is the line(s) of code I can point to as being incorrect
5.  Why is it difficult for a system to comply with its specification?
    *   We're human, so we're bound to miss something
        *   Both while writing the specification, as well as writing the code

</details>



# [Validation vs. Verification](../Testing_Software.md#software-testing)

When testing our software we are on the lookout for failures.  Code failures can be detected with unit tests, but are not the only ways a system can fail us.  We face deeper problems when the very design of the system is incorrect.

The terms "Validation" and "Verification" help us distinguish between design flaws and coding errors.

While debugging is an important part of the process, it can't be applied until a failure has been noticed.  A coding error, once identified, is often easily fixed.  A design error, on the other hand, may send you back to the drawing board.



# [Types of Software Tests](../Testing_Software.md#types-of-software-tests)

There is a lot of jargon surrounding this topic.  This is a glossary of the most important terms you need to know.



# How Gamers Killed Ultima Online's Virtual Ecology (~8 mins)

When creating Ultima Online, Richard Garriott had grand dreams. Richard and Starr Long planned on implementing a virtual ecology into their massively multiplayer online role-playing game. It was an ambitious system, one that would have cows that graze and predators that eat herbivores.

[How Gamers Killed Ultima Online's Virtual Ecology | War Stories | Ars Technica](https://www.youtube.com/watch?v=KFNxJVTJleE)


<details>
<summary><h2>The moral of the story</h2></summary> 

Testing is good but you may still be woefully unprepared for the realities of the production environment.  Due to the sheer scale of the user base combined with their unique perspectives, your in-house tests will not address the issues they will discover.

Despite your best efforts, there are problems with your system that you'll just never discover until it becomes heavily used.

*   Scale of data; number of files, records as well as the sheer volume of data
*   Scale of network I/O
*   Scale of concurrent users
*   Your users will do things with your system that neither you nor your testers imagined possible
*   Beta-tests involving a sizable subset of your user base is one way to grapple with this problem.

</details>



