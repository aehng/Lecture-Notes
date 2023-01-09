CS1440 - Monday, January 09 - Lecture 01 - Module 0

# Topics:
* [Get to know your professor](#get-to-know-your-professor)
* [You're hired](#youre-hired)
* [What CS 1440 is about](#what-cs-1440-is-about)
* [Problem-Solving Activity: When will you find time to sleep](#problem-solving-activity-when-will-you-find-time-to-sleep)
* [Action Items](#action-items)


------------------------------------------------------------
# Get to know your professor

Hi, I'm Erik Falor, and I'm your professor this semester.

My family got our first computer for Christmas in 1994, when I was in eighth grade.  I always thought of myself as being "good with computers", but I didn't begin seriously programming until my second year of college when I was 21.  I was originally a Communications major because I debated and worked on the newspaper in High School.  I was not then, nor am I now, mathematically inclined.  Compared to my CS classmates I had a late start getting into programming, and I felt like I had to do a lot of catching up to get even with where they were.

I earned my Bachelor's in CS and worked as a software engineer for 13 years at Spillman Technologies, Inc. (now Motorola Solutions) and Automated Products Group.  In 2011 I joined the USU Master's program as a part-time remote student, and graduated fall 2016.  I taught a class as an adjunct the following spring semester, and loved it.  I have been teaching full-time since fall 2017.


I spent my programming career:

*   _Reading_ horrible documentation
*   _Writing_ documentation that was, hopefully, an improvement
*   _Maintaining_ software that was first written **way** before my time.  Some of the oldest code I touched was first written in the early 90's, while I was still in elementary school.
    *   _Testing_ code written by myself and teammates
    *   _Finding_ and fixing bugs
    *   _Monitoring_ the performance of our software on customers' systems
    *   _Porting_ software between platforms
*   _Building_ software with build systems such as Make, Ant, VisualStudio, IAR Embedded Workbench and shell scripts
*   _Reviewing_ code written by my team
*   _Processed_ data with SQL & ISAM databases, XML/XSLT, the Unix text tools and tools that I made myself
*   _Designing_ new software
    *   _Writing_ new code in Perl, C, C++, Java/C#, XSLT and Shell


<details>
<summary>Things I don't like</summary>

0.  Counting from `1`
1.  Corporate OSes (Microsoft Windows™, Apple OS X)
2.  Desktop Environments
3.  Office Suites with their pretentious "rich" file formats
4.  Your text editor
5.  Squishy keyboards, touch screens and mice
6.  QWERTY
7.  Ball-point pens
8.  Mainstream music

</details>


<details>
<summary>Things I do like</summary>

0.  Counting from `0`
1.  Linux
2.  Tiling window managers
3.  OG plain-text files, Markdown, and $`\LaTeX`$
4.  Vim
5.  Mechanical keyboards
6.  Colehack - my own custom keyboard layout
7.  Fountain pens
8.  Lately I've been listening to shoegaze. Some bands I like
    *   Nothing
    *   Narrow Head
    *   Gleemer
    *   Airiel
    *   Grivo
    *   trauma ray
    *   Pinkshinyultrablast

</details>


There is no such thing as a "stupid question" in my classroom...

![Ten Thousand - https://xkcd.com/1053/](./10-ten_thousand.png)

...though some questions are not germane to the lecture.  I'm always happy to stay after class to answer off-topic questions.



# You're hired!

Welcome to DuckieCorp, the consultancy firm for programmers who talk to themselves.

The purpose of this course is to prepare you to become a competent problem-solver who understands and uses the best software engineering techniques.


*   Course structure 
    *   [Topics covered in this course](../../Outline_of_Topics.md)
    *   These on-line lecture notes are your textbook
        -   https://gitlab.cs.usu.edu/erik.falor/sp23-cs1440-lecturenotes
    *   Content and assignments are organized into Modules on Canvas
*   Assignments (80% of your grade)
    *   Assignments here are large multi-stage projects as compared to the small exercises from CS 1400
    *   You have approximately 2 weeks per assignment
        -   This is *not* an invitation to procrastinate. Make every day count!
        -   A filled-out Software Development Plan is a **required part of each assignment**
        -   Don't write any code at the beginning - make sure you first understand what the assignment is about
    *   You *may* design & brainstorm with study buddies
    *   You *must* write your code individually
        *   *Do not* submit code you saw on Chegg, CourseHero, Stack Overflow, YouTube, the CS Discord, etc.
    *   Submit to GitLab only; there nothing to turn in on Canvas
    *   After you submit your code, complete the **Assignment Reflection Quiz** for 5 points
* Quizzes (10% of your grade)
* Participation (10% of your grade)
    *   50 points for being the Designated Questioner **one time only**
    *   50 points for in-class participation activities, earned 5 points at a time
*   Course Discord Server
    *   Participation on Discord is **optional**
    *   Get the sign up link by taking the **Discord Rules Quiz** on Canvas
*   CS Coaching Center
    *   Location: Old Main 304
    *   Hours
        *	Mon - Thu: 10am to 8pm
        *   Fri: 10am to 6pm
        *	Saturday: 12pm to 6pm
    *   [Online Queue](https://coach.cs.usu.edu)
    *   The coaches aren't there to write your code for you, they support you in doing the work yourself!
    *   When seeking coding help, bring your *Software Development Plan* and explain it to the coach. You don't want to be that person who asks for help with something that is completely unnecessary
*   My Office Hours
    *   When: Thursday 9am to 12pm
    *   IRL: Old Main room 418A
*   Teaching Assistants
    *   Check the **Syllabus** for their up-to-date office hours and contact info
    *   Jaxton Winder
        *   >
    *   Logan Smith
        *   > I grew up in Riverton, Utah, and I spent a few years living in Chicago, Illinois.
            > 
            > I have been at USU studying CS since spring 2019. I took this class in fall 2019, and I liked is so much I decided to come and be a TA for it. 
            > 
            > About me:
            > - I took 2 years of Japanese classes here.
            > - I love video games, and also love board and card games.
            > - I have been married since summer 2020
            > 
            > I am also working as the Computer Science department Peer Advisor, so you can reach me during my peer advising hours or during my office hours for this class. I will also try to respond to emails by the end of the work day on weekdays, and will try to be available to answer emails or discord messages outside those hours. Feel free to reach out for any help
    *   Peter Fowles
        *   > I am from:
            > 
            > - Fort Benton, Montana
            > - Salem, Utah
            > - San Jose, California
            > - All over Texas
            > 
            > I have been studying Computer Science since Fall 2019, and I hope to graduate sometime in the next year or two. 
            > 
            > About me:
            > 
            > - I am a part of the USU Aggie Marching Band/Aggie Pep Band as a Tuba player
            > - I have been married for just over a year and a half (I met my wife in the marching band during my first semester here in 2019)
            > 
            > I worked as a TA in CS1400 and in the coaching center for a year, after which I was employed as a software developer at the Space Dynamics Laboratory (SDL) for a year and a half. I really missed teaching, so I left that job very recently to TA for all of you, as well as work in the coaching center again! I look forward to working with you here. 
            > 
            > I believe that this class is the most essential and useful one that the CS department offers, since everything you will learn here will apply to everything you do in Computer Science, regardless of what you end up doing with it.



# [What CS 1440 is about](../../What_CS_1440_Is_About.md)

CS 1440 is **fundamentally different** than CS 1400.  This document helps you set the right expectations.



# Problem-Solving Activity: When will you find time to sleep?

Getting a college degree is a **lot** of work.  But exactly how much work are you in for?  Can you afford to have a job, a social life, or even to sleep?

After all of this hard work, you should be able to call yourself an expert in your field, right?

Since I am a programmer, my instinct is to write a program to figure this out.  But every time I dive straight in and write code, I get stuck.  A better way is to first *design* the program in my mind before I commit it to [code](./effort.py)

Let's find answers to these questions in particular:

*   How many hours per week will I need to spend on classes?
    *   ...
*   How many hours per week can I sleep?
    *   ...
*   How many hours per week can go towards a job?
    *   ...
*   How many hours of free time can I afford per week?
    *   ...
*   How many hours of my Bachelor's degree actually go towards becoming a programmer (or your intended profession)?
    *   ...
*   How close to a 10k-hour "Gladwell Expert" will I be upon graduation?
    *   ...



# Action Items

## Before our next lecture on **Wednesday**:

0.  Make an account on https://gitlab.cs.usu.edu
    *   Follow the instructions in [GitLab Account Setup](../../Using_Git/GitLab_Account_Setup.md)
    *   While on campus you must connect using the **Eduroam** network
    *   You cannot see my GitLab server while on **BLUEZONE** 
    *   ![](./18-use-eduroam.png "Use Eduroam")
1.  Run through the Required Software Install Instructions on Canvas so we can address any issues ASAP
2.  Use Git to clone Assignment #0 [Shell Tutor](https://gitlab.cs.usu.edu/erik.falor/shell-tutor) and begin working through it
3.  If your Python skills are rusty, send me an email and I will invite you to the **Python Crash Course** on Canvas
4.  Take the "Get to know you" participation survey on Canvas
    *   Now that you know a little bit about me, this week's participation activity asks a few questions to help me get to know you as a person
    *   Find the **Get to know you** quiz in Module 0 on Canvas
    *   It is due at *midnight, Wednesday, January 11*



