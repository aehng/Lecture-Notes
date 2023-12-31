CS1440 - Friday, April 07 - Lecture 34 - Module 5

# Topics:
* [Announcements](#announcements)
* [Review the Sequences Demo](#review-the-sequences-demo)
* [Code Reuse](#code-reuse)
* [Factory Method Pattern](#factory-method-pattern)
* [Strategy Pattern](#strategy-pattern)


------------------------------------------------------------
# Announcements

## The [BSidesSLC Schedule](https://www.bsidesslc.org/schedule) is up!


## IDEA Surveys - Rare Extra Credit Opportunity

You should have received a notification about the IDEA Student Rating of Instruction (SRI) survey.

Your feedback is very important to me, and I really want you to take this survey.  Each semester I take many useful suggestions and incorporate them into my future courses.  If I'm doing anything right, it is due to suggestions given by previous students.

The more input I get from you the better I am able to improve as an instructor.  My goal is to reach 80% participation.  To that end, I am offering 25 points of sweet, sweet *extra credit* for your response.  This is the *only* extra credit I give.  Your responses remain anonymous, and I will not even see them until after finals week.

*   The extra points will be automatically applied to your grade on Canvas by the University **at the end of Finals Week**
    *   There is nothing that I can do to speed this up or verify that your submission was accepted - **it's anonymous!**
    *   Your points will come through; trust the system
*   The survey closes Wednesday, April 26th at 11:59 PM

### IDEA Survey FAQ's

*   Do professors actually read my comments?
    *   Some do, some do not.
    *   Constructive criticism about things that are within the instructor's control goes a long way to help us improve.
    *   If what you want is to vent, try not to be a jerk about it.
        *   Cutting remarks fall on deaf ears, and train instructors to stop reading these reports.
    *   If you have nice things to say, strive to be specific.
        *   "Everything is awesome!!1" isn't as helpful as "I really appreciate ..."
*   Why does the survey ask me to rank this course on how it develops my awareness of "diverse perspectives, other cultures, or my creative capacities"?
    *   IDEA surveys for all courses across campus are designed to be uniform.
    *   If we gave everybody a different survey, we couldn't compare results between different courses.
*   What do I make of all of the learning objectives?
    *   These objectives are **essential** to this course:
        *   3. Learning to apply course material (to improve thinking, problem solving, and decisions)
        *   4. Developing specific skills, competencies, and points of view needed by professionals in the field most closely related to this course
    *   These objectives are **important** to this course (weigh half as much as essentials)
        *   1. Gaining a basic understanding of the subject (e.g., factual knowledge, methods, principles, generalizations, theories)
        *   9. Learning how to find, evaluate, and use resources to explore a topic in depth
*   What changes to this course have come as a result of IDEA feedback?
    *   Introduced the Shell Tutor
    *   Slowed the pace of the first lectures about Bash and Git
    *   The whole DuckieCorp shtick; giving out rubber duckies, scrum + retrospectives
    *   Code roasts
    *   Increased the # of unit tests you get to write (still not enough, but increasing year-over-year)
    *   Dropped file-handling requirements from Assignment #1 (Tic-Tac-Toe) and introduce this concept later
    *   Reformed the Fractal assignments & adjusted their difficulty
    *   Improved the Bingo! assignment (I was going to dump this, but many students reported getting a lot out of it)
    *   Changed the way I teach UML (idem.)
    *   Designated Questioner (idem.)
    *   Post-assignment reflection quizzes
    *   Show students' previous semester performance on assignments
    *   Class Discord server


## ACM & ACM-W Destroy the Stereotype Night

*   **When**  6:00pm Monday, April 10th
*   **Where** Old Main 326

![./03-acmw-poster.png](./03-acmw-poster.png)


# Action Items

*   *Today* you should finish phase **1. Design** of the assignment
    *   Be ready to move on to phase **2. Implementation** *early next week*
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Review the Sequences Demo

Let's review the code from the Sequences Demo that we worked on last week:

*   An *abstract* class `Sequence` defines the overall "shape" for each concrete subclass
    *   Because it is *abstract*, it should be impossible to create a `Sequence` object
    *   Presently this isn't the case, but if I do make a `Sequence` object, it will crash when I call its `.run()` method
    *   [ ] Change the code to prevent a `Sequence` object from existing
*   The concrete class `NonSquare` does not inherit from `Sequence`
    *   The fact that my program can use a `NonSquare` object is an example of *Duck-Typing*
    *   If `NonSquare` was just a little different, my program could crash when I used it
    *   [ ] Change the definition of `NonSquare` so that it inherits from `Sequence`, thus guaranteeing that the minimum set of required methods will exist



# 5 types of [Code Reuse](../Design_Patterns.md#code-reuse)

0.  Cutting & Pasting
1.  Abstract Data Types (ADT)
2.  Libraries
3.  Algorithms
4.  Design Patterns



# The [Factory Method Pattern](../Design_Patterns.md#the-factory-method-pattern)

The idea of the Factory Method design pattern is to separate the *location of creation* from the choice of *what* to create.

See the completed [Sequences](./Sequences) demo for an example of this pattern



# The [Strategy Pattern](../Design_Patterns.md#the-strategy-pattern)

This design pattern allows your users to select an algorithm or behavior at runtime.




