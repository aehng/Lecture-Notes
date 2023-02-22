CS1440 - Wednesday, February 22 - Lecture 18 - Module 3

# Topics:
* [Announcements](#announcements)
* [Protip: colored diff output and what to do if diff says EVERY line is different](#protip-colored-diff-output-and-what-to-do-if-diff-says-every-line-is-different)
* [Objects and Classes](#objects-and-classes)
* [UML Class Diagrams](#uml-class-diagrams)


------------------------------------------------------------
# Announcements

## BSidesSLC Registration is Open!

*   **When**  Friday, April 14th - Saturday, April 15th
*   **Where** Conference Center at SLCC Miller Campus 9750 S 300 W, Sandy, UT
*   [**BSidesSLC Discord**](https://discord.com/invite/hBcnv9gb73).
*   **Cost**  
    *   General Admission $19 + taxes & fees
    *   General Admission + Electronic Badge $119 + taxes & fees
    *   [Tickets](https://www.eventbrite.com/e/bsidesslc-2023-tickets-527264701917)

![](./02-bsides-logo.png)


### BSidesSLC attendance replaces your lowest assignment/exam score

*   If you attend the conference I will replace your lowest assignment/exam score with **full credit**
    *   It is good enough if you can only make it one of the days, either Friday or Saturday
*   Either find me at the conference or send me a selfie your conference badge
*   *Note:* if you are enrolled in both of my classes this semester, you may replace a low score in only **one** class


## Free Software and Linux Club

*   **What**  Functional Programming with Elixir
*   **When**  6:30pm Thursday, February 24th
*   **Where** ESLC 053, [FSLC Discord server](https://discord.gg/GKWhbVDN38)

Are you interested in functional programming? What about the process of building, and deploying, distributed applications and systems?
Join us in exploring Elixir - a functional language - and the architecture of CheSSH (which you may review prior to the meeting at https://github.com/Simponic/chessh if you wish), a distributed multiplayer game of Chess over SSH!

Hope to see you there! 


# Action Items

*   You should be in the midst of phase **3. Testing and Debugging** *today*
    *   Continue your testing work *tomorrow*, taking care to document your test cases and their results
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Protip: colored diff output and what to do if diff says EVERY line is different

`diff` is a text tool that helps you compare two files.  You can use it to compare the output your program creates against the specimen supplied with the starter code.

`diff` has a lot of neat options for you to explore, but using it can be as simple as this:

```bash
$ diff [-u|-Z|--color=always] FILE0 FILE1
```

*   `diff` describes how the input files differ from one another
    *   If `diff FILE0 FILE1` results in *NO* output, that means the two files are **identical**
*   The `-u` flag is optional, but recommended.  It causes `diff` to display its output in the so-called *unified format*, which is the same format used by `git diff`
    *   `diff` is capable of producing output in many different formats
    *   The *unified format* is the easiest to understand


Suppose my Big Data program produced a report with *mostly* correct values.  `diff -u output.txt data/USA_full/output.txt` produces this output:

```diff
--- output.txt	2023-02-21 17:27:08.383713318 -0700
+++ data/USA_full/output.txt	2023-02-16 10:49:24.325990481 -0700
@@ -1,5 +1,5 @@
 [==========================================================]
-[ US BLS Quarterly Census of Employment and Wages for 2020 ]
+[ US BLS Quarterly Census of Employment and Wages for 2021 ]
 [==========================================================]
 
 Statistics over all industries
@@ -24,13 +24,13 @@
 Number of FIPS areas in report       1,627
 
 Total annual wages                   $111,505,515,321
-Area with maximum annual wages       "King County, Washington"
+Area with maximum annual wages       King County, Washington
 Maximum reported wage                $24,259,942,206
 
-Total number of establishments       54,993
-Area with most establishments        "New York County, New York"
-Maximum # of establishments          1,637
+Total number of establishments       54,994
+Area with most establishments        New York County, New York
+Maximum # of establishments          1,636
 
 Total annual employment level        535,426
-Area with maximum employment         "King County, Washington"
+Area with maximum employment         King County, Washington
 Maximum reported employment level    74,792
```

`diff` tells me how to make `output.txt` become the same as `data/USA_full/output.txt`.  By deleting lines that begin with `-` and adding lines beginning with `+`, then the files will become the same.


## How to read a unified diff

A unified diff is the format displayed by the `git diff` command.

*   The first two lines are the *header*, which names the two files being compared.
        *   The first file's name is preceded with `---`
        *   The second file's name is preceded with `+++`
*   Lines that begin and end with `@@` mark "hunks" (that's really the technical term)
        *   The numbers in between the at-signs locate that hunk within each file
*   Lines with a ` ` in the first column are **identical** in both files, and are presented for context.
*   Remaining output describes how to change the first file to become the same as the second:
    *   Lines with a `-` in the first column are **deleted** from the first file
    *   Lines with a `+` in the first column are **added** to the first file

Adding the option `--color=always` to the command makes `diff`'s output match Git's (tested on Mac and Linux).


## Windows users: diff says *every* line is different

Windows users may be seeing confusing output from the diff tool that tells them that *every* single line of their program's output differs from the example that I provided, even though there are no apparent differences.  This is not a problem on your part; it's just a quirk of your game console operating system.  The problem is that end of line (EOL) characters differ between the example files I gave you and what your program produces.

*   Linux and Mac: lines in text files end in `\n`
*   Windows: lines in text files end with `\r\n`

`diff` notices that your files have an extra `\r` that is not present in the files I provided.

You can fix this by giving `diff` the `-Z` option, which tells it to disregard differences in EOL characters:

```bash
$ diff --color=always -uZ output.txt data/USA_full/output.txt
```



# [Objects and Classes](../Objects_and_Classes.md)

Getting the design of a system right is the focus of this class.  Time spent upfront in the design phase saves much time later on in the testing and debugging phase.

Understanding what Classes and Objects are and their role in your software system is the key to a good design.



# [UML Class Diagrams](../UML.md)

The Unified Modeling Language is an important design-phase tool that helps you
capture the essence of an object-oriented system.  Creating a UML class diagram
early on will support your work in the later phases of the project, especially
the Implementation phase.



