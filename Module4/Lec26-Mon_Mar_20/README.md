CS1440 - Monday, March 20 - Lecture 26 - Module 4

# Topics:
* [Announcements](#announcements)
* [Retrospective: Assignment #4](#retrospective-assignment-4)
* [Assignment #4 Code ~~Review~~ Roast](#assignment-4-code-review-roast)
* [Assn 5.0: Fractal Visualizer - Refactoring](#assn-50-fractal-visualizer-refactoring)
* [Using complex numbers in Python](#using-complex-numbers-in-python)


------------------------------------------------------------
# Announcements

## [HackUSU](https://www.hackusu.com/) - Utah's Premiere Collegiate Hackathon

*   **What**  Build a software or hardware project to compete against other teams. All college students and high school seniors are invited!
*   **When**  4:00pm Friday, March 24 - Saturday, March 25
*   **Where** Huntsman Hall


# Action Items

*   Work on phase **0. Requirements Analysis** of the new assignment *today*
    *   Wrap it up *tomorrow*
*	Call on 2 designated questioners



# Retrospective: Assignment #4

## The three L's: **Liked**, **Learned**, **Lacked**

Pick up 3 sticky notes and write your answer each of these three questions:

*   What did you **like** about this assignment?
*   What did you **learn** from this assignment?
*   What do you feel that you **lacked** in this assignment?

Post them on the white board in the appropriate location.

There were 18 days from *Monday, Feb. 27* to *Friday, Mar 17*




# Assignment #4 Code ~~Review~~ Roast

*Disclaimer: Please don't take it personally if it is your code shown here.  I wanted to show the most common mistakes I came across throughout all of the submissions.  If I happened to pick yours, it was just the luck of the draw*


## Pop quiz

<details>
<summary>Don't say anything out loud.</summary>

```python
class Card():
    def __init__(self, idnum, ns):
        """
        Initialize a Bingo! card
        """
        self.__idnum == idnum
        self.__ns == ns
```

<details>
<summary>Raise your hand when you spot the bug</summary>

`==` instead of `=`
</details>

</details>



## PyCharm, for the last time, `src` is not a package

Don't do this.  Fix your IDE instead.

```
sys.path.insert(0, './/src')
```

You made the Don sad.

![./32-massacred.jpg](./32-massacred.jpg "Look how they massacred my boy")


## Who keeps cards in a dictionary, anyways?

This actually accidentally works:

```python
self.__cards = {}  
```

You're lucky that Python dictionaries remember the order that keys are inserted.  Otherwise the Cards in your Deck would be permanently shuffled!


## Pet Peeve: Loops

A lot of you wrote loops that quit when a variable changes from `False` to `True`:

```python
done = False
while not done:
    ...
    done = True
```

You could have just used `break` instead of keeping track of a variable:

```python
while True:
    ...
    break
```

Some did both:

```python
done = False
while not done:
    ...  # doesn't look at done ever again
    break
```

This forever loop was new to me:

```python
while not False:
    ...
    break
```


## Pet Peeve: Setting a boolean variable

Don't write 4 lines of code when 1 will do.  You want `self.free` to be either `True` or `False`?

```python
     1	if len(ns) % 2 != 0:
     2	    self.free = True
     3	else:
     4	    self.free = False
       
     5	if self.free:
     6	    self.rows[(len(ns) // 2)][(len(ns) // 2)] = "FREE!"
```

Just assign the result of the Boolean operation directly to the variable:

```python
     1	self.free = len(ns) % 2 != 0
     2	if self.free:
     3	    self.rows[(len(ns) // 2)][(len(ns) // 2)] = "FREE!"
```


In this program the variable is just a waste of space, since it's never used again.  So why bother?

```python
     1	if len(ns) % 2 != 0:
     2	    self.rows[(len(ns) // 2)][(len(ns) // 2)] = "FREE!"
```

### There and back again: A Random Number's Journey

I found this in Deck.py.  Notice that the `RandNumberSet` is converted to a `str` before it's passed to `Card()`:

```python
for i in range(self.num_cards):
    self.deck.append(Card(i + 1, str(RandNumberSet(self.card_size, max_num)), self.card_size))
```

I defined `RandNumberSet.__str__()` while debugging and testing.  It returns a big, long string that makes a `RandNumberSet` look like a series of arrays.  But that can only mean...

```python
     1	class Card():  	    	       
     2	    def __init__(self, idnum, ns, size):  	    	       
     3	        self.idnum = idnum
     4	        self.size = size        
     5	        temp_ns = ns.replace("[", "").replace("]", "").replace(",", "").split("\n")
     6	        self.ns = []
     7	        for item in temp_ns:
     8	            self.ns.append(item.split(" "))
     9	        if len(self.ns) % 2 != 0:
    10	            self.ns[ceil(self.size / 2) - 1][ceil(self.size / 2) - 1] = "Free!"
    11	        return self.ns
```

![32-nooooo.gif](./32-nooooo.gif "Nooooooooooooooo!")



### Placing FREE! spaces in the middle of a `Card`

*n.b. In this code example the `//` operator is employed.  This is the "floor division" operator, a.k.a. the "integer division" operator, which throws away the fraction portion of a dividend.  `a // b` is equivalent to `math.floor(a / b)`.*

```python
class Card():
    def __init__(self, idnum, size, randNumberSet):
        """Card constructor"""
        self.__m_idnum = idnum
        self.__m_values = [[None for i in range(size)] for j in range(size)]
        randNumberSet.shuffle()
        freeIndex = size + 1
        if size % 2 == 1:
            freeIndex = size // 2
        for i in range(size):
            for j in range(size):
                for n in randNumberSet.next_row():
                    if i == freeIndex and j == freeIndex:
                        self.__m_values[i][j] = "FREE"
                    else:
                        self.__m_values[i][j] = n
```

This strikes me as having been written before being designed.  I don't believe that your duckie would come up with an algorithm like this.

What grabs my attention is the `if/else` within a triple `for` loop.  That test is going to be executed **a lot**, so you should ask yourself if there is a way to "pull" it out of the loops so that it runs either before or after the loops.  If it cannot be extracted, see if you can at least pull it out of the innermost loop: that's the difference between doing something $`N^{2}`$ times versus $`N^{3}`$.

*   Every single time the program fills out a square, it has to stop and check whether *this* time it is in the middle square.
*   Even after it's already placed the `"FREE"` square in the middle, the program still dutifully checks to see if it's in the middle
*   Worse still, this test still happens on even-sized cards which **CAN'T** have a middle square.
    *   Although things are set up such that it is impossible to place a `"FREE"` square on an even-sized card, this program still has to do the check!


Instead of looking for the middle square $`N^{2}`$ times, it's simpler to overwrite the middle square with `"FREE"` after the fact.

<details>
<summary>Not only is this formulation faster, but it is shorter and easier to understand:</summary>

```python
class Card():
    def __init__(self, idnum, size, randNumberSet):
        """Card constructor"""
        self.__m_idnum = idnum
        self.__m_values = [[None for i in range(size)] for j in range(size)]
        randNumberSet.shuffle()
        for i in range(size):
            for _ in range(size):
                self.__m_values[i] = randNumberSet.next_row()

        # The middle square (when there is one) is FREE
        if size % 2:
            self.__m_values[size // 2][size // 2] = "FREE"
```
</details>


After making that change, it becomes obvious that this program uses **two** pairs of nested `for` loops to initialize the card.

0.  The first pair of loops is in a list comprehension, and makes an $`N \times N`$ grid of `None` values
1.  The next pair of loops replaces the `None` values with numbers from the `RandNumberSet`.

Does it really take two pairs of `for` loops to fill in a `Card`?

<details>
<summary>Why bother with the <code>None</code> values?</summary>

You may as well insert from the `RandNumberSet` to begin with.  This is exactly what the `next_row()` method is for:

```python
class Card():
    def __init__(self, idnum, size, randNumberSet):
        """Card constructor"""
        self.__m_idnum = idnum
        randNumberSet.shuffle()
        self.__m_values = [randNumberSet.next_row() for _ in range(size)]

        if size % 2:  # The middle square (when there is one) is FREE
            self.__m_values[size // 2][size // 2] = "FREE"
```

*Code style note: I used the variable name `_` instead of `i` within the list comprehension because I never used its value.  The variable name `_` informs the reader that variable is not important and can be ignored.*
</details>


### So close, yet so far away

I was so hopeful when I saw line 6.  But then I noticed line 11.  Then I wondered what the rest of the initializer was doing...

```python
     1	class Card():
     2	    def __init__(self, idnum, ns, size):
     3	        self.idnum = idnum
     4	        self.ns = ns
     5	        self.size = size
     6	        self.dataList = [[None for _ in range(size)] for _ in range(size)]
       
     7	        rowCounter = 0
     8	        subArrayCounter = 0
     9	        subArrayLengthCounter = 0
    10	        self.ns.shuffle()
    11	        numList = [[None for _ in range(len(self.ns.get_segments()[0]))] for _ in range(self.ns.__len__())]
       
    12	        while subArrayCounter < self.ns.__len__():
    13	            while subArrayLengthCounter < len(self.ns.get_segments()[self.ns.__len__() - 1]):
    14	                numList[subArrayCounter][subArrayLengthCounter] = self.ns.get_segments()[subArrayCounter][subArrayLengthCounter]
    15	                subArrayLengthCounter += 1
    16	            subArrayCounter += 1
    17	            subArrayLengthCounter = 0
       
    18	        while rowCounter < size:
    19	            rowCounterForData = 0
    20	            columnCounter = 0
    21	            while columnCounter < size:
    22	                self.dataList[rowCounter][columnCounter] = numList[rowCounterForData][0]
    23	                numList[rowCounterForData].pop(0)
    24	                rowCounterForData += 1
    25	                columnCounter += 1
    26	            rowCounter += 1
       
    27	        if self.size % 2 == 1:
    28	            self.dataList[int((size-1)//2) ][int((size-1)//2) ] = "Free!"
```

This initializer does the exact same thing:

```python
     1	class Card():  	    	       
     2	    def __init__(self, idnum, ns, size):  	    	       
     3	        self.idnum = idnum
     4	        self.ns = ns
     5	        self.size = size
       
     6	        self.ns.shuffle()
     7	        self.dataList = [ns.next_row() for _ in range(size)]
       
     8	        if self.size % 2 == 1:
     9	            self.dataList[(size-1)//2][(size-1)//2] = "Free!"
```


### Don't be a dunder head

This was the most common mistake I noticed this semester.  Lots of you called dunders directly!

```python
def getCard(self):
    """
    Prints out the specified card by returning a String
    """
    string = str(self.__str__())
    self.__card = string
    return string
```

When you define a method `__str__`, you don't need to call it as `object.__str__()`, but rather `str(object)`.  Python's built-in functions `len()`, `str()` and the operator `[]` are just *syntactic sugar* for calling the associated dunder method (`__len__`, `__str__`, and `__getitem__`).  *Syntactic sugar is what we call the little conveniences programming languages provide to help us write more readable code.*

Calling the dunder directly doesn't make your program do the wrong thing; it just means that you did more typing than necessary.

This line:

```python
string = str(self.__str__())
```

actually calls `__str__` twice!  First, it calls `Card.__str__()`, then it calls Python's built-in `str()`.

It should have been written as:

```python
string = str(self)
```


<details>
<summary>What's wrong from a software design point of view</summary>

`Card.getCard()` is doing the same thing as `Card.__str__()`.  It is unnecessary and should be deleted.

However, this student tried to do something interesting, which is to *cache* the result of `Card.__str__()`.  Because a Card's appearance never changes, this would be a viable optimization if it were particularly expensive to visualize a card.  Unfortunately, this student never made use of the cached string.  A correct implementation could look like this:

```python
def getCard(self):
    """
    Compute the String representation of a Card once;
    Return the cached string
    """
    if self.__card is None:
        self.__card = str(self)
    return self.__card
```

You might take this a step further and roll this caching logic directly into `Card.__str__()`.

Again, I wouldn't actually do this for this program; I don't feel that displaying a Card is so computationally expensive that it justifies the added complexity of including and maintaining a cache.

</details>


### Not playing with a full deck

The most natural implementation of `Deck` is that it contains an array of `Card` objects.  I'm looking for it and coming up with `404: Not Found`:


#### Deck.py

```python
class Deck():
    def __init__(self, card_size, num_cards, max_num):  	         	  
        self.num = num_cards
        sz = int(card_size)
        num = int(num_cards)
        hi = int(max_num)
        for i in range(num):
            id = i+1
            Card(id,RandNumberSet(sz,hi))

    def card(self, n):  	         	  
        c = int(n)*2
        print(Card.card[c-1])  
        print(Card.card[c])
```

*Hint: why does `Deck.card()` refer to the static attribute `card` of the `Card` class (e.g. in `print(Card.card[c])`)?*



<details>
<summary>Psst! Try looking at Card.py</summary>

```python
class Card():
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	         	  
    card = []
    def __init__(self, idnum, ns):
        self.card = Card.card
        self.idnum = idnum
        self.ns = ns
        self.num = []
        count = 0
        RandNumberSet.shuffle(self.ns)
        free = ((self.__len__()**2)/2)+.5
        for k in self.ns:
            for p in k:
                count += 1
                if count == free:
                    self.num.append("FREE!")
                else:
                    self.num.append(p)
        self.card.append("Card #"+str((len(Card.card)//2)+1))
        self.card.append(self.__str__())
```

As the Deck is built up, the string representation of each card is appended onto the list `Card.card`.  A `Card` is stored as two strings - the Card's header, then the body itself. Later, when the deck of cards is displayed or written to a file, `Deck.card()` is called with the card's ID number.  Because every `Card` is stored as two strings, this number must be doubled before the correct `Card` is retrieved from the deck.

</details>





# [Assn 5.0: Fractal Visualizer - Refactoring](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn5)

This program creates images of the Mandelbrot Set and other related fractals.
Ultimately, DuckieCorp will release an improved version of this program, but
before we can make it better we need to first make it *good*.

Your job for this assignment is to convert a messy program into a nice, clean
program that does the same thing.  The process of improving source code is
called *refactoring*.


## I'm afraid of breaking this program and getting stuck!

Read the section titled *Testing and reverting mistakes* in `instructions/Hints-5.0.md`.
As long as you go slow, step through the program with the debugger, use git
frequently, and test everything you do, you'll be fine.

**You can complete this assignment even if you don't really know what's going on...**

All you really need to know is that it is possible to make *small changes* to a
program that preserve its overall behavior, even if you don't really understand
everything that's going on.

0.  Some lines of code can be rearranged in ways that preserve their original meaning while making them *look* cleaner
    *   Re-run the program; if the program doesn't crash or do something different, your change probably wasn't bad
1.  You can identify certain lines of code that *don't matter* to the program by commenting them out
    *   Re-run the program; if the program doesn't crash or do something different, that line probably didn't need to be there
2.  You know enough about [Git](../../Using_Git/Intermediate_Git.md) to undo your mistakes and try again
    *   With Git your screw-ups aren't forever! (TM)


## But I don't know anything about fractals!

**...but it does feel nice to know what's going on**

What is an image but a grid of colored pixels?  For any picture you can ask the
question "why is this pixel this color?"

This program implements an algorithm called the ["Escape Time" algorithm](http://mathworld.wolfram.com/MandelbrotSet.html)
which is used to decide which color each pixel should be.

This algorithm is explained in greater detail in `instructions/Hints-5.0.md` in the starter code repository:

https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn5/-/blob/master/instructions/Hints-5.0.md#understanding-the-fractal-algorithms

I created a demo program in the starter code repo that will help you grasp the
concept:

[Demo: interactive Mandelbrot viewer](https://gitlab.cs.usu.edu/erik.falor/cs1440-falor-erik-assn4/blob/master/demo/interactive.py)


## But I don't know anything about `tkinter` or GUIs!

It is possible to refactor a program without a deep understanding of how the
code works.  Throughout your career you will be asked to work on huge programs
that you have never seen before nor fully understand.  At the beginning of the
project you will feel lost and confused.

This assignment is *specifically designed* to evoke the feeling of being lost
in a big code base.  As you spend time reading the code, testing and running
through it in the debugger, you will gradually come to understand how and why
it works.

The feeling of confusion you will face in this assignment is heightened because
this code is purposefully written in a bad way.  Throughout your career you
will be asked to work on horribly ill-designed abominations of spaghetti code.
When that happens to you at work it won't be the first time because you will
finish this assignment.

Always remember that the first portion of this assignment (5.0) doesn't ask you
to change what this program does.  You need only to re-arrange the working code
so that it's easier to understand and change later.

As long as you

*   go slow
*   step through the program with the debugger
*   use git frequently
*   and test everything you do

you'll be fine!


<details>
<summary><h2>Advice students gave last semester</h2></summary>

*   Read all of the instructions before starting.  Then read them again partway through the project
*   Visit the CS Tutoring Center, or find somebody who will let you explain the program in layman's terms
*   Start early - the assignment may take longer than you expect
    *   I did the assignment on the due date, and spent 16 hours finishing it.  It was the most miserable thing ever.
*   The starter code is hard to read, but this program isn't really that complicated
*   The debugger is your friend
    *   Run the program in the debugger to learn the flow of information
*   Don't get caught up in the details of useless code
*   To "refactor" means to edit or to reword; it does not mean "recreate from scratch" like my gut told me to do
*   Only make *one* small change, then test the program.
    *   Commit or revert that change depending on how the test went
*   Write the unit tests and always make sure they pass; if a test starts failing (e.g. from renaming a function) fix the test so you can always tell if the function is working
*   Take plenty of time just to sit with the code.
    *   Write some notes about what's duplicated, what's inefficient, and where to expand or create new functions
*   At the end of the day, the starter code does work.
    *   Take the parts it does well and apply them in the final version
*   Clean up the code before dividing it among the new modules

</details>



# Using complex numbers in Python

Complex numbers are a built-in data type in the Python programming language.
Just like any other builtin type in Python, there are two ways to construct
complex number objects:

*   **Literal Syntax**: write a floating-point number followed by `+` or `-`,
    followed by another floating-point number, followed by `j`
    *   Examples:
        *   `0+0j`
        *   `3.14159-1.414213j`
        *   `0+2.718281j`
        *   `-13.37j`
*   **Constructor Function**: `complex(real, imag)`.  This is the preferred way
    to convert a pair of real `X`, `Y` values into a complex number
    *   Examples:
        *   `complex(x, y)`
        *   `complex(0, 0)`
        *   `complex(3.14159, -1.414213)`
        *   `complex(0, 2.718281)`
        *   `complex(0, -13.37)`

Complex numbers can be used in Python arithmetic expressions just like real
numbers.  When using complex numbers together with real numbers and integers in
an expression, Python automatically converts the participating values into the
same type for you; you don't need to *cast* them yourself.  This behavior of
the language is called *type coersion*.


```python
>>> complex(3, 7) * complex(2, 5)
(-29+29j)

>>> complex(3, 7) * (2+5j)
(-29+29j)

>>> 27.0 * complex(2, 5)
(54+135j)
```

Complex literals used in arithmetic expressions may need to be surrounded in parentheses so they are parsed correctly.  This is true for complex numbers with a *real* component of zero:

```python
>>> 17 / complex(0, 1)
-17j

>>> 17 / 0+1j
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> 17 / (0+1j)
-17j

>>> 3+7j * 2+5j
(3+19j)              # wrong!

>>> 3 + 7j * 2 + 5j  # is parsed like this
(3+19j)

>>> (3+7j) * (2+5j)  # this is what I meant
(-29+29j)

>>> complex(3, 7) * complex(2, 5)
(-29+29j)
```

You can extract the real and imaginary components. They come out as floats:

```python
>>> c = complex(3, 7)

>>> c.real
3.0

>>> c.imag
7.0
```


## The absolute value of complex numbers

One notable difference between complex numbers and real numbers is that the
absolute value of a complex number is calculated as a distance from origin on a
plane instead of as the distance from a point on a line.

This is of little consequence to us as Python's built-in function `abs()`
automatically handles complex numbers the correct way.  If you are interested
in the details, you can read about it in
[this explanation](https://www.mathwarehouse.com/algebra/complex-number/absolute-value-complex-number.php)


## More info about `Complex` values in Python:

*   https://docs.python.org/3/library/functions.html?highlight=complex#complex
*   https://docs.python.org/3/library/stdtypes.html#typesnumeric



