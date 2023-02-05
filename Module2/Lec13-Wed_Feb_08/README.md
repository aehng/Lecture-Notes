CS1440 - Wednesday, February 08 - Lecture 13 - Module 2

# Topics:
* [Announcements](#announcements)
* [Python's Built-in Data Structures](#pythons-built-in-data-structures)
* [Which data structure will give me the best performance](#which-data-structure-will-give-me-the-best-performance)
* [When should I use an *unordered* collection](#when-should-i-use-an-unordered-collection)


------------------------------------------------------------
# Announcements


# Action Items

*   You should be in the midst of phase **3. Testing and Debugging** *today*
    *   Continue your testing work *tomorrow*, taking care to document your test cases and their results
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# [Python's Built-in Data Structures](../Python_builtin_data_structs.md)

In Assignment #3 you'll need the right data structure for the job.  Let's see what Python has to offer.

## Mud cards in Erik's section

*   Write your name and A number at the top of your mud card
*   As we discuss this topic, please jot down any thoughts & questions that come to your mind



# Which data structure will give me the best performance?

Knowing what to do to make your program faster largely comes down to *experience*.

You need to gain a good understanding of

0.  What your program is doing
1.  How often it is doing it, and
2.  The relative expense of each operation

You don't want to optimize the wrong thing!

> Premature optimization is the root of all evil
>
> Donald Knuth

https://en.wikipedia.org/wiki/Program_optimization#When_to_optimize

Consider the case of the [Smart Caesar Cipher](./36-smart_caesar/README.md)

See the section about [Sets and Dictionaries](../Python_builtin_data_structs.md#sets-and-dictionaries) in this module's resources.


#### Storage Hierarchy

Storage is a trade-off between speed, size and cost.  The storage devices at the top are *smaller*, *faster* and *more expensive per byte* than those at the bottom:

0. CPU registers
1. CPU cache
2. Main memory (RAM)
3. Solid-State Disk (SSD)
4. Magnetic Disk (Hard Disk)
5. Optical Disk (DVD, CDROM, etc.)
6. Magnetic Tapes


## Mud card deep-thoughts

*   Given that both traditional hard disks and SSDs are slower than RAM, how many times should you read through your CSV files in Assignment #3?
*   In a language like Python, how might you ensure that your data stays in the CPU cache?

![./36-head-explode-headache.gif](./36-head-explode-headache.gif "Hmm... hmmmmmmm...")



# When should I use an *unordered* collection?

I introduced the *dictionary* collection and demonstrated how it can make a program faster.  But don't think that converting a list into a dictionary will magically make *every* program faster.

### You should use a *dictionary* when...

*   You need to keep track of pieces of information that can be recalled by a *name* or a *key word*
    *   If information can be indexed by *consecutive integers*, a list is more appropriate
        *   If the indices are consecutive but don't start at `0`, you can always add an *offset* value
    *   If there are *irregular* gaps between numbers, a dictionary will be more efficient
*   The *order* which the data has been encountered doesn't matter
    *   E.g. it doesn't matter which item is *first* or *last*
    *   E.g. you are indifferent to whether one item is *before* or *after* another item
*   The *frequency* which the data has been encountered matters
    *   e.g. the piece of data is the *key*, the number of times it has been seen is the value


### You should use a *set* when...

*   You need to quickly determine whether a piece of information is *present or not*
*   The *order* or *frequency* which the data has been encountered doesn't matter


### You should use a *list* when...

*   The *relative position* of pieces of information is important
    *   The information can be indexed by *consecutive integers* beginning from `0`, and without big gaps
        *   (If the indices are consecutive but don't start at `0`, you can always add an *offset* value)
*   A number is an appropriate index *and* you don't have a lot of gaps between data


The way Assignment #3 asks you to use FIPS codes and their corresponding human-friendly labels from `area_titles.csv` is the *perfect* use-case for a dictionary.



