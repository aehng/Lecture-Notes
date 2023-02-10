CS1440 - Friday, February 10 - Lecture 14 - Module 2

# Topics:
* [Announcements](#announcements)
* [Demo: Making a dictionary out of favorite_colors.dat](#demo-making-a-dictionary-out-of-favorite_colorsdat)
* [`eval()` is evil](#eval-is-evil)


------------------------------------------------------------
# Announcements

## Science Unwrapped: Computing with Honeybees

*   **What**  USU computer scientist Vladimir Kulyukin presents "Music, Traffic, Solar Harvests: Computing with Honeybees"
*   **When**  7:00pm Friday, February 10th
*   **Where** ESLC 130

Computation can unlock mysteries of honeybee behavior, how the bees' environment affects how they live, along with the "music" of bees' buzzing. Learn now artificial intelligence can transform hives into robots to monitor the health of these important pollinators.

Dr. Kulyukin will speak for about half an hour and then invite questions from the audience. Afterwards, enjoy refreshments and hands-on STEM learning activities provided by student and community groups in the ESLC atrium.


## Build yourself a website and Git a job

*   **When**  5 - 7pm Monday, February 13th
*   **Where** Old Main 407 (the CS Lounge)
*   **What**  ACM Club online portfolio tutorial night
    *   Learn how to host an online portfolio website, on your own domain, that shows off your work
    *   A hiring manager from Lucid will tell you how to make your digital portfolio stand out from the rest
    *   Free pizza!


# Action Items

*   Complete phases **4. Deployment** and **5. Maintenance** *today* 
    *   Make your final push to GitLab early so you have plenty of time to **verify** your submission
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Demo: Making a dictionary out of favorite_colors.dat

The file [favorite_colors.dat](./favorite_colors.dat) is a tab-separated text
file that contains some students names and their favorite colors.  Its form is
similar to that of `area_titles.csv` in the upcoming homework assignment.

Write a program called `make_dict.py` that reads data from the file
`favorite_colors.dat` and puts it into a dictionary called `students`
for processing.

Using `colors` complete these tasks:

0. Create a dictionary called `students` from 'favorite_colors.dat'
1. Print the number of pairs in the dictionary `students`
2. Print the dictionary `students` all at once
3. Print pairs one-by-one, by key
4. Print only certain keys
5. Safely check whether a key exists
6. Safely retrieve a value from `students`, getting a default otherwise
7. Reverse the mapping: Create a dictionary called `colors` associating colors to students who like it

Instructor's solution: [make_dict.py](./make_dict.py).



# `eval()` is evil

The `eval()` function is tempting because it can make certain tasks very easy.  However, this convenience comes at a cost: any program that uses `eval()` unwisely introduces a serious security vulnerability.  Programs that use the `eval()` function to process *data provided by users* falls victim to the "eval injection" class of security vulnerabilities.  The list of software that has succumbed is [long and distinguished](https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=eval+injection).  It is my wish that **none** of my students ever make this list.  You can avoid landing on this hall of shame by refusing to use `eval()` in your programs.


## What's the big problem?

Would you let any rando from the internet run any code they want on *your* computer?  Because that's what you are doing when you use `eval()` in your program.

The `eval()` function is dangerous because it is *powerful*.  `eval()` executes its string parameter as though it were normal source code.  It does not pause to check whether the code inside the string is a good idea.  If that string can be influenced by a user in any way, it will eventually be used against any computer that runs your program.  This will happen because, given enough time, your program will eventually be used by a bad actor who wants to subvert other people's computers.  Do not be the careless person who leaves the backdoor open.

![./54-simpsons-security.gif](./54-simpsons-security.gif "As useful as a screen door in a battle ship!")

Besides converting user input from `str` to other data types, `eval()` is most often used by naïve programmers to create new variable names on the fly.  In 100% of cases this is unnecessary because there are better ways achieve this effect (see below).

In Python you must also reject `eval()`'s evil stepmother `exec()`.  It is less well-known than `eval()`, but has far fewer restrictions on its capabilities.



## Danger zone

Convert the `cat` text tool into a `sum_csv` tool that relies on `eval()` to convert strings to integers.  The `sum_csv` text tool sums the numbers for each line of a CSV file, for the entire file, as well as the grand total across all input files.

Run `sum.py` using these [crafted files](./evil-eval/) to illustrate the problems with `eval()` and `exec()`.


## What can I do instead of `eval()`?

0.  Use a function that parses user input *without running it like code*.
    *   In Python this means avoiding the functions `eval()` and `exec()`
    *   If you are expecting a number, use `int()`, `float()` or `complex()` instead of `eval()`
1.  If you think you *must* use `eval()`, you need to manually scan **all** user input and *reject* everything that is even slightly suspicious
    *   This task is more subtle and tricky than you think
        *   Techniques like *Regular Expressions* help make it tractable
    *   You have to take a very big step back when thinking about what type of data your program might encounter
        *   As the author of the program you naturally have a very big blind-spot when it comes to what data users might supply
        *   Enlist the help of outsiders to help you think of test cases
    *   Even if you aren't using `eval()` yourself, you may still need to be this careful with user-controlled input anyway
2.  If `eval()` is used in your program to create new variables at runtime, stop what you're doing and **use a dictionary** instead
    *   **Everything** you want to do with runtime-defined variables can be done better and more safely with a dictionary



