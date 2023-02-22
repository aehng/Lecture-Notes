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


<details>
<summary><h3>Module 1</h3></summary>

07. [Wednesday, January 25](./Module1/Lec07-Wed_Jan_25/README.md)
	* [The Read, Eval, Print, Loop (REPL)](./Module1/Lec07-Wed_Jan_25/README.md#the-read-eval-print-loop-repl)
	* [What is an IDE?](./Module1/Lec07-Wed_Jan_25/README.md#what-is-an-ide)
	* [Coding by context menu (and other IDE pitfalls)](./Module1/Lec07-Wed_Jan_25/README.md#coding-by-context-menu-and-other-ide-pitfalls)
08. [Friday, January 27](./Module1/Lec08-Fri_Jan_27/README.md)
	* [The REPL is your code lab](./Module1/Lec08-Fri_Jan_27/README.md#the-repl-is-your-code-lab)
	* [How to Run Programs](./Module1/Lec08-Fri_Jan_27/README.md#how-to-run-programs)
09. [Monday, January 30](./Module1/Lec09-Mon_Jan_30/README.md)
	* [Retrospective: Assignment #1](./Module1/Lec09-Mon_Jan_30/README.md#retrospective-assignment-1)
	* [Assignment #2 - Text Tools](./Module1/Lec09-Mon_Jan_30/README.md#assignment-2-text-tools)
	* [Assignment #1 Code ~~Review~~ Roast](./Module1/Lec09-Mon_Jan_30/README.md#assignment-1-code-review-roast)
	* [What does PyCharm's green "Run" button *really* do?](./Module1/Lec09-Mon_Jan_30/README.md#what-does-pycharms-green-run-button-really-do)
10. [Wednesday, February 01](./Module1/Lec10-Wed_Feb_01/README.md)
	* [Debugging](./Module1/Lec10-Wed_Feb_01/README.md#debugging)
	* [Ten Cool Debugging Tricks That Will Impress Your Friends](./Module1/Lec10-Wed_Feb_01/README.md#ten-cool-debugging-tricks-that-will-impress-your-friends)
	* [How to Debug Anything in Four Easy Steps](./Module1/Lec10-Wed_Feb_01/README.md#how-to-debug-anything-in-four-easy-steps)
	* [Rubber Duck Debugging](./Module1/Lec10-Wed_Feb_01/README.md#rubber-duck-debugging)
	* [The "Wolf Fence" Algorithm for Finding Bugs](./Module1/Lec10-Wed_Feb_01/README.md#the-wolf-fence-algorithm-for-finding-bugs)
	* [How to Read a Stack Trace](./Module1/Lec10-Wed_Feb_01/README.md#how-to-read-a-stack-trace)
11. [Friday, February 03](./Module1/Lec11-Fri_Feb_03/README.md)
	* [Fred Brooks Jr.'s "The Tar Pit"](./Module1/Lec11-Fri_Feb_03/README.md#fred-brooks-jrs-the-tar-pit)
	* [Reading files in Python](./Module1/Lec11-Fri_Feb_03/README.md#reading-files-in-python)
	* [How to write the `cat` text tool](./Module1/Lec11-Fri_Feb_03/README.md#how-to-write-the-cat-text-tool)
	* [IDE Debugger Tools](./Module1/Lec11-Fri_Feb_03/README.md#ide-debugger-tools)
	* [Direct Debugging in the IDE](./Module1/Lec11-Fri_Feb_03/README.md#direct-debugging-in-the-ide)
	* [The call stack](./Module1/Lec11-Fri_Feb_03/README.md#the-call-stack)
	* [Another cool tool: the expression evaluator](./Module1/Lec11-Fri_Feb_03/README.md#another-cool-tool-the-expression-evaluator)

</details>


<details>
<summary><h3>Module 2</h3></summary>

12. [Monday, February 06](./Module2/Lec12-Mon_Feb_06/README.md)
	* [What kinds of programming languages are there?](./Module2/Lec12-Mon_Feb_06/README.md#what-kinds-of-programming-languages-are-there)
13. [Wednesday, February 08](./Module2/Lec13-Wed_Feb_08/README.md)
	* [Python's Built-in Data Structures](./Module2/Lec13-Wed_Feb_08/README.md#pythons-built-in-data-structures)
	* [Which data structure will give me the best performance](./Module2/Lec13-Wed_Feb_08/README.md#which-data-structure-will-give-me-the-best-performance)
	* [When should I use an *unordered* collection](./Module2/Lec13-Wed_Feb_08/README.md#when-should-i-use-an-unordered-collection)
14. [Friday, February 10](./Module2/Lec14-Fri_Feb_10/README.md)
	* [Demo: Making a dictionary out of favorite_colors.dat](./Module2/Lec14-Fri_Feb_10/README.md#demo-making-a-dictionary-out-of-favorite_colorsdat)
	* [`eval()` is evil](./Module2/Lec14-Fri_Feb_10/README.md#eval-is-evil)
15. [Monday, February 13](./Module2/Lec15-Mon_Feb_13/README.md)
	* [Introduce Assignment #3: Big Data Processing](./Module2/Lec15-Mon_Feb_13/README.md#introduce-assignment-3-big-data-processing)
	* [Assignment #2 Retrospective](./Module2/Lec15-Mon_Feb_13/README.md#assignment-2-retrospective)
	* [A solution to `paste`](./Module2/Lec15-Mon_Feb_13/README.md#a-solution-to-paste)
	* [Assignment #2 Code ~~Review~~ Roast](./Module2/Lec15-Mon_Feb_13/README.md#assignment-2-code-review-roast)
16. [Wednesday, February 15](./Module2/Lec16-Wed_Feb_15/README.md)
	* [Intermediate Git](./Module2/Lec16-Wed_Feb_15/README.md#intermediate-git)
17. [Friday, February 17](./Module2/Lec17-Fri_Feb_17/README.md)
	* [How to Read Documentation](./Module2/Lec17-Fri_Feb_17/README.md#how-to-read-documentation)
	* [Applying Text Tools to Assignment #3](./Module2/Lec17-Fri_Feb_17/README.md#applying-text-tools-to-assignment-3)
	* [Write the `startgrep` text tool](./Module2/Lec17-Fri_Feb_17/README.md#write-the-startgrep-text-tool)
	* [Redirect a program's output with the shell](./Module2/Lec17-Fri_Feb_17/README.md#redirect-a-programs-output-with-the-shell)

</details>


### Module 3
18. [Wednesday, February 22](./Module3/Lec18-Wed_Feb_22/README.md)
	* [Protip: colored diff output and what to do if diff says EVERY line is different](./Module3/Lec18-Wed_Feb_22/README.md#protip-colored-diff-output-and-what-to-do-if-diff-says-every-line-is-different)
	* [Objects and Classes](./Module3/Lec18-Wed_Feb_22/README.md#objects-and-classes)
19. [Friday, February 24](./Module3/Lec19-Fri_Feb_24/README.md)
	* [UML Class Diagrams](./Module3/Lec19-Fri_Feb_24/README.md#uml-class-diagrams)
	* [What is the point of a UML Class Diagram?](./Module3/Lec19-Fri_Feb_24/README.md#what-is-the-point-of-a-uml-class-diagram)
	* [UML: Multiplicity Constraints](./Module3/Lec19-Fri_Feb_24/README.md#uml-multiplicity-constraints)
	* [Real-world UML class diagrams](./Module3/Lec19-Fri_Feb_24/README.md#real-world-uml-class-diagrams)
20. [Monday, February 27](./Module3/Lec20-Mon_Feb_27/README.md)
	* [Introduce Assignment #4: Bingo! UML Design](./Module3/Lec20-Mon_Feb_27/README.md#introduce-assignment-4-bingo-uml-design)
	* [Retrospective: Assignment #3](./Module3/Lec20-Mon_Feb_27/README.md#retrospective-assignment-3)
	* [What you need to gain from assignments](./Module3/Lec20-Mon_Feb_27/README.md#what-you-need-to-gain-from-assignments)
	* [A solution to Assignment #3](./Module3/Lec20-Mon_Feb_27/README.md#a-solution-to-assignment-3)
21. [Wednesday, March 01](./Module3/Lec21-Wed_Mar_01/README.md)
	* [Top comments from Monday's retrospective](./Module3/Lec21-Wed_Mar_01/README.md#top-comments-from-mondays-retrospective)
	* [Introduction to Software Testing](./Module3/Lec21-Wed_Mar_01/README.md#introduction-to-software-testing)
22. [Friday, March 03](./Module3/Lec22-Fri_Mar_03/README.md)
	* [Discuss Brooks' "Passing the Word"](./Module3/Lec22-Fri_Mar_03/README.md#discuss-brooks-passing-the-word)
	* [Software Testing Jargon Activity](./Module3/Lec22-Fri_Mar_03/README.md#software-testing-jargon-activity)
	* [Validation vs. Verification](./Module3/Lec22-Fri_Mar_03/README.md#validation-vs-verification)
	* [Writing and Running Unit Tests in Python](./Module3/Lec22-Fri_Mar_03/README.md#writing-and-running-unit-tests-in-python)
	* [Ad-Hoc Testing vs. Unit Tests](./Module3/Lec22-Fri_Mar_03/README.md#ad-hoc-testing-vs-unit-tests)



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

it is because that script has MS-DOS line endings.  To fix it, try running this command **exactly** as written here:

```bash
$ sed -i -e 's/\r//' concatenate.sh
```

then re-run the concatenate script.
