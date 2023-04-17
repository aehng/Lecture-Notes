CS1440 - Monday, April 17 - Lecture 37 - Module 6

# Topics:
* [Announcements](#announcements)
* [Discussion: "The Mythical Man-Month" by Fred Brooks, Jr](#discussion-the-mythical-man-month-by-fred-brooks-jr)
* [Assignment 5.1 Retrospective - Quick Wins](#assignment-51-retrospective-quick-wins)
* [Assignment #5.1 Code ~~Review~~ Roast](#assignment-51-code-review-roast)
* [Assignment #6: Recursive Web Crawler](#assignment-6-recursive-web-crawler)
* [A Tour Of Some Useful Python Libraries](#a-tour-of-some-useful-python-libraries)
* [Uniform Resource Locators](#uniform-resource-locators)


------------------------------------------------------------
# Announcements

## Take the IDEA Survey

*   So far we're at a 49% response rate!
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

This assignment was open from **Monday, April 3rd** to **Friday, April 14th**
Put your sticky note along the timeline on the white board.





# Assignment #5.1 Code ~~Review~~ Roast

*Disclaimer: Please don't take it personally if it is your code shown here.  I wanted to show the most common mistakes I came across throughout all of the submissions.  If I happened to pick yours, it was just the luck of the draw*


## `print("FractalFactory: Creating default fractal")` found in main.py

I imagine this student's thought process was "The instructions and the video said the program is supposed to print this message out, so I'm going to print it out at all costs..."


```python
### main.py

if len(sys.argv) < 2:
    fractalInfo = {'type': 'mandelbrot', 'pixels': '640', 'axislength': '4.0', 'iterations': 100, 'min': {'X': -2.0, 'Y': -2.0}, 'max': {'X': 2.0, 'Y': 2.0}, 'pixelsize': 0.00625, 'imagename': 'mandelbrot.png'}
    print("FractalFactory: Creating default fractal")
else:
    fractalInfo = makeFractalDictionary(sys.argv[1])
```

"...even if it is incorrect."

The `True` branch of this `if` statement contains logic that belongs in the fractal factory, not in `main.py`.  Writing this code in this file defeats the whole point of having a factory.


## Better Safe Than Sorry

```python
### main.py
import sys

if len(sys.argv) >= 3:
    fractalInfo = FractalParser.parseFracFile(sys.argv[1])
    fractal = FractalFactory.makeFractal(fractalInfo)
    ...
elif len(sys.argv) == 2:
    fractalInfo = FractalParser.parseFracFile(sys.argv[1])
    fractal = FractalFactory.makeFractal(fractalInfo)
    ...
else:
    fractal = FractalFactory.makeFractal(defaultFractalInfo)
    ...



### FractalParser.py
import sys

def parseFracFile(fileName):
    if len(sys.argv) > 1:
        file = open(fileName)
```

So let me get this straight:

0.  `FractalParser.parseFracFile()` is only called when `len(sys.argv)` is >= 2 ...
1.  ... in which case `sys.argv[1]` is passed to `FractalParser.parseFracFile()` ...
2.  ... but the string in `sys.argv[1]` is only opened *after* checking that `sys.argv` is long enough to have had an element `1`

What Lovecraftian horror did you witness that compelled you to write code like this?

![](./32-horror.jpg)


## Repetition, Tedium, Propensity To Errors

Whenever something is repetitive, tedious, and error prone, it is best to get the computer to do it for you.  Automation is your friend. This can be as easy as a `for` loop that re-uses a piece of code more than once instead of duplicating it through copy & paste.

```python
class FractalInformation:
    def __init__(self, path = None):
        self.path = path
        self.config = {}

        if path is None:
            self.config = {
                'type': 'mandelbrot',
                'centerx': -0.6,
                'centery': 0.0,
                'axislength': 2.5,
                'pixels': 520,
                'iterations': 111,
            }

        else:
            config = open(path)
            for line in config:
                line = line.rstrip()
                if not line.replace(" ", "").startswith('#'):
                    if line.replace(" ", "").lower().startswith('type'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['type'] = sb[1].replace('\n', "")
                    elif line.lower().replace(" " , "").startswith('creal'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['creal'] = sb[1].replace('\n', "")
                    elif line.lower().replace(" " , "").startswith('cimag'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['cimag'] = (sb[1].replace('\n', ""))
                    elif line.lower().replace(" " , "").startswith('centerx'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['centerx'] = (sb[1].replace('\n', ""))
                    elif line.lower().replace(" " , "").startswith('centery'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['centery'] = (sb[1].replace('\n', ""))
                    elif line.lower().replace(" " , "").startswith('axislength'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['axislength'] = (sb[1].replace('\n', ""))
                    elif line.lower().replace(" " , "").startswith('pixels'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['pixels'] = (sb[1].replace('\n', ""))
                    elif line.lower().replace(" " , "").startswith('iterations'):
                        sb = line.lower().replace(" ", "").split(":")
                        self.config['iterations'] = (sb[1].replace('\n', ""))
            errorCheck(self.config)

def errorCheck(fractal):
    ''' This section simply checks for possible errors the fractal dictionary may run into '''
    ...
```

This implementation weighs in at 44 SLoC, of which 8 lines are *completely* identical, and 16 are *essentially* identical.  If you are asked to add a new key/value pair, this long if/else chain must be lengthened.  Whenever you find yourself writing code such as this, remember that **you** will probably be the person who gets to maintain it!  The easiest code to maintain is code which doesn't exist!


<details>
<summary>Erik's implementation</summary>

```python
class FractalInformation:
    def __init__(self, path = None):
        if path is None:
            # I'd keep this the same as before
            self.config = { ... }

        else:
            f = open(path)
            self.config = {}
            for line in f:
                if line.startswith('#'):
                    continue  # skip comments

                # do this once!
                line = line.rstrip().replace(" ", "").lower()

                if line == '':
                    continue  # while we're at it, skip blank lines

                kv = line.split(":", maxsplit=1)
                if len(kv) != 2 or kv[1] == '':
                    raise RuntimeError(f"Configuration item '{kv[0]}' does not have a value")
                else:
                    self.config[kv[0]] = kv[1]

            f.close()  # Remember to close our files!
            self.errorCheck()  # promote this into a method

    def errorCheck(self):
        ''' This section simply checks for possible errors the fractal dictionary may run into '''
        ...
```

More functionality is attained in only 20 SLoC:

*   This version skips blank lines
*   The file is closed at the end

More importantly, this version is much easier to extend and maintain.

</details>


## A Curious Way To Iterate Through A File

This implementation gives up at the first sight of a blank line, and neglects to handle comments (well, it ignores comments, so it "accidentally" gets this right).  Additionally, this suffers from the same redundancy as the previous example.


```python
fileobj = open(filename)
emptyString = False
while not emptyString:
    line = fileobj.readline().lower()
    if line.startswith('type'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()
    if line.startswith('centerx'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()
    if line.startswith('centery'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()
    if line.startswith('axislength'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()
    if line.startswith('pixels'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()
    if line.startswith('iterations'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()
    if line.startswith('creal'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()
    if line.startswith('cimag'):
        key, value = line.split(':')
        fractal_data[key.strip()] = value.strip()

    if line == "":  # <---- This one
        emptyString = True
fileobj.close()
```

*   You've already seen how I would handle the long sequence of `if` tests.
*   I would instead use an ordinary `for line in fileobj` loop; it is more robust **and** does not require keeping track of an extra detail in a boolean variable.
*   Here's an additional tip about some long sequences of repeated `if` tests: consider whether the guarded statements are *mutually exclusive*.
    *   Mutually exclusive means that if one condition is true, the others cannot be true
    *   Mutual exclusion is more clearly expressed using `elif`
        *   `elif` is also more efficient: as soon as the one true condition is met, no time is wasted testing the remainders which *could not* possibly be true.
*   Writing a group of guarded statements as this student did *suggests* that any or all of them could be true
    *   Because the tests use `str.startswith()`, this cannot possibly be the case


## "You keep using that word. I do not think it means what you think it means."

This example illustrates the importance of exercising failure cases in unit tests.

I like to call code like this *Vizzini Code*:

```python
if not self.config['pixels'].isdigit:
    raise RuntimeError(f"'pixels' needs to be an integer value, not {self.config['pixels']}")
if not self.config['axislength'].replace(".", "").isdigit:
    raise RuntimeError("'axislength' needs to be a float value.")
if not self.config['centerx'].replace(".", "").isdigit:
    raise RuntimeError("'centerx' needs to be a float value.")
if not self.config['centery'].replace(".", "").isdigit:
    raise RuntimeError("'centery' needs to be a float value.")
if not self.config['iterations'].isdigit:
    raise RuntimeError("'iterations' needs to be an integer value.")
```

**Q:** Under what circumstances will each of these exceptions be raised?

<details>
<summary><strong>The answer may shock you</strong></summary>

**A:** Never!

*   `isdigit` is a method that must be *called*
*   Referring to a method without calling it returns a *function object* which evaluates to `True` in a boolean context
*   Thus, all of these `if` statements are *always* true, and no exception can ever be raised, no matter how wrong the contents of `self.config` are

</details>



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



# A Tour Of Some Useful Python Libraries

This assignment will see you combining 3rd party Python libraries into a
web-crawling bot.  I've written some demo programs to help you become familiar
with each library.  It is my hope that you will hack on these programs to
answer your own questions about how these libraries will fit into your own
program.

## Installing The Libraries

If you haven't yet begun, **do this today!**

```
$ python3 -m pip install requests beautifulsoup4
```

## The Demo Programs

*   [urlparse - understanding the anatomy of a URL](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_urlparse.py)
*   [urljoin - making an absolute URL from a relative one](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_urljoin.py)
*   [Requests - GETting data from the web](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_requests.py)
*   [Beautiful Soup - Finding order in chaos](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn6/-/blob/master/demo/demo_beautifulsoup.py)


## What Resources Can Help You Answer Questions About These Libraries?

*   ...
*   ...



# [Uniform Resource Locators](../URLs.md#conquering-stack-overflow)

A URL is a unique name for an object on a computer network.



