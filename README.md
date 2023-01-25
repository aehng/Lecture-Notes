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

<details>
<summary><h3>Module 0</h3></summary>

01. [Monday, January 09](./Module0/Lec01-Mon_Jan_09/README.md)
	* [Get to know your professor](./Module0/Lec01-Mon_Jan_09/README.md#get-to-know-your-professor)
	* [You're hired](./Module0/Lec01-Mon_Jan_09/README.md#youre-hired)
	* [What CS 1440 is about](./Module0/Lec01-Mon_Jan_09/README.md#what-cs-1440-is-about)
	* [Problem-Solving Activity: When will you find time to sleep](./Module0/Lec01-Mon_Jan_09/README.md#problem-solving-activity-when-will-you-find-time-to-sleep)
02. [Wednesday, January 11](./Module0/Lec02-Wed_Jan_11/README.md)
	* [Be The Designated Questioner](./Module0/Lec02-Wed_Jan_11/README.md#be-the-designated-questioner)
	* [Setting up your computer for DuckieCorp](./Module0/Lec02-Wed_Jan_11/README.md#setting-up-your-computer-for-duckiecorp)
	* [Assignment #0: Shell Tutor](./Module0/Lec02-Wed_Jan_11/README.md#assignment-0-shell-tutor)
	* [Why are we learning an interface straight out of the 70's](./Module0/Lec02-Wed_Jan_11/README.md#why-are-we-learning-an-interface-straight-out-of-the-70s)
	* [Unix command line basics](./Module0/Lec02-Wed_Jan_11/README.md#unix-command-line-basics)
03. [Friday, January 13](./Module0/Lec03-Fri_Jan_13/README.md)
	* [Using Git at DuckieCorp](./Module0/Lec03-Fri_Jan_13/README.md#using-git-at-duckiecorp)
04. [Wednesday, January 18](./Module0/Lec04-Wed_Jan_18/README.md)
	* [When to Submit Your Work](./Module0/Lec04-Wed_Jan_18/README.md#when-to-submit-your-work)
	* [Assignment #1: Tic-Tac-Toe](./Module0/Lec04-Wed_Jan_18/README.md#assignment-1-tic-tac-toe)
	* [Software Development Plan and Sprint Signature](./Module0/Lec04-Wed_Jan_18/README.md#software-development-plan-and-sprint-signature)
	* [The Markdown markup language](./Module0/Lec04-Wed_Jan_18/README.md#the-markdown-markup-language)
05. [Friday, January 20](./Module0/Lec05-Fri_Jan_20/README.md)
	* [Stand Up Scrum Meetings](./Module0/Lec05-Fri_Jan_20/README.md#stand-up-scrum-meetings)
	* [Retrospective: Assignment #0](./Module0/Lec05-Fri_Jan_20/README.md#retrospective-assignment-0)
	* [How to Report Bugs Effectively](./Module0/Lec05-Fri_Jan_20/README.md#how-to-report-bugs-effectively)
06. [Monday, January 23](./Module0/Lec06-Mon_Jan_23/README.md)
	* [How to Use the Lecture Notes](./Module0/Lec06-Mon_Jan_23/README.md#how-to-use-the-lecture-notes)
	* [Using Modules for code organization](./Module0/Lec06-Mon_Jan_23/README.md#using-modules-for-code-organization)
	* [Namespace Collision Quiz](./Module0/Lec06-Mon_Jan_23/README.md#namespace-collision-quiz)

</details>


### Module 1
07. [Wednesday, January 25](./Module1/Lec07-Wed_Jan_25/README.md)
	* [The Read, Eval, Print, Loop (REPL)](./Module1/Lec07-Wed_Jan_25/README.md#the-read-eval-print-loop-repl)
	* [What is an IDE?](./Module1/Lec07-Wed_Jan_25/README.md#what-is-an-ide)
	* [Coding by context menu (and other IDE pitfalls)](./Module1/Lec07-Wed_Jan_25/README.md#coding-by-context-menu-and-other-ide-pitfalls)



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


### Troubleshooting

If `./concatenate.sh` yields error messages like these:

```
concatenate.sh: line 2: $'\r': command not found
concatenate.sh: line 9: syntax error near unexpected token `$'do\r''
```

it is because that script has MS-DOS line endings.  To fix it, try running this
command:

```bash
$ dos2unix concatenate.sh
dos2unix: converting file concatenate.sh to Unix format...
```

then re-run the concatenate script.
