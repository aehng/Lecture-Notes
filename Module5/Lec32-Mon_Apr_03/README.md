CS1440 - Monday, April 03 - Lecture 32 - Module 5

# Topics:
* [Announcements](#announcements)
* [Assignment #5.0 Retrospective: Pay it forward](#assignment-50-retrospective-pay-it-forward)
* [Assignment #5.0 Code ~~Review~~ Roast](#assignment-50-code-review-roast)
* [Introduce Assignment #5.1 - Design Patterns](#introduce-assignment-51-design-patterns)
* [What if my Assignment 5.0 code doesn't work](#what-if-my-assignment-50-code-doesnt-work)


------------------------------------------------------------
# Announcements

## DC435 Meeting This Week

*   **What**  T-Pot Honeypot by Allen Hill
*   **When**  7:00pm Thursday, April 6th
*   **Where** Bridgerland Technical College (1301 N 600 W, Logan)
    *   Room 840
*   [Discord](https://discord.dc435.org/)


# Action Items

*   Work on phase **0. Requirements Analysis** of the new assignment *today*
    *   Wrap it up *tomorrow*
*	Call on 2 designated questioners
*	Hold a 3-minute stand-up scrum meeting with your team



# Assignment #5.0 Retrospective: Pay it forward 

0. Pick up one sticky note, color doesn't matter
1. Write your name and/or A number on the sticky note
2. What advice about this assignment would you give a student who will take this course next semester?
3. Put your sticky note on the whiteboard



# Assignment #5.0 Code ~~Review~~ Roast

*Disclaimer: Please don't take it personally if it is your code shown here.  I wanted to show the most common mistakes I came across throughout all of the submissions.  If I happened to pick yours, it was just the luck of the draw*


## Wheel 2.0: Now with more moving parts!

This example is *exactly* the sort of thing that I have been warning you about.  Programmers who buy into Object-Oriented Programming seem to be especially prone to this kind of over-complication.

*Every* line of code is a liability!

This code is not as simple as it could be, and hides a subtle bug.  Can you spot it?

```python
##############
# Palette.py #
##############

 1  from colour import Color
   
 2  class Palette:
 3      __contents = []
   
 4      def __init__(self, *colors):
 5          self.__contents.extend(colors)
   
 6      def extend(self, *colors):
 7          self.__contents.extend(colors)
   
 8      def __getitem__(self, index):
 9          return self.__contents[index]
   
10      def __len__(self):
11          return len(self.__contents)
   
   
12  MANDELBROT = Palette(
13      *[Color(c) for c in [
14          ... 111 colors elided ...
15          ]])
   
16  PHOENIX = Palette(
17      *[Color(c) for c in [
18          ... 102 colors elided ...
19          ]])
```

<details>
<summary><h3>Click for a hint</h3></summary>

What are the lengths of `MANDELBROT` and `PHOENIX`?

</details>


<details>
<summary><h3>This is the problem</h3></summary>

Both lists have length `213`.  They are, in fact, the same lists.

Line 3 of this file defines a list as a *class attribute* instead of an *instance attribute*:

```python
class Palette:
    __contents = []
```

In Java-speak you'd say this is a "class static variable".  There is only one `__contents` list shared by *all* `Palette` objects in this program.

For `__contents` to become an *instance* attribute (a.k.a. *instance variable* or *data member*) it must be declared in `__init__()`, like this:

```python
class Palette:
    def __init__(self, *colors):
        self.__contents = colors
```

Because of how classes in Python work, line 5 of the program finds the existing `Palette.__contents` instead of creating a list in the context of the newly created object.  It extends this list by the colors passed to the initializer, making the class's static list longer and longer each time the programmer tries to make a new `Palette` object.

</details>

When you design a new class, be careful that you don't re-invent existing data structures that your language gives you for free.  `Palette` is just a list with fewer features.  Look at the methods and dunders that `Palette` defines; what makes a `Palette` different from Python's built-in list (besides the fact that Python's list works...)?  

*   In Python version 3.10.7, `list` defines 36 dunders
*   `Palette` defines 2: `__getitem__` and `__len__`
    *   And these just call on the underlying `list` operations


<details>
<summary><h3>This is all that was needed</h3></summary>

```python
##############
# Palette.py #
##############

 1  MANDELBROT = [ '#89ff00', '#a4f817', '#baf12e',
 2                  ... 35 lines elided ...            
 3                  '#e052da', '#e33e97', '#e8283f']
       
 4  PHOENIX = [ '#FFE4B5', '#FFE5B2', '#FFE6AF', '#FFE8AC', '#FFE9A9', '#FFEBA7',
 5              ... 16 lines elided ...
 6              '#002B7D', '#00267A', '#002277']
```

</details>



## Spaghetti Code

A student sought help when their program always crashed with this error:

```
Traceback (most recent call last):
  File "src/main.py", line 67, in <module>
    main()
  File "src/main.py", line 48, in main
    mbrot.mbrot_main(sys.argv[1])
  File "src/Mandelbrot.py", line 101, in mbrot_main
    paint_mbrot(mbrots, arg, win, 512, photo)
  File "src/Mandelbrot.py", line 74, in paint_mbrot
    ImagePainter.canvas('#000000',baseSize, photo=photo)
  File "src/ImagePainter.py", line 20, in canvas
    photoObject.create_image((baseSize / 2, baseSize / 2), image=photo, state="normal")
  File "/python3.10/tkinter/__init__.py", line 2819, in create_image
    return self._create('image', args, kw)
  File "/python3.10/tkinter/__init__.py", line 2805, in _create
    return self.tk.getint(self.tk.call(
_tkinter.TclError: image "pyimage1" doesn't exist
```

I had seen that error message before, but couldn't quite recall what could cause it.

<details>
<summary><h3>Pop quiz: When presented with a Python stack trace, where do you begin?</h3></summary>

Start at the bottom, and work your way up until you find a file that *you* wrote

I began on line 20 of `src/ImagePainter.py` and worked my way back up the call-stack.  It turned out that the problem began in an earlier function call.  

</details>

Here are the relevant bits of code.  Look for something that is duplicated:


```python
#################
# Mandelbrot.py #
#################

 1  def mbrot_main(arg):
 2      win = ImagePainter.makeWindow()
 3      photo = ImagePainter.makePhoto(512,512)
 4      mbrots = getImages()
 5      paint_mbrot(mbrots, arg, win, 512, photo)
   
 6  def paint_mbrot(fractals, imagename, window, baseSize, photo):
 7      # Display the image on the screen
 8      ImagePainter.canvas('#000000',baseSize, photo=photo)
 9      
10      ...
11      
12      for row in range(512, 0, -1):
13          ...
14          window.update()  # display a row of pixels


###################
# ImagePainter.py #
###################

 1  def makeWindow():
 2      window = Tk()
 3      return window
   
 4  def makePhoto(width, height):
 5      photoObj = PhotoImage(width=width, height=height)
 6      return photoObj
   
 7  def canvas(bg, baseSize, photo):
 8      # Display the image on the screen
 9      window = makeWindow()
10      photoObject = Canvas(window, width=baseSize, height=baseSize, bg=bg)
11      # pack the canvas object into its parent widget
12      photoObject.pack()
13      photoObject.create_image((baseSize / 2, baseSize / 2), image=photo, state="normal")
```


<details>
<summary><h3>The answer</h3></summary>

The `image "pyimage1" doesn't exist` error message happens when `Tk()` is called too many times.

The programmer was confused by the flow of their program jumping from `Mandelbrot.py` to `ImagePainter.py`, the back out to `Mandelbrot.py` only to turn back into `ImagePainter.py`, and missed that `ImagePainter.makeWindow()` is called twice - once in `Mandelbrot.mbrot_main()` and a second time in `ImagePainter.canvas()`.

When I slowed the program down by running it in the debugger, sure enough, I saw both windows appear.  

Had this error not resulted in a crash early on, another problem would arise when `window.update()` is called at the bottom of `paint_mbrot()`.  `window` that is passed to `Canvas` on line 10 of `ImagePainter.py` is *different* than the Window in `win` which is given to `paint_mbrot()` on line 5 of `Mandelbrot.py`.

*   `Mandelbrot.mbrot_main()` does half of the work of setting up the Tkinter window, and `ImagePainter.canvas()` does the other half.  There is no reason to divide this work this way.
*   What value does `ImagePainter.makeWindow()` add to the program?  It costs 3 lines to do the same thing as `Tk()`, and doesn't make the program more convenient.
*   What benefit does `ImagePainter.makePhoto()` provide?  It's just a longer way of calling `PhotoImage()`.  You might justify its existence if it didn't require passing in the size of the image as parameters (which are fixed in our program), thus simplifying your code.

I believe this student arrived at this design because the assignment required that `ImagePainter` is the *only* module that may import `tkinter`.  The student really wanted to use its features in `Mandelbrot`, so creating this interface enables them to do so while following "the rules".  I made that rule to encourage you to *only* do things relating to the image in the `ImagePainter`.  Keeping that logic in one place makes this task a straight shot:

```python
#################
# Mandelbrot.py #
#################

 1	def mbrot_main(arg):
 2	    fractal = getImages()[arg]
 3	    ImagePainter.paint(fractal)


###################
# ImagePainter.py #
###################

 1	SIZE = 512
 2	BG = '#000000'
   
 3	def paint(fractal):
 4	    # Display the image on the screen
 5	    window = Tk()
 6	    photo = PhotoImage(width=SIZE, height=SIZE)
 7	    canvas = Canvas(window, width=SIZE, height=SIZE, bg=BG)
 8	    canvas.create_image((SIZE / 2, SIZE / 2), image=photo, state="normal")
 9	    canvas.pack()
10	    ...
11	    
12	    for row in range(512, 0, -1):
13	        ...
14	        window.update()  # display a row of pixels
```

</details>

**Lessons to draw from this example:**

*   **Minimize** the number of levels of redirection, as they make the flow of the program hard to follow
    *   Carefully design the flow of your program so that control doesn't jump back and forth more than necessary
    *   Even within the confines of structured programming it is possible to end up with a tangled mess of **spaghetti code**!
*   Don't create functions just for the sake of creating functions
    *   Functions should **add value** to the program
    *   Don't make functions to **get around** design constraints!
    *   When I ask you to do (or **not** do) something, there is a good reason - usually to force you into a simpler solution



# Introduce Assignment #5.1 - Design Patterns

*Hint: Watch the demo video on Canvas!*

Bugs found in the instructions have been fixed since you cloned the repository.  Run this command in the assignment repo to get the latest changes:

```bash
$ git pull old-origin master
```



## Installing the `colour` module

```bash
$ pip3 install --user colour
```

If that doesn't work, try running `pip` instead of `pip3`.

If that *still* doesn't work, try one of these:

```bash
$ python3 -m pip install --user colour
```

or

```bash
$ python -m pip install --user colour
```

## Assignment #5.1 is your final opportunity to use your Grading Gift

*   As a reminder, per the course rules the Grading Gift may not be used on the final assignment
*   Assignment 5.1 **Design Patterns** is the last assignment which the grading gift may be used



# What if my Assignment 5.0 code doesn't work?


To help everybody begin Assignment 5.1 on even footing, you may use Erik's solution
as the basis for the next assignment.  Instructions follow.

In any event, everybody should pull the latest `master` branch.  There have been a few documentation bugs that are fixed in the latest commits:

```bash
$ git pull old-origin master
```


## Using my Assn5.1 starter code

You will find the Assn5.1 starter code on my repo in a directory called
`erik-src/` in a new branch called `erik-starter`.  You can get that branch from
my starter code repository through the name `old-origin` if you followed
GitLab's suggestions when creating your repository.  If you don't have a remote
repo called `old-origin` which points to my repo, you can easily add it:

```bash
$ git remote add old-origin https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn5
```

Now you can `git fetch` the new branch and merge it into your own `master` branch:

```bash
$ git fetch old-origin
$ git merge --no-edit old-origin/erik-starter
```

(The `--no-edit` argument prevents Git from dumping you into a text editor to review a boring boilerplate commit message).

Then replace your `src/` directory with `erik-src`:

```bash
$ mv src my-src
$ mv erik-src src
$ git add .
$ git commit -m "Starting afresh with Erik's starter code"
```



