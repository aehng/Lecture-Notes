CS1440 - Monday, April 17 - Lecture 37 - Module 6

# Topics:
* [Announcements](#announcements)
* [Discussion: "The Mythical Man-Month" by Fred Brooks, Jr](#discussion-the-mythical-man-month-by-fred-brooks-jr)
* [Assignment 5.1 Retrospective - Quick Wins](#assignment-51-retrospective-quick-wins)
* [Assignment #5.1 Code ~~Review~~ Roast](#assignment-51-code-review-roast)
* [Assignment #6: Recursive Web Crawler](#assignment-6-recursive-web-crawler)
* [A tour of some useful Python libraries](#a-tour-of-some-useful-python-libraries)
* [Uniform Resource Locators](#uniform-resource-locators)


------------------------------------------------------------
# Announcements

## Take the IDEA Survey

*   So far we're at a XX% response rate!
    *   My goal for the class is 80%
*   It's worth 25 points of extra credit
*   The survey closes 04/26/2023 at 11:59 PM


## Questions for AMA lecture - Monday, April 24th

The topic of the last lecture of the semester is **Ask Me Anything**

I'd love to hear what you'd like to learn a little more about, and what topics may pique your interest!  There is a Canvas discussion thread called **Ask Me Anything** (Canvas Sidebar -> Discussions).  There you can post questions you've been dying to ask all semester, and I will do my best to answer them in the last lecture.

You will receive **10 participation points** for posting in/responding to this thread.  If you'd rather share your question in the Discord `#AMA` channel instead of on Canvas, just post a link to your question on Discord so I can credit the participation points to you.  You are encouraged to strike up a discussion on each others' questions, and your participation will help craft our final lecture!

*This thread will be locked at midnight on Friday, April 21st to give me time to put the lecture together*


# Action Items

*   Work on phase **0. Requirements Analysis** of the new assignment *today*
    *   Wrap it up *tomorrow*
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Discussion: "The Mythical Man-Month" by Fred Brooks, Jr.

## What is the big idea Brooks wants to get across?

*   ...
*   ...

## Does a bigger team of programmers make a project come together faster?

*   ...
*   ...

## Do teams spend enough time testing their code?

*   ...
*   ...

## How much time does Brooks recommend a project spend in testing?

*   ...
*   ...

## What should you do if your schedule starts to slip?

*   ...
*   ...


## Key take-aways

<details>
<summary>Ideas that you must remember from this essay</summary>

*   Developers are **irresponsibly optimistic** when it comes to estimating project schedules
    *   On the other hand, some developers give up on estimations entirely and **just throw out huge numbers** without paying much thought to the matter
*   With experience you can become a **good estimator**
    *   This is helped by **gaining knowledge** both in the problem domain as well as with the tools/technologies used
*   One reason large projects exceed their schedule is **communication**
    *   As more programmers become involved, more **coordination** is needed
    *   This increases time spent in large meetings
    *   Meeting time is very expensive (programmers cost a lot per hour), and is time not spent creating code or running tests
*   System testing is **deferred** until all production is completed *(you don't have a system to test until then)*
    *   If the production schedule has slipped, **testing time is foreshortened**
    *   This is a **grave mistake**, and one that is repeated to this day
*   Brooks recommends spending up to **50% of a project's time in testing**
    *   Most projects don't plan for this and go past the due date by at least this much anyway
*   Programmers need to stiffen their backbones and tell managers & customers that **the best thing to do for a late software project is be patient**
    *   *Nothing* you do can possibly make it finish **sooner**
    *   *Anything* you do will most likely make it even **later**!
    *   Remember Brooks's Law: *Adding manpower to a late software project makes it later*

</details>



# Assignment 5.1 Retrospective - Quick Wins

> It's very difficult to improve 1 thing by 100%. It's much easier to improve 100 things by 1% for the same effect.
>
> -- [Dave Brailsford](http://www.funretrospectives.com/marginal-gains/)

Over the course of Assignment 5 you were asked to make a great change in a small program.  Throughout the course of the project you made these changes gradually through refactoring instead of all at once.

In this retrospective you will identify *quick wins*, little things that were easily done, which add up to great improvements.

> A quick win is something that could be implementable in a couple of hours, with very little cost.

Now that you've seen this entire project through to the end, I want you to go back and consider how successful you would have been if you just directly modified the starter code instead of first refactoring it.

Pick up a sticky note, write your name and/or A number, and answer one of the following prompts:

*   What would have been the same?
*   What would have been more difficult?
*   What *quick wins* did you experience?
*   How did refactoring the starter code set you up for a quick win?
*   In the end, was refactoring worthwhile to you?  Why or why not?

Put your sticky note along the timeline on the white board.

There were 14 days from *Monday, Nov. 14* to *Monday, Nov. 28*





# Assignment #5.1 Code ~~Review~~ Roast

*Disclaimer: Please don't take it personally if it is your code shown here.  I wanted to show the most common mistakes I came across throughout all of the submissions.  If I happened to pick yours, it was just the luck of the draw*





# Assignment #6: Recursive Web Crawler

In this assignment you will combine three Python libraries into a web-crawling
bot.  The starter code is capable of scanning a web page for links.  It is up
to you to make it *recursively* crawl the web by visiting those links, then
visiting the links it finds there, and so on.

In addition to one standard Python library, this assignment uses two 3rd party
libraries to reach out to the web.

*   Follow the instructions included with the assignment to install these libraries onto your system
*   You can expect the grader to have these libraries on their systems
*   *Do not expect* any other libraries to be present!


I have provided some demo programs in the starter code to help you learn how to use these libraries.

*   Plan on spending a day just playing with and understanding these demo programs
*   Six hours before the due date isn't the right time to learn how `urljoin()` works!



# A tour of some useful Python libraries

This assignment will see you combining 3rd party Python libraries into a
web-crawling bot.  I've written some demo programs to help you become familiar
with each library.  It is my hope that you will hack on these programs to
answer your own questions about how these libraries will fit into your own
program.

## Installing the libraries

If you haven't yet begun, **do this today!**

```
$ python3 -m pip install requests beautifulsoup4
```

## The demo programs

*   [urlparse - understanding the anatomy of a URL](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_urlparse.py)
*   [urljoin - making an absolute URL from a relative one](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_urljoin.py)
*   [Requests - GETting data from the web](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_requests.py)
*   [Beautiful Soup - Finding order in chaos](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_beautifulsoup.py)


## What resources can help you with questions about these libraries?

*   ...
*   ...



# [Uniform Resource Locators](../URLs.md#conquering-stack-overflow)

A URL is a unique name for an object on a computer network.



