CS1440 - Wednesday, January 11 - Lecture 02 - Module 0

# Topics:
* [Announcements](#announcements)
* [Be The Designated Questioner](#be-the-designated-questioner)
* [Setting up your computer for DuckieCorp](#setting-up-your-computer-for-duckiecorp)
* [Assignment #0: Shell Tutor](#assignment-0-shell-tutor)
* [Why are we learning an interface straight out of the 70's](#why-are-we-learning-an-interface-straight-out-of-the-70s)
* [Unix command line basics](#unix-command-line-basics)


------------------------------------------------------------
# Announcements

## Take the Discord Quiz

*   You can be given an invite link to the course Discord server **after** passing this quiz
    *   The quiz is not graded
    *   Participation in the course Discord is *optional* 


## Adventures in data science education - from Coursera courses to community based data science

*   **What**  Department of Mathematics and Statistics Colloquium
*   **Who**   Jeff Leek ('03) Chief Data Officer, Vice President, and J Orin Edson Foundation Endowed Chair of Biostatistics at the Fred Hutchinson Cancer Center
*   **When**  3:30pm Thursday, January 12th
    *   Refreshments 30 min prior
*   **Where** Huntsman Hall 270

Data touches every part of our lives -from our news, to our health, to entertainment, to our politics. One reason is that data became spectacularly inexpensive over a very short period of time in the last 20 years. At the same time, it became easier and easier to rent computing time on a massive scale to analyze these data. These trends lead to a massive revolution across all aspects of business, science, health, news, and society. I'll discuss how I got caught up in this sea change and ended up teaching more than 8 million people data science; about how we used AI tools to make that kind of teaching possible; and ultimately how we used advanced machine learning and local, sustainable partnerships to develop data science training in underserved communities through our DataTrail program.



# Be The Designated Questioner

*   An important part of your training as a software engineer is to develop a habit of critical thinking.
*   The best engineers and programmers I worked with have one thing in common: they were driven to understand _why_.
*   In each lecture I call upon students to be the "designated questioners" (DQ) for that day.
    *   You may be a DQ once per semester.
    *   DQ's ask their questions in-person.
    *   If you choose to be the DQ that day you will will earn 50 points for your question.
*   When you are called it is your responsibility to ask a _good_ question during that lecture.


### Bad Questions

These are not suitable for a DQ's question:

0.  _"Will this be on a quiz?"_
1.  _"How many points will I lose if I turn this in a day late?"_
2.  _"What day did we talk about the Factory Method design pattern?"_


### Good Questions

A good question

* Gets at the _why_ of the topic at hand
* Sparks a thoughtful discussion
* Is not trivially answerable by looking at the syllabus or the lecture notes


<details>
<summary><strong>Hints for asking a good question</strong></summary>

0.  Restate what you _do_ understand.
    *   _"It seems that at each step of the Wolf-Fence algorithm I divide the problem in half, thus reducing the number of potentially buggy lines of code exponentially.  Is that correct?"_
1.  Explain what you _don't_ know.  Putting your misunderstandings into words is an effective way to organize your thoughts and to identify gaps in your knowledge.
    *   _"I don't understand difference between giving the program its input from the command line versus an interactive prompt.  In either case I'm just typing text for the computer to read.  Is one way really better than the other?"_
2.  Ask a counterfactual question.  When you are called upon to be the DQ but don't feel that you need clarification, ask a question that attacks the underlying assumptions behind the subject at hand.
    *   _"Why did you do it that way?  What would happen if you did it another way?"_

</details>


## Opting out

If you have a legitimate reason to not be a DQ, contact me discreetly to work out an alternative arrangement.


## Call on 2 designated questioners



# Setting up your computer for DuckieCorp

Read and follow the document titled **Required software installation instructions** in the **DuckieCorp Employee Handbook**

It looks like a really long document, but most of it is there to help Windows ~~sufferers~~ users convert their game consoles into workstations.  If you use Mac or Linux you are already 90% of the way there.

If you do use Windows, get to work on this ASAP so we can help you fix any issues you run into before the Shell Tutor is due.



# Assignment #0: Shell Tutor

The best way to overcome the learning curve of CLI's is with *consistent* practice.
I created the [Shell Tutor](https://gitlab.cs.usu.edu/erik.falor/shell-tutor)
to help you get this practice in a guided environment.

*   The Shell Tutor consists of eight **required** lessons
    *   Lesson `3.1-wsl-setup.sh` is **only for users of WSL**; Linux and Mac users can skip it
    *   On average, a lesson takes 25 minutes to complete
*   Install the Shell Tutor **after** completing the **Required Software Installation Instructions** on Canvas
    *   Installation instructions are found on the Shell Tutor home page


## Assignment Quizzes

Each assignment has two quizzes.  Think of them as "pre" and "post" quizzes

*   **Starter Code Quiz** (8 points)
    *   You may take this quiz as many times as you want; the highest score is kept.
    *   For the current assignment, some of the answers are found in the syllabus, while others come from lessons in the Shell Tutor.
        *   You should take the quiz **after** finishing the Shell Tutor.
        *   On future assignments the quiz will focus on the starter code, and you should take the quiz near the beginning.
*   **Assignment Reflection Survey** (5 points)
    *   This is an opportunity to reflect on your experience working on the assignment.  
    *   There are no right or wrong answers.
    *   All responses are anonymous.
    *   Your responses help me develop better homework assignments.


## Bug Bounties

We've recently revamped the **Shell Tutor**, which means that there are many *bugs* lurking in the code.  Our folly is your opportunity!

Be the *first* to provide an *actionable* bug report, and you'll earn **10** points of extra credit!
Anything is fair game, from serious crashes to things that would make your
English teacher cringe (like **tpyos** and **words that missing**).

Just send your _actionable_ bug report in an email to **erik.falor@usu.edu**.

**What is an _actionable_ bug report?**

Include the following information in your bug report to ensure that we are able to use it to fix a problem:

*   Tell me *what you were doing* when you noticed the bug
*   Describe what *actually* happened
*   Explain what you *expected* to happen
*   Copy the output of the `tutor bug` command (if the tutor didn't crash entirely)
    *   Copy as much of the text on your terminal as possible to capture the previous commands you ran before the problem erupted (scroll up a few screens)
    *   Paste the **PLAIN TEXT** into a `.txt` file (do this in Notepad.exe or a similar program to avoid "helpful" formatting)
*   **NO SCREENSHOTS PLEASE** - whoever said *"a picture is worth a thousand words"* never had to debug a program from a JPEG.
    *   The Shell Tutor is not a graphical program; plain text really is the best.



# Why are we learning an interface straight out of the 70's?

[How to view someones IP address and connection speed!](https://www.youtube.com/watch?v=SXmv8quf_xM)

There are many ways to control computers; a field called Human Computer
Interaction (HCI) is dedicated to understanding them all.

There are many ways to interact with a computer.  HCI researchers recognize four:
        
<details>
<summary><strong>0. Instructing</strong></summary>

Telling the computer what to do 

*   shortcut keys
*   buttons
*   strings of characters
*   quick and prompt feedback
</details>


<details>
<summary><strong>1. Conversing</strong></summary>

Holding a back-and-forth dialog with a computer

*   wizards
*   pop-up boxes
*   context-sensitive menus
*   prompts
</details>


<details>
<summary><strong>2. Manipulating</strong></summary>

Leverage users' knowledge of the "real-world" through analogs to familiar concepts

*   desktop
*   icons
*   folders
*   drag-and-drop
*   point-and-click
</details>


<details>
<summary><strong>3. Exploring</strong></summary>

Moving through virtual or physical environments

*   virtual reality
*   augmented reality
*   "It's a UNIX system, I know this!"
</details>

<details>
<summary>Which category do you think the command line fits into?</summary>

**Conversing**, though most people treat it like **Instructing** by ignoring
half of the conversation.

</details>


*   Each style of interaction has its own strengths and weaknesses
*   Even I will admit that CLI isn't the end-all-be-all of UI
*   Command-line interfaces (CLI) were created on mainframe computers in the
    1960's
    *   CLIs have stayed relevant because they
    *   enable users to *concisely* communicate big ideas to a computer
    *   make it very easy to **automate** repetitive, tedious and error-prone tasks
*   The biggest downside of CLIs is that they are **not intuitive**



# [Unix command line basics](../Unix_CLI.md)

The command line interface you will use in this class is called Bash (Mac users
have Zsh, but you won't be able to tell them apart at this early stage).

Bash was originally designed for Unix operating systems, but today it is
available on many platforms and is widely used by developers.

## [Necessary Jargon](../Unix_CLI.md#jargon)

Important words to know

*   Terminal or Console
*   Shell
    *   Bash
    *   Zsh
*   Directory
    *   Current working directory
    *   Subdirectory
    *   Parent directory
*   Prompt
*   Command
*   Argument
    *   Option
    *   Switch
    *   Flag

## [Unix Shell Cheatsheet](../Shell_Cheatsheet.md)

The shortcuts listed here work out of the box in both Bash and Zsh.



