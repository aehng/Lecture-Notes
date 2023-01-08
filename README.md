# Sp23 CS 1440 Lecture Notes Repository

This git repository is your textbook for CS 1440.
Code examples written in class, demos and other important resources will be found here.


## How to use this repository

Clone the repository to your computer *(do this one time)*:

```
$ git clone https://gitlab.cs.usu.edu/erik.falor/sp23-cs1440-lecturenotes
```

I would like you to *experiment* with the demo programs I include in the lectures.  This is my invitation for you to change and/or break my code.  You can put all files in the repository back to their original state with this command:

```
$ git restore :/
```

Update your local repo with the latest notes *(do this after each lecture)*:

```
$ cd sp23-cs1440-lecturenotes
$ git restore :/
$ git pull origin master
```


## Table of Contents

*   Outline of [Topics in CS 1440](./Outline_of_Topics.md)
*   [What CS 1440 Is About](./What_CS_1440_Is_About.md)
*   [Required Reading Schedule](./Required_Reading_Schedule.md) for the course
*   Your Guide to [Using Git](./Using_Git/README.md)

### Module 0
01. [Monday, January 09](./Module0/Lec01-Mon_Jan_09/README.md)
	* [Get to know your professor](./Module0/Lec01-Mon_Jan_09/README.md#get-to-know-your-professor)
	* [You're hired](./Module0/Lec01-Mon_Jan_09/README.md#youre-hired)
	* [What CS 1440 is about](./Module0/Lec01-Mon_Jan_09/README.md#what-cs-1440-is-about)
	* [Problem-Solving Activity: When will you find time to sleep](./Module0/Lec01-Mon_Jan_09/README.md#problem-solving-activity-when-will-you-find-time-to-sleep)



## Creating a comprehensive study guide from individual lecture notes files

I have created a little tool to help you to easily find a topic when you don't
remember on which day it was covered or to create a study guide for an exam.

[concatenate.sh](./concatenate.sh) is a shell script that concatenates (joins)
all lecture note files found in this repository into one comprehensive file.
Only lecture notes named `README.md` are included; extra files such as code,
images and media are left out.

This program creates a read-only file called `all_notes.md`.

```
$ cd sp23-cs1440-lecturenotes
$ git pull origin master
$ ./concatenate.sh
```

`all_notes.md`  is marked read-only to remind you to not make any important
changes as they will be destroyed the next time you run `concatenate.sh`.
