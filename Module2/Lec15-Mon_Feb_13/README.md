CS1440 - Monday, February 13 - Lecture 15 - Module 2

# Topics:
* [Announcements](#announcements)
* [Assignment #2 Retrospective](#assignment-2-retrospective)
* [A solution to `paste`](#a-solution-to-paste)
* [Introduce Assignment #3: Big Data Processing](#introduce-assignment-3-big-data-processing)
* [Assignment #2 Code ~~Review~~ Roast](#assignment-2-code-review-roast)


------------------------------------------------------------
# Announcements

## Build yourself a website and Git a job

*   **When**  5 - 7pm Monday, February 13th
*   **Where** Old Main 407 (the CS Lounge)
*   **What**  ACM Club online portfolio tutorial night
    *   Learn how to host an online portfolio website, on your own domain, that shows off your work
    *   A hiring manager from Lucid will tell you how to make your digital portfolio stand out from the rest
    *   Free pizza!

![](./02-Git_a_jobACTUAL-1.png)


# Action Items

*   Work on phase **0. Requirements Specification** of the new assignment *today*
    *   Wrap it up *tomorrow*
*	Call on 2 designated questioners


## Assigned Reading: "How to Read Documentation"

*   Read the essay "How to Read Documentation" before our meeting on Friday, February 17th and be prepared to discuss it.
*   The article is right here, [in the lecture notes repo](../How_to_Read_Documentation.md)



# Assignment #2 Retrospective

*   Was it helpful to start from the `cat` tool?
    *   If so, **why**?
*   Which text tool was the hardest to write?
    *   **Why** was that one particularly difficult?
    *   How hard was the `paste` tool to implement compared to the others?
*   Are there any other lessons that you drew from this experience?


## Profoundness and value of insights

0.  Get a sticky note and write down your A#
1.  Think of an insight you gained, the first thing that comes to your mind.
    *   How big of a **"click"** was it?
    *   Did it surprise you that you (or your ducky) came up with it?
    *   Did it make a large impact on your project?
2.  Post it on along the **Profoundness** axis from *enlightened* to *cliché*



# A solution to `paste`

In the past students have reported that `paste` was the hardest to write because it bears the least resemblance to `cat`.

I will now show one way to implement [`paste`](./Partial.py).

*Demo* 

```
$ python Partial.py data/*
```



# Introduce Assignment #3: Big Data Processing

## Important!

This assignment includes **2 new** Shell Tutor lessons.  You should complete these lessons *before* getting into the assignment.

We will talk about what you learn in the Shell Tutor in our next lecture on Wednesday.


## Tour of the Assn3 code

```
git clone git@gitlab.cs.usu.edu:erik.falor/cs1440-falor-erik-assn3
```

*   What do you make of this code?
    *   ...
*   What tasks have been done for you?
    *   ...
*   What is left for you to do?
    *   ...


## What is the problem that you have been asked to solve?

Take a moment to read the
[Instructions](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn3/blob/master/instructions/README.md)
and explain to your study buddies in your own words what this program is about.


## This looks like a lot!  Where should I start?

Take it from somebody who was once in your shoes:

> I remember when I did this assignment I didn't really know where to start.
> I think the best place to start is reading all of the .gov resources and
> opening up the small CSV files to see their format.


## Why can't I just use XYZ program to find the answer?

The full [data set](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn3/uploads/cc7bba707d9a07dd6e8a5c81c178b99e/2021_annual_singlefile.zip)
is 514429368 bytes (491 megabytes) in size.  Let's see what happens when we attempt to open this file in some common editors:

*   LibreOffice Calc (Spreadsheet)
*   PyCharm
*   VS Code
*   Emacs
*   Vim



# Assignment #2 Code ~~Review~~ Roast

Here are solutions to the Text Tools program that some of you came up with.  If your code is shown here I am not putting you or your work down.  The best way to learn coding skills is by looking at code written by others.


## Solutions to `tac`

### Use a counter to count back from the bottom of the file

Nice pseudocode description, BTW:

```python
# tac:
#
#     check for enough parameters
#     check if file can be opened
#         if yes open file and pass back object
#     if not show error
#     for each line in file starting at the end
#         print to the screen

 1  def tac(args):
 2      """concatenate and print files in reverse"""
 3      # print("TODO: concatenate and print files in reverse")
 4      if len(args) < 1:
 5          usage("Too few arguments", "tac")
 6          sys.exit(1)
 7      for fname in args:
 8          fobj = open(fname)
 9          lines = fobj.readlines()
10          i = len(lines) - 1
11          while i >= 0:
12              print(lines[i], end='')
13              i -= 1
14          fobj.close()
```

This is a pretty typical solution written by students with your level of experience.  The body of this function is 11 source lines of code (SLoC, not including blanks and comments).  Not bad, but a little wordy.


### Idem, but with an extraneous call to `seek()`

```python
 1  def tac(args):
 2      if len(args) == 0:
 3          Usage.usage("Tac needs to be given at least one file", "tac")
 4          sys.exit()
 5  
 6      for fname in args:
 7          lineList = []
 8          fobj = open(fname)
 9          numLines = -1
10          for lines in fobj:
11              lineList.append(lines)
12              numLines += 1
13  
14          fobj.seek(0)
15          for line in lineList:
16              if numLines > -1:
17                  print(lineList[numLines], end="")
18                  numLines -= 1
19  
20          fobj.close()
```

This is a faithful translation of this function's pseudocode as given in the SDP.

The call to the `.seek()` method is either a result of research and experimentation carried out in the REPL (if so, good on ya!), or a misapplication of StackOverflow advice from a previous failed attempt.  It is entirely unnecessary because `fobj` is never used again in this function.

In the design phase this author conflated the file object for the list of lines from the file and carried this misconception forth into the implementation.



### Concatenate lines into a string, just to split them back again *(WAT?)*

```python
 1  def tac(args):
 2      for fName in args:
 3          fObj = open(fName)
 4          fileLines = "" # Create empty string to store the file
 5          for line in fObj:
 6              fileLines += line
 7  
 8          splitString = fileLines.splitlines() # Split the string into a list at the new lines
 9          linesLength = len(splitString) - 1
10          while linesLength >= 0:
11              print(splitString[linesLength])
12              linesLength -= 1
13          fObj.close()
```

This is the kind of algorithm that you come up with when you code by the seat of your pants.  Concatenating a file read one-line-at-a-time into a string, just to split it up again is **not** something that will occur to you in the planning phase.

This person's plan was not very detailed; nevertheless, this implementation does not resemble their meager plan which spoke of a list that would be reversed.  This implementation creates a list in a very round-about way and does not reverse it.



### Slurp ALL lines into a single list, which effectively reverses the arguments *(WAT?)*

```python
 1  def tac(args):
 2      """:arg (List<String>) Files lines
 3      :return (String) Reverse concatinated output"""
 4      all_lines = []
 5      result = ""
 6      for file in args[1:]:
 7          file = open(file)  # This line was not here in the original; Erik is guessing how to fix it
 8          for i in file.readlines():
 9              all_lines.append(i)
10          file.close()  # This line was missing in the original; Erik is guessing how to fix it
11      all_lines.reverse()
12      for line in all_lines:
13          result += line
14      print(result)
```

The idea behind this implementation is close to the right track, but fails because it carelessly combines **ALL** files together into a single list, which is reversed.

A few moments spent testing this implementation alongside the example output would have revealed the mistake: `tac` is supposed to reverse the lines of each file *separately*.

An SDP was not written for this submission.

This code also fails because the call to `open()` was in the wrong place and the file object was not closed.


## Uses `reversed()` (good!), but only works for up to 2 files (*so* close!)

```python
 1  def tac(args):
 2      if len(args) == 4:
 3          textFile1 = args[2]
 4          textFile2 = args[3]
 5          file1 = open(textFile1)
 6          file2 = open(textFile2)
 7          for line in reversed(file1.readlines()):
 8              print(line, end='')
 9          for line in reversed(file2.readlines()):
10              print(line, end='')
11          file1.close()
12          file2.close()
13      elif len(args) == 3:
14          textFile = args[2]
15          file = open(textFile)
16          for line in reversed(file.readlines()):
17              print(line, end='')
18          file.close()
19      else:
20          usage(error="Too few arguments", tool="tac")
21          sys.exit(2)
```

While this implementation *does* work for the examples given, it does not live up to the requirement that the text tools take one **or more** arguments.


At 21 SLoC this is both the longest and least-capable example of the bunch.  In the interest of time this student wrote only a short plan that amounted to little more than a TODO list.  As a result, an important requirement was overlooked, yielding a program which is simultaneously less useful and too complex.  Following this line of thought it would be very difficult to make this program support 3 or more files.



<details>
<summary><h3>What I would do:</h3></summary>

```python
 1  def tac(args):
 2      """concatenate and print files in reverse"""
 3      for file in args:
 4          fobj = open(file, "r")
 5          for line in reversed(fobj.readlines()): # has to have a list of all the lines of the file in order for the reversed to work
 6              print(line, end="")
 7          fobj.close()
```

*   The advantage to this approach is that it is *clear* and *simple*
*   The drawback to this approach is that reversing a large file will be costly in terms of memory.
    *   If that is an important consideration a more sophisticated approach would be needed.

</details>



## Solutions to `tail`

`head` and `tail` are interesting tools because they both require

*   Handling an optional argument which itself takes an argument
    *   The argument following `-n` is required *and* must be an integer
    *   If the optional argument isn't given a default value is to be used
*   A banner naming each file is *only* displayed when multiple files are given on the command line

After solving the optional argument problem, `head` is just a `cat` that quits
early.  `tail` adds the additional complication of skipping to near the *end*
of the file and printing from there.

Your ideas about how to pull this off were surely be colored by your experience
of having written `tac`.  Did your plan survive its first contact with reality?


### Splits file in half instead of last 10 or `-n N` lines

This implementation prints (and returns) a list of strings instead of properly formatting its output.

Notice the duplicated code in each branch of the `if/else` conditional.  This was a common feature of many submissions.

The corresponding plan was not very detailed.

```python
 1  def tail(args):
 2      """output the last part of files"""
 3      print("TODO: output the last part of files")
 4      if args[1] == "-n":
 5          for fname in args[3:]:
 6              fileOb = open(fname)
 7              fileContents = fileOb.read()
 8              words = fileContents.split()
 9              secondHalf = words[len(words) // 2 if len(words) % 2 == 0
10                                 else ((len(words) // 2) + 1):]
11              splitHalf = secondHalf[0: int(args[2])]
12  
13              print(splitHalf)
14              fileOb.close()
15              return splitHalf
16  
17      else:
18          for fname in args[1:]:
19              fileOb = open(fname)
20              fileContents = fileOb.read()
21              words = fileContents.split()
22              secondHalf = words[len(words) // 2 if len(words) % 2 == 0
23          else ((len(words)//2)+1):]
24              print(secondHalf)
25              return secondHalf
```



### Read through each file twice

It's very easy to print the first `N` lines of a file.  This is just `cat` with an added variable and `if` statement.  The need to print `N` lines *back* from the end of a file of unknown length is *tricky*!

Reading through the file two times is a very common solution to this problem.  Either the file is closed and re-opened, or is `seek()`ed back to the top.

```python
 1  def tail(args):
 2  
 3      numFlag = 10
 4      if args[0] == "-n":
 5          try:
 6              numFlag = int(args[1])
 7          except ValueError as e:
 8              usage('Number of lines (as an integer) is required with option "-n"', "head")
 9              sys.exit(1)
10          strNumFlag = args[1]
11          args.remove("-n")
12          args.remove(strNumFlag)
13  
14      numOfLines = 0
15      for file in args:
16          f = open(file)
17          if len(args) > 1:
18              print(f"==> {file} <==")
19          for line in f.readlines():
20              numOfLines = numOfLines + 1
21          f.seek(0,0)
22          for i, line in enumerate(f):
23              if i >= numOfLines - numFlag <= numOfLines:
24                  print(line, end="")
25          numOfLines = 0
26          f.close()
```


### Duplicate code for 1 vs. N files

The added requirement of displaying a banner *only* when more than 1 filename is given complicates matters slightly.  But, as many of you learned, copying & pasting your code for each case multiplies the complication.

```python
 1  def tail(args):
 2      """output the last part of files"""
 3      # TODO: output the last part of files
 4      # checks to see if it has enough arguments
 5      if len(args) == 0:
 6          usage("Too few arguments", "tail")
 7      else:
 8          # more checks for arguments
 9          if args[0] == "-n":
10              if len(args) < 2:
11                  usage("Too few arguments", "tail")
12              else:
13                  # determines if it is valid argument
14                  numberOfLines = int(args[1])
15                  if numberOfLines < 0:
16                      usage("Invalid arguments", "tail")
17                  else:
18                      # iterates through and appends items to list
19                      printLines = numberOfLines
20                      args = args[2:]
21                      if len(args) == 1:
22                          file = open(args[0])
23                          x = 0
24                          lines = []
25                          for y in file:
26                              lines.append(y)
27                          if printLines > len(lines):
28                              equal = False
29                              while not equal:
30                                  printLines -= 1
31                                  if printLines == len(lines):
32                                      equal = True
33                          while x < printLines:
34                              print(lines[len(lines) - printLines + x], end="")
35                              x += 1
36                          file.close()
37                      # this is for multiple files
38                      else:
39                          for x in args:
40                              print("==> " + x + " <==")
41                              file = open(x)
42                              z = 0
43                              lines = []
44                              for y in file:
45                                  lines.append(y)
46                              while z < printLines:
47                                  print(lines[len(lines) - printLines + z], end="")
48                                  z += 1
49                              file.close()
50                              print("")
51          # The below section is exactly like the above section except that it uses the default values of 10
52          else:
53              printLines = 10
54              if len(args) == 1:
55                  file = open(args[0])
56                  x = 0
57                  lines = []
58                  for y in file:
59                      lines.append(y)
60                  if printLines > len(lines):
61                      equal = False
62                      while not equal:
63                          printLines -= 1
64                          if printLines == len(lines):
65                              equal = True
66                  while x < printLines:
67                      print(lines[len(lines) - printLines + x], end="")
68                      x += 1
69                  file.close()
70              else:
71                  for x in args:
72                      print("==> " + x + " <==")
73                      file = open(x)
74                      z = 0
75                      lines = []
76                      for y in file:
77                          lines.append(y)
78                      while z < printLines:
79                          print(lines[len(lines) - printLines + z], end="")
80                          z += 1
81                      file.close()
82                      print("")
```


### Forgot to handle `-n`; fails to close the file in a fun way

This brief solution skips over most of the requirements of the program; unsurprisingly this student's SDP was not filled out.

I'd like you to notice how the file is opened but *not* put into a variable at the top of the function (the variable `file1` is an array of strings, not a file object as you might expect).  At the end of the function the filename is opened again, and instantly closed in an attempt to close the originally opened file.

This does not work.  I'm sure this student felt that this code wasn't quite right as they wrote it.

```python
 1  def tail(searchFile):
 2      """output the last part of files"""
 3      # print("TODO: output the last part of files")
 4  
 5      file1 = (open(searchFile).readlines())
 6      iterations = len(file1)
 7      if len(file1) > 10:
 8          iterations = 10
 9  
10      for i in range(iterations):
11          print(file1[len(file1) - 10 + i].strip())
12  
13      open(searchFile).close()
```


### Misuse of `.isdigit()`; clever double `reverse()`; wasted `.seek()`

This submission features a helper function `checkValidity()` which was added to the `Usage` module to ensure that a filename can be accessed.  Very nice!

The use of `.isdigit` instead of the intended `.isdigit()` a few lines into the function is unfortunate because the program is incapable of detecting a non-numeric argument to `-n`.  A little more thorough testing would have uncovered this flaw.

Otherwise, good work, and a good translation from the original plan.

```python
 1  def tail(args):
 2      start = 2
 3      partialLength = 10
 4      # if given file path is invalid usage("Invalid path", head)
 5      # check for -n argument and N and applies to partialLenght int, partialLength is defaultly 10
 6      if len(args) <= start:
 7          usage("Too few arguments:", "head")
 8          sys.exit(1)
 9      if args[2] == "-n":
10          if len(args) <= start + 1:
11              usage("Too few arguments:", "head")
12              sys.exit(1)
13          if not args[3].isdigit:
14              usage("Enter an integer for # of lines", "head")
15          partialLength = int(args[3])
16          start = 4
17      checkValidity(args[start:], "head")
18  
19      # for each file:
20      for i in range(start, len(args)):
21          count = partialLength
22          f = open(args[i])
23          f.seek(0)
24          lines = f.readlines()
25          partialLines = []
26          # read the last partialLength number of lines and print each into console
27          for j in reversed(lines):
28              if count > 0:
29                  partialLines.append(j)
30                  count -= 1
31              else:
32                  break
33  
34          if len(args) - 1 > start:
35              print(f"==> {args[i]} <==")
36          for j in reversed(partialLines):
37              print(j, end="")
38          if len(args) - 1 > start:
39              print()
40  
41          f.close()
42          # if multiple files were given, create banner with file/path
43  
44          # close file(s)
```

We can prove for ourselves in the REPL that a condition on `.isdigit` will **NEVER** be `False`:

```
>>> bool("7".isdigit)
True

>>> bool("seven".isdigit)
True
```

</details>


### Over-complicated argument handling Considered Harmful

My complaint with this implementation is the way `-n` is searched for and handled.  This code assumes that the `-n N` may appear anywhere in the command line.  The command-line syntax shown in the documentation make it clear that this optional argument *only* appears at the beginning, right after the tool's name.  Unfortunately, this misunderstanding creates an unnecessary and confusing `for` loop in the middle of otherwise elegant code.

```python
 1  def tail(args):
 2      """
 3      output the last part of files
 4  
 5      Tail(files)
 6          if multiple files then add a title for each file
 7          if -n flag exists then set num of lines to keep else it is 10
 8          add the lines to a list
 9          print the last num of lines
10  
11      """
12      if len(args) < 1:
13          usage("Incorrect formatting", "tail")
14          return -1
15      numOfLines = 10
16      formatNumber = False
17      if "-n" in args:
18          remainingArgs = []
19          for element in args:
20              if formatNumber:
21                  if element.isdigit():
22                      numOfLines = int(element)
23                  else:
24                      usage("What follows the -n keyword is not a number", "tail")
25                      return -1
26                  formatNumber = False
27              elif element == "-n":
28                  formatNumber = True
29              else:
30                  remainingArgs.append(element)
31              args = remainingArgs
32      if formatNumber:
33          usage("Number of lines is required", "tail")
34          return -1
35      for file in args:
36          if os.access(file, os.R_OK):
37              textFile = open(file)
38          else:
39              usage("Files not Found", "tail")
40              return -1
41          if len(args) > 1:
42              print(f" ==> {file} <== ")
43          Output = []
44          for line in textFile.readlines():
45              Output.append(line.strip("\n"))
46          textFile.close()
47          for x in range(-numOfLines, 0):
48              print(Output[x])
```


### A clever use of of `min()`

This implementation is the shortest I found, and is *almost* perfect.  I really liked the use of the built-in `min()` function to avoid an `IndexError` when faced with a file that is shorter than the prevailing `numLines`.

*nitpick: the 2nd call to `usage()` mentions the wrong text-tool; copy & paste FAIL*

```python
 1  def tail(args):
 2      """output the last part of files"""
 3      if len(args) == 0:
 4          usage(error="Not enough arguments", tool="tail")
 5          sys.exit(1)
 6      if args[0].startswith("-n"):
 7          args.pop(0)
 8          if len(args) == 0 or not args[0].isnumeric():
 9              usage(error="Number of lines is required", tool="head")
10              sys.exit(1)
11          numLines = int(args.pop(0))
12      else:
13          numLines = 10
14  
15      for file in args:
16          if len(args) > 1:
17              print(f"==> {file} <==")
18          openFile = open(file, 'r')
19          lines = openFile.readlines()
20          openFile.close()
21          numLines = min(numLines, len(lines))
22          for i in range(len(lines) - numLines, len(lines)):
23              print(lines[i], end="")
```

However, once a file *shorter* than `numLines` is encountered, its length becomes the new `numLines` for the rest of the program (or until an even shorter file is encountered):

```
$ tt.py tail -n 13 data/words200 data/words5 data/random30
==> data/words200 <==
chucks
adumbrates
parse
convicting
exacerbating
indictment
very
impersonated
latching
reconfigurations
activates
autobiographies
adverbs
==> data/words5 <==
babbles
sneakiness
trimly
agree
frankly
==> data/random30 <==
28
65
94
93
29
```

This wasn't a failure of design.  Only thorough testing would have caught this bug.



### A robust and svelte implementation

At 21 SLoC for the function body, it doesn't get much better than this:

```python
 1  def tail(args):
 2      """output the last part of files"""
 3      if len(args) == 0:
 4          usage("not enough arguments supplied", "tail")
 5          sys.exit(1)
 6  
 7      numberOfLines = 10
 8      if args[0].lower() == "-n":
 9          if not str.isnumeric(args[1]):
10              usage(f"not a valid argument: '{args[1]}'", "tail")
11              sys.exit(1)
12          numberOfLines = int(args[1])
13          del args[0:2]
14  
15      for filePath in args:
16          fileObj = open(filePath)
17          fileText = fileObj.readlines()
18          fileObj.close()
19          del fileText[0:len(fileText) - numberOfLines]
20  
21          if len(args) > 1:
22              if filePath != args[0]:
23                  print()
24              print(f"-----{filePath}-----")
25          for line in fileText:
26              print(line, end='')
```

*nitpick: technically, the `-n` argument is case sensitive; this program will erroneously accept `$ python tt.py tail -N 7 ...`*

If you didn't know about Python's `del` keyword for removing items from a collection don't feel bad; you could have done the same thing with a list slice:

```
args = args[2:]
```

But now you have another cool Python trick up your sleeve!



