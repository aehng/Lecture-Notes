# How and When to Comment

Comments can be a controversial subject.  Strongly-held opinions run the gamut from "always comment everything" to "comments are a code smell".  Here I offer some advice to help you decide what comments belong in your source code.


* [What is a "self-documenting" program?](#what-is-a-self-documenting-program)
* [Readability does make a difference](#readability-does-make-a-difference)
* [Are comments a blessing or a burden?](#are-comments-a-blessing-or-a-burden)
* [How to know when a comment is appropriate](#how-to-know-when-a-comment-is-appropriate)
* [Comment Do's and Don'ts](#comment-dos-and-donts)



## What is a "self-documenting" program?

*   A program which puts to good use identifiers which are required to be there anyway. By consistently applying a good naming scheme, you can help a human reader understand what the program is doing
*   Bugs are much easier to find in a program that adheres to the "self-documenting" principle.


### Example

This is a function from a real C program I once worked on which contains a bug.  Its job is to calculate the amount of liquid in a horizontal tank with hemispherical ends.

This is an example of [poor readability](./readability/poor.c).  Can you spot the bug lurking in that program?

[Here's a hint](https://math.stackexchange.com/questions/18914/horizontal-tank-with-hemispherical-ends-depth-to-capacity-calculation).

Here's the same function re-written to be a bit [better](./readability/better.c).


## Readability does make a difference

![One does not simply...](./assets/one_does_not_simply.jpg)

If you insist on using global variables, the least you can do is give them good
names!

![I, too, like to live dangerously](./assets/live_dangerously.png)



## Are comments a blessing or a burden?

There are two schools of thought regarding code comments.

### The more the merrier

+   Comments don't make a program run any slower, nor do they have any noticeable affect on compilation/run times (even if your source-code contains the entire text of War and Peace by Leo Tolstoy)
+   They can be used explain aspects of the program which cannot be made clear by reading the source code itself.  Concepts such as "why is this code written this way?" can explained by a comment.
+   Important information is immediately at hand.  Comments are the only place another programmer is guaranteed to see your wisdom.  Realistically, programmers are too lazy to bother with external documents, wikis or revision control histories.


### Comments considered harmful

+   Programmers forget to update comments in their own code, which gradually become obsolete over time.  Out-of-date comments can be worse than no comments at all.
+   For some reason programmers are loathe to change comments which they didn't write themselves.  We're perfectly comfortable re-writing your algorithm, but your comments on the algorithm are sacred.  It's weird, but you'll see this all the time.  Again, comments gradually drift into obsolescence .
+   With respect to ordinary users, you'll find no better hiding place for critical information than in the source code.



## How to know when a comment is appropriate

These comments are never appropriate:

```
// Holy crap, WTF is this?

// Drunk, will fix later

// Magic, do not touch

// I'm sorry...
```

Not only do these comments convey no useful information, they are discouraging!

Some programmers seem to regard comments as their personal Twitter account and overshare.  The new implementation of JavaScript's `left-pad` module is an example of going overboard with comments.  Did you really need to point out that `while (true)` is a loop?

* [On the web](https://github.com/left-pad/left-pad/blob/master/index.js)
* [Just the file](./readability/left-pad.js)


In response to code like the above, some programmers advocate to *never* use comments at all, instead relying on [Self Documenting Code](http://wiki.c2.com/?SelfDocumentingCode) to get their point across.

My recommendation lies in the middle of these two extremes and is based on the observation that executable code is a poor way to communicate the programmer's intent and rationale.

*   Let the code speak for itself.  Code can explain **what** is happening.
*   Use comments to explain **why** a particular approach has been taken.


## Comment Do's and Don'ts

**Don't** use a comment to describe what the code itself already explains:

```Python
i = 1337 # initialize i to 1337

# Make an XML Parse Tree from the data stream
xmlParseTree = makeXmlParseTree(dataStream)
```


**Do** write a comment when a fragment of code is used in an unexpected way to explain *why* you didn't write it in the most obvious way:

```C
// Intentional NOOP; delay for 3.5 milliseconds (assuming a 48MHz processor)
for (int j = 0; j <= 168000; ++j)
    ;
```


**Do** find a way to make a puzzling code fragment *self-documenting*.  For this snippet I still rely on comments to explain *why* I made some choices that seem arbitrary (CPU clock speed & disabling compiler optimizations).

```C
// This figure is derived from a CPU clock frequency of 48MHz
// Change this value when you switch to a microcontroller with a
// different clock speed
#define NANOSEC_PER_CLOCK_TICK 20.83333333333

/* Sleep for the given number of microseconds.
   We write our own implementation of this function because our standard
   library doesn't provide this function, and we don't have a timer to spare.

   IMPORTANT: This only works when compiler optimizations are disabled!
*/
void usleep(unsigned int microseconds) {
    int ticks = microseconds * NANOSEC_PER_CLOCK_TICK * 1000.0;

    for (int j = 0; j <= ticks; j++)
        ;
}
```

Later on in the program you can sleep for 3.5 milliseconds with this self-documenting line of code:

```
usleep(3500);
```


### It's always a good idea to [CodeForTheMaintainer](http://wiki.c2.com/?CodeForTheMaintainer)

> Always code as if the person who ends up maintaining your code is a violent psychopath who knows where you live.
