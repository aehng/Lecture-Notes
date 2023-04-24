CS1440 - Monday, April 24 - Lecture 40 - Module 6

# Topics:
* [Announcements](#announcements)
* [Ask Me Anything](#ask-me-anything)


------------------------------------------------------------
# Announcements

## Friday was the last day to be DQ

*   If you're lacking very many participation points this late in the semester, the best I can do is wish you good luck!
    *   I will publish final participation scores during the day on **Wednesday, April 26th**

## Take the IDEA Survey

*   So far we're at a 72% response rate!
    *   My goal for the class is 80%
*   The survey closes this **Wednesday** at 11:59 PM


## Erik's last office hours session is Thursday, April 27th


# Action Items

*   Complete phases **4. Deployment** and **5. Maintenance** *today* 
    *   Make your final push to GitLab early so you have plenty of time to **verify** your submission
*	Hold a 3-minute stand-up scrum meeting with your team



# Ask Me Anything

*Like an AMA on Reddit, but totally different*


* [Career Advice](#career-advice)
* [Education Advice](#education-advice)
* [Coding](#coding)
* [Opinions on Programming and Technology](#opinions-on-programming-and-technology)
* [About Me](#about-me)



# Career Advice

## What are the most important personal traits to have for a job in CS?

Larry Wall (creator of the Perl programming language) identifies [3 virtues](https://thethreevirtues.com/) that every great programmer possesses:

1.  **Laziness**: The quality that makes you go to great effort to reduce overall energy expenditure. It makes you write labor-saving programs that other people will find useful and document what you wrote so you don't have to answer so many questions about it.
2.  **Impatience**: The anger you feel when the computer is being lazy. This makes you write programs that don't just react to your needs, but actually anticipate them. Or at least pretend to.
3.  **Hubris**: The quality that makes you write (and maintain) programs that other people won't want to say bad things about.

To this list I add a 0th virtue, **Curiosity**: The drive to learn and to keep coming back even when the going gets tough.  The desire to understand how things really work.


## What is the most crucial skill you think every software developer should possess?

Attention to detail.  For example, you'd be amazed at how much time you can save by actually reading and digesting error messages.


## What are the best qualities for a team leader/manager to have?

Listening; to your team, and to your customers.

> How can we best learn and develop these qualities?

It just takes practice.  You should try it sometime!  The people in your life will appreciate it.


## With the rise of ChatGPT and other similar resources...
> ...how do you think that will affect the computer science industry, and what would you do if you were in our shoes to effectively use everything available and prepare for our futures.

*   I like to think about generative AI from the perspective I imagine a grizzled, old greybeard programmer from the 1960's would have about modern, high-level languages like Java or Python
    *   This hypothetical greybeard
        *   wrote everything in assembly
        *   devoted years of his life to understanding one CPU architecture
        *   made every last byte and clock cycle count
    *   Contrast this to a modern programmer who
        *   doesn't know what "displacement" means and writes in a language that doesn't even have pointers
        *   doesn't know the endianness of their CPU
        *   rarely encounters "Out Of Memory" errors
*   The greybeard thinks you are missing out on the things that makes a programmer a programmer; do you feel like you're missing anything?
    *   Whether or not something is a crutch is subjective
*   Advances in technology lowered the barriers to entry to becoming a programmer
    *   There are more computer programmers today than at any time in history
    *   Sure, programmers today don't understand what we're doing to the same level of detail...
    *   ..but we can make bigger systems than the old-timers could
*   I see generative AI as another step in our progression
    *   You should practice using it now so you can learn its *strengths* and *limitations*
    *   If you maintain your **curiosity**, you will not let it become a crutch
*   AI is very helpful for writing **unit tests**


> Also, in your opinion, what is the craziest thing that it can do?

*   I've not had much success doing this myself, but I've seen demos where the user is able to coax the AI into correcting mistakes it makes in code
    *   I'm not convinced that coding this way is faster than just doing it yourself (at this point in time)
*   I use AI as a *prototyping* tool to quickly build a quasi-working system
    *   Since I didn't work for the code, I feel no regret scrapping it and re-writing a better version

> Will we become dependant on AI?

*   Yes, but I don't think we will view this as a bad thing
    *   We are already dependant on compilers to write machine code for us
    *   There was a time when some programmers regarded this as a weakness; but they're all retired now


> Will our jobs be all about proofing what it coded for us?

*   Yes, you will be responsible to
    *   do the design work
    *   guide the AI to create correct code
    *   notice the problems with the code and coax the AI into fixing it
    *   or, fix it yourself


## Before, you told us that the video game industry is kind of a trap for new graduates
> In your opinion, what kinds of jobs should we be looking for upon graduation?

*   I don't want do discourage you from making video games
*   If you want to make games, do it on **your own** terms as an indie dev; do not work for a studio
    *   I've *never* met anybody in that industry who recommends it
*   The industry takes advantage of the fact that each year thousands of freshly-graduated and desperate new programmers flood the job market
    *   Video games are the reason why 50% of all CS majors get into Computer Science [citation needed]
    *   The pay is low, the hours are long, and advancement opportunities are rare
*   You'll be better off taking a job writing *uninteresting* code in a *boring* industry, and write an indie game on your own time


> What industries should we try to start in?  Which ones would treat us best but also have valuable experience?

*   Anything besides game dev!
    *   Security is blowing up right now
    *   As is anything dealing with AI and ML
*   In my experience embedded programming is a mixed bag
    *   There are some very exciting opportunities here...
    *   ...and a lot of dead ends in small niches with comparatively low pay



# Education Advice

## How do I know which field of CS would be best for me?

*   What sorts of things do you like?
    *   If you like breaking/fixing things, go into cybersecurity
    *   If you like making things happen in the real world, go into robotics or embedded programming
    *   If you need validation from others, go into web development
    *   If you don't mind being an unsung hero, look into systems programming, data science
    *   If you want to be on the cutting edge, AI and machine learning is looking promising right now
    *   If you like molding young minds, look into CS education
*   Take some classes in different areas
    *   Graduating seniors often tell me that they took an undesired class because of a scheduling conflict, and it ended up being their favorite class of all


## What classes would you recommend as most useful/interesting? 

*   CS 4700 Programming Languages
*   CS 5300 Compiler Construction
*   CS 5410 Game Development
*   CS 5600 Intelligent Systems


## What was one of the most helpful classes that helped prepare you for working in the industry?

CS 5300 was good in so many ways

*   I *really* learned what my programming languages were trying to accomplish
    *   ...and what their error messages were trying to tell me!
*   I learned how to work on a really hard project that was just at the edge of my understanding
    *   It gave me experience working on a vast project that spanned several source files, hundreds of lines of code, and involved a few different languages


## Do you have a favorite list of books, YouTube channels, podcasts, etc that have helped you learn or stay up to date in the CS Field?
> **Related:** Do you have any book recommendations, either for fun or learning?

*   **Books**
    1.  As mentioned previously, *Think Like a Programmer* by V. Anton Spraul is great
    2.  *The Pragmatic Programmer, 20th Anniversary Edition* by Andrew Hunt and David Thomas is another favorite.  In a previous version of this class it was required readding.
    3.  Read the rest of *The Mythical Man-Month*.  Out of all of the essays, I can only think of one which hasn't stood the test of time.  The rest is awesome.
    4.  *Grokking Simplicity - A book on Functional Programming* by Eric Normand. https://grokkingsimplicity.com/
    5.  *Surreal Numbers* by Donald Knuth.  Don is a legend in CS.  This book isn't exactly about computers, but I think you'll enjoy it.
*   Some of these books are available for free through the O'Reilly Bookshelf.  Read them for free over the summer while you can!
*   **YouTube Channels**
    *   Numberphile
    *   Computerphile
    *   TNMOC - The National Museum of Computing
    *   LGR
    *   Luke Smith
    *   Mental Outlaw
*   **Podcasts**
    *   The Hacks
    *   Advent of Computing
    *   Darknet Diaries
    *   Eric Normand's LispCast
    *   Hanselminutes
    *   Software Engineering Radio


## You mentioned in class that it is very important to be able to read a lot of different types of code.
> **Related:** What are some recommendations of code repositories or public programs that would be beneficial for students to look at and read through?

*   The Hitchhiker's Guide to Python offers [this list](https://docs.python-guide.org/writing/reading/)
*   This [Hacker News thread](https://news.ycombinator.com/item?id=9896369) has some good suggestions, after you skip past the nerd fight about Peter Norvig's Python coding style.
*   The Python Standard Library that came with your Python installation is easily accessible and pretty well documented
    *   To get started, simply open a REPL and
        1.  `import` an arbitrary module `import re`
        2.  Evaluate the module's `__file__` dunder to see the name of the file the library resides in `re.__file__`
        3.  Find that file with your File Explorer
    *   Watch out for modules that are loaded from binary .DLL or .SO files


## The intro courses for CS and ECE are nearly identical
> For many assignments I would write them in C and translate them into Python. In most of my ECE classes we started **from scratch** and in most of my CS classes we were given **starter code**. Why is there this difference in teaching style?

*   It is very unrealistic for you to start a project entirely from scratch
*   We want you to learn how to navigate and work within a code base


## What suggestions do you have for staying sharp and progressing in computer science over the summer for those who aren't taking a summer semester?

See [last Friday's](../Lec39-Fri_Apr_21/README.md#take-part-in-coding-competitionschallenges) lecture for a list of programming challenge websites 


## Do you think it is valuable for an engineering major to get a minor in computer science?

*   Yes!
    *   A lot of tools that engineers use have scripting interfaces
        *   SolidWorks
        *   Autodesk
        *   Altium
    *   If you know how to code, you can automate the *tedious*, *repetitive* and *error prone* parts of your job

# Coding

## Why do you put writing the unit tests into the design phase rather than the implementation phase?

*   Test Driven Development
    *   As you *design* your software, you should consider:
        *   How might it fail, and what would that look like?
        *   What would success look like?
    *   These thoughts will become your test cases
*   If you put off any thought of testing until the code exists, it is already too late


## Do you have any experience working on audio applications like Virtual Studio Technology or Digital Audio Workstations?

No, I don't.

> What would you recommend doing to start programming one?

Jump into the FSLC Discord - one of my former students (@KernelPanic) has told me about this stuff, and may be able to give you some pointers.


## What is your recommended process for writing documentation for a software project?
> What apps/processes do you like

*   Approach it like the SDP
    *   Consider the requirements for the documentation
    *   Think about what problems the docs should solve   
    *   Define what "good" documentation will look like (so you'll know when you're done)
*   As for apps... I personally don't like word processors, and prefer to write in something like Markdown

> How do you ensure that the documentation remains up-to-date and relevant as the software evolves over time, and what strategies do you use to manage version control for documentation?

*   Plan some time each sprint to update docs that will be affected by the changes to the application you plan on making


# Opinions on Programming and Technology

## What are the best practices for maintaining internet privacy / anonymity?

There is one technique that is guaranteed to protect a system from attack: pull the plug.  A computer that is not running can't be hacked into.

Seriously, tho...

*   Practice good [password hygiene](https://pages.nist.gov/800-63-3/)
*   Protect your primary email account with your strongest password, and use 2FA
*   Build up [layers of security](https://blogs.cisco.com/security/layers-of-security)


## What is the benefit to using something like GitKraken or GitClient
> vs the benefits of using Git straight from command line?

*   A GUI tool can be an accelerator *after* you have a grasp on the underlying concepts
    *   Until then, it is a crutch, and will lead you astray
*   When things get *really* messed up, you should be comfortable in the CLI
    *   Stack Overflow, blog posts, etc. won't tell you how to get out of trouble with a GUI


## Do you think they should start teaching programming younger and tie it with teaching the other STEM subjects?

I am in favor if this insofar as students are given an *accurate* mental model of how computers actually work.


## You talk a lot about how you think Linux is best
> Do you truly believe it to that extent or do you play it up more to make a point?

I am a true believer

> Would you recommend all students (including non-CS students) use Linux?

*   Yes
    *   You will encounter Linux in your professional life, so you might as well learn it now
    *   Because you have been using Bash/Zsh this semester you are halfway there


## What are your thoughts on Vim keybinds in VS Code/PyCharm?

They are a pale imitation of the real thing


## What are some ways you have automated tasks in your life or ways you have used CS in your personal life?

*   Whenever I find myself doing something complicated in the shell for the 2nd or 3rd time, I consider writing a script to streamline it
    *   I also automate recurring tasks that come up too infrequently to memorize
*   I have scripts to
    *   Synchronize my lecture Git repos across all of my computers
    *   Help me rebuild my kernel, rebuild Vim, update the packages on all of my systems
    *   Send myself a text message (via my phone's email address) to alert me when certain websites are changed
    *   Grade Designated Questioners on Canvas
    *   Add/update Quiz questions on Canvas
    *   Clone all of your assignments from my GitLab server


## In your opinion, which computer programming language is the most useful?

*   As a Linux user, C has the most useful language to know
    *   My OS is written primarily in C, so understanding this language helps me to understand documentation, blogs and articles about Linux
    *   C is like Latin in that it is a mother tongue to many other programming languages; understanding C makes understanding Perl, Python, C++ so much easier


## What is your favorite programming language and why?

[Scheme](https://www.scheme.org/)

I think Scheme is a good 3rd or 4th language to learn, because it is:

0.  Really different
1.  Conceptually simple
2.  Backed by a large, helpful and healthy community
3.  Has lots of literature and tutorials
4.  Easy to get started in

*   Many of the features in your current programming language that were likely inspired by Scheme (or LISP, of which Scheme is a dialect).
    *   I gave an introductory talk on Scheme to the FSLC in the spring of 2021.  If you are interested in learning more, check it out on [Odysee](https://odysee.com/@fadein:0/SchemeTalk2021:f)

After Scheme, I like C and Perl.


# My Professional Life

## What kinds of programming languages did you use the most when working in the industry?

*   Perl
*   C
*   Java/C#
*   XSLT/XML
*   Shell


## Did you ever freelance and if so what was your experience with it?

*   No, I haven't been a freelancer


## In your work experience, how much time do you usually spend on a single project?

*   Anywhere from 3 sprints (6 weeks) to three years.


## In your experience, what percentage of your work is documentation?

*   Over my whole career, < 5%
    *   Most of that was written in my last year or two
    *   With what I know now, I'd spend much more time than that!


## What is your favorite project that you have worked on in your career and why?

*   Porting Spillman's flagship record management system from Unix to Linux
    *   This had been my dream task for years
    *   I contributed to the Linux takeover of the data center
    *   Finding and deleting gobs of unused code


## What is the largest scale program you have been a part of?

*   The record management system at Spillman Technologies
    *   For a presentation I once gave, I scanned the source code and found that it was > 5 million lines of code
    *   That puts it in the same ballpark as PyCharm and LibreOffice
*   For comparison:

|: Program      :|: SLoC :|: Files :|: Languages                          :|: Notes                                                    :|
|----------------|--------|---------|--------------------------------------|-------------------------------------------------------------
| My Assn5.0 sln | 808    | 34      | Python                               | I went a bit overboard on mine; yours likely won't be so big
| Nano           | 17k    | 18      | 100% C                               | v5.6  
| Zsh            | 116k   | 160     | 93% C, 5% Shell                      | v5.8
| Bash           | 130k   | 434     | 86% C, 5% Shell                      | v5.1
| Git            | 512k   | 2,007   | 47% C, 41% Shell, 5% Perl and 4% TCL | v2.31.0
| Python         | 1.0M   | 2,601   | 71% Python, 26% C                    | v3.8
| LibreOffice    | 4.5M   | 14k     | Written in 16 languages              | v7.2.0
| PyCharm        | 5.2M   | 92k     | 88% Java, 12% Python                 |
| Firefox        | 10.3M  | 49k     | 48% C++, 17% Rust, 16% C, 12% Python | v87.0
| Linux Kernel   | 19M    | 52k     | 99% C                                | There are some 250k lines of Assembly Language


## What is the smallest project you've been a part of professionally?

*   I wrote an application on a handheld barcode reader in C# all by myself at Spillman Technologies 
    *   It fit in your hand, like a cellphone
    *   I spent around 6 weeks on it; there wasn't very much code nor testing to do
    *   Most of that time was familiarizing myself with the programming environment (Windows CE OS, micro version of .NET, learning how to get data from the barcode reader, etc.)
*   I worked on a handful of embedded systems while at APG
    *   They were maybe a few thousand lines of C code
    *   The PCBs (printed circuit boards) were all smaller than a 3x5 card

## What made you decide to get into teaching instead of staying in the industry?

*   At one of my former jobs I started giving training presentations to our tech support staff
*   Eventually, I came to enjoy that part of my work much more than my other responsibilities
*   Around the same time I started giving presentations at local tech conferences, which I enjoyed very much


## What was the weirdest question somebody asked you when you were on call and getting asked for help at 3am?

*   I honestly cannot remember specific instances - I've blocked them all out
*   I can remember feeling very frustrated on several occasions when I was called about a problem I had just *barely* given a training on that week
    *   The techs always felt bad when they realized this, but that didn't stop them from calling me

> You're a more patient man than I am.

*   I don't know about that


## Professionally have you ever been responsible for a giant project as a solo programmer?

*   In any project of respectable size we always worked in teams
*   I was not interested in becoming a manager, so I got out when that became the next step on the ladder

> What did you do to streamline the project, especially in the discovery of requirements?

*   As a scrum team, we deliberated over how to best approach the problem
*   When the customer surprised us with new requirements, we sadly scrapped our code and started over, resetting all of our progress
    *   This didn't actually happen too often; our project managers were pretty good about understanding what the customer wanted
    *   It was a different story when the customer actually got to **use** their new software...


## Have you ever had to sign any form of NDA (non-disclosure agreement) in regard to creating/maintaining a program?

*   I can neither confirm nor deny any details about NDAs I may or may not have signed

> If so, how often, and in what circumstances?

*   All of my jobs came with non-compete clauses
    *   I was not allowed to work for one of our competitors for 365 days from leaving
    *   The idea is to prevent the competition from poaching engineers


# About Me

## What kind of projects do you have cooking behind the scenes?

*   More shell tutor lessons for next year's class
*   A command-line tool to customize your shell's color scheme
*   Improved automation for lecture management


## If you had as much time as you wanted to work on a personal CS project, what would you like to work on?

I would like to make a Roguelike game in Scheme where every object in the world is backed by a lambda expression.  The game mechanics would center around "hacking" the objects in the world to bend reality to your whim.


## What has been your favorite project to work on and why? 

*   I once wrote a self-extracting Perl program
    *   Java has .jar files
    *   Python can run a .zip file if it contains a script called `__main__.py`
*   Perl didn't have anything like this, so I had to make it.
    *   We needed to send a Perl script + a bunch of libraries; dozens of files all together
    *   The Perl script would unzip itself, and start running the main program
    *   I had to write this in pure Perl because, at the time, Perl didn't have a compression module in its standard library


## What is something that you are currently learning about in Computer Science or something that you would like to learn more about?

Functional programming.  Every time I think I got it, I learn something new that blows my mind.  It is simultaneously the most simple and the most mind-bending way to program.



