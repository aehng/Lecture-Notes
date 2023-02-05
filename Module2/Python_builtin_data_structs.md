# Python's Advanced Built-in Data Structures

*   [How to determine a value's type](#how-to-determine-a-values-type)
*   [Ordered Collections: Lists, Tuples, Ranges and Strings](#ordered-collections-lists-tuples-ranges-and-strings)
*   [Unordered Collections: Dictionaries and Sets](#unordered-collections-dictionaries-and-sets)
*   [Nesting data structures within data structures](#nesting-data-structures-within-data-structures)


## Overview

In assignment #3 you'll need the right data structure for the job.
So far you have been using *scalar* and *collection* values in our programs.

**Scalar**: an atomic quantity that holds only one value at a time

*   Integers: `0`, `-1`, `1337`
*   Floating point numbers: `0.0`, `-1.0`, `13.37`
*   Booleans: `True`, `False`
*   The `None` value


**Collection**: multiple values in one object

*   Lists: `[1, 2, 3]`, `sys.argv`
*   Strings: `"Hello world"`, `"tt.py"`

Strings seem to blur the line a little because we tend to think of them as
simple atomic values, but they are actually an *ordered* collection of characters.

The Python language provides other kinds of collections besides lists and
strings.  Some collections are *unordered*.  This document will introduce you
to the most important ones.


## How to determine a value's type

Use Python's `type()` function to discover the type of a value:

```
>>> type(1)
<class 'int'>

>>> type(13.37)
<class 'float'>

>>> type(True)
<class 'bool'>

>>> type(None)
<class 'NoneType'>

>>> a = 1
>>> type(a)
<class 'int'>

>>> a = 13.37
>>> type(a)
<class 'float'>
```

Python is a "dynamically typed" language.  This means that variables in Python
aren't fixed with respect to the type of value they may refer to.  For instance
a variable `a` may refer to an integer value at one moment, then it may be
assigned a list value, and later it can refer to an object.

This is in contrast to a "statically typed" language such as Java, where a
variable is permanently associated with a type, and that variable may only
refer to values of that type for the duration of the program.  In such a
language it is an error to attempt to assign a `string` value to a variable
declared as type `int`.  It is generally the case that compiled languages (e.g.
C++, Java, C#, Rust and Go) are statically typed because it leads to more
efficient machine code.  Another advantage is that some bugs can be detected in
the compile phase before the program is ever executed.

Interpreted "scripting" languages (e.g. Python, Ruby, Perl, Scheme, JavaScript)
tend to employ dynamic type systems.  Code in these languages is easier to
write and modify.  For instance, it can be possible to change the type of data
a function returns without being forced to update every line of code where the
function is called.  This supports experimentation and rapid prototyping.  On
the other hand, some bugs that might have been caught by a compiler will go
undetected until users have the misfortune of stumbling into them.

There are strengths and weaknesses to each type of language.  One kind of
language is not better than the other; they're just different.



### Creating Data Structures in Python

There area two ways to create data structures in Python: through *syntax* and
with *constructor functions*.

**Syntax**: the rules that define the combinations of symbols that are
considered to be a correctly structured program.

Literal values in a Python program have their own representation which, when
presented to the Python interpreter, evaluate to the same value.

*   `1` evaluates to `1`, an **integer**
*   `3.14159` evaluates to `3.14159`, a **floating point** number
*   `'hello'` evaluates to the **string** `"hello"`.
    *   This string contains characters in the same order they were entered in the source
    *   The choice between single `'` and double `"` quote marks does not matter in Python; both are acceptable
*   `['h', 'e', 'l', 'l', 'o']` evaluates to the **list** `['h', 'e', 'l', 'l', 'o']`.
    *   This list contains characters in the same order they were entered in the source
    *   This is similar to, but not equal to a string
*   `{'h', 'e', 'l', 'l', 'o'}` evaluates to the **set** of letters `{'l', 'h', 'o', 'e'}`
    *   Observe that the letters are now in a different order than they were entered in the source, and that one of the `'l'`'s is missing
    *   When you evaluate this in your REPL, the resulting **set** may display the letters in a different order than they did for me


**Constructor function**: A function which initializes and returns a new object.

*   `int("1")` creates the **integer** value `1` from the string `"1"`
*   `float("3.14159")` creates the **floating point** number `3.14159` from the string `"3.14159"`
*   `list("hello")` evaluates to `['h', 'e', 'l', 'l', 'o']`
    *   `list()` creates a new list from another type of sequence
    *   In this case the input sequence was a string
*   `set("hello")` evaluates to the **set** `{'l', 'h', 'o', 'e'}`
    *   `set()` creates an unordered set of the unique elements of its input sequence
    *   Just as before, when you run this in your REPL you may see the letters in a different order

In the following sections I will show you both ways to create each type of sequence (where possible).



## Ordered Collections: Lists, Tuples, Ranges and Strings

-   [Sequence Types — list, tuple, range](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
-   [PythonWiki - HowTo/Sorting](https://wiki.python.org/moin/HowTo/Sorting)

Sequence types store their contents in order.  There is a first element, a last
element, and the elements in between all know their place.  


### Lists

*   [Lists](https://docs.python.org/3/library/stdtypes.html#lists)

A list is created with the `list()` constructor function or with square
brackets `[]`.  Contrary to your expectations (and the beautiful example set
forth by LISP), the `list()` constructor function does not accept multiple
arguments; `list()` is meant to convert other sequence types (tuples, strings,
ranges...) into a list.

```
>>> l = [1, 2, 3, 4, 5] # list created with square brace syntax

>>> l
[1, 2, 3, 4, 5]

>>> type(l)
<class 'list'>  

>>> l[2] = 2222         # changing an element within a list

>>> l  
[1, 2, 2222, 4, 5]

>>> s = list("list of chars in string")  # list created with the list() constructor function

>>> s
['l', 'i', 's', 't', ' ', 'o', 'f', ' ', 'c', 'h', 'a', 'r', 's', ' ', 'i', 'n', ' ', 's', 't', 'r', 'i', 'n', 'g']

>>> empty = list()

>>> empty
[]

>>> type(empty)
<class 'list'>
```


### Tuples

*   [Tuples](https://docs.python.org/3/library/stdtypes.html#tuples)

A tuple is an immutable list.  *Immutable* means that the value is "not
changeable" or "read-only".  Tuples are created with the `tuple()` constructor
or with parentheses syntax:

```
>>> t = tuple([1, 2, 3, 4, 5]) # convert a list into a tuple

>>> t
(1, 2, 3, 4, 5)

>>> type(t)
<class 'tuple'>  

>>> t[2] = 2222         # changing an element within a tuple is an error
Traceback (most recent call last):  
  File "<stdin>", line 1, in <module>  
TypeError: 'tuple' object does not support item assignment  

>>> t = (7, 8, 9, 10)    # assigning a new tuple into t using tuple literal syntax

>>> t
(7, 8, 9, 10)

>>> s = tuple("tuple of chars in string")  # tuple created from a string + tuple()

>>> s
('t', 'u', 'p', 'l', 'e', ' ', 'o', 'f', ' ', 'c', 'h', 'a', 'r', 's', ' ', 'i', 'n', ' ', 's', 't', 'r', 'i', 'n', 'g')

>>> empty = tuple()

>>> empty
()

>>> type(empty)
<class 'tuple'>
```


### Ranges

*   [Ranges](https://docs.python.org/3/library/stdtypes.html#ranges)

A range gives us a way to efficiently store a huge sequence of integers in
memory without actually storing each value.  A range only needs to store the
beginning and end values along with the "step" (counting by twos, counting by
fives, etc.). The range can be turned into an honest to goodness list with the
list() constructor (provided you have enough RAM)

```
>>> r = range(10000000000000)

>>> r
range(0, 10000000000000)

>>> l = list(range(10000000000000))
Traceback (most recent call last):
  File "", line 1, in 
MemoryError
```

Because sequence types are ordered they may be *sorted*.  The Python Wiki has an
article about [sorting](https://wiki.python.org/moin/HowTo/Sorting) with some
useful recipes for sorting lists of varying degrees of complexity.


### Text Sequence Type - str

*   [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

Strings in Python are *immutable* sequences of Unicode *code points*.

*   **Immutable** - this means that strings cannot be changed.  Whenever you *think* you're changing a string, you're really making a copy of it
*   **Unicode code points** - strings are not actually sequences of 8-bit bytes.  This may or may not be evident as Python doesn't have a "character" data type - "characters" in Python are just strings of length 1.


## Unordered Collections: Dictionaries and Sets

In contrast to sequences, the values in sets and dictionaries are not stored in
any particular order. The concept of "first" or "next" doesn't make sense to
these collections.  Now, of course, the computer literally stores them in
_some_ order in memory.  To the user of the data structure this ordering may
appear random.  Your programs should not depend on the contents of these
structures being in any particular order, as the order can vary between
versions of Python, across different computers, or even between different runs
of the same program.

Like lists and tuples, there are two ways to make each of these collections, a
constructor and syntax.

-   [Dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
-   [Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
-   [Python Data Structures Tutorial](https://docs.python.org/3/tutorial/datastructures.html)



### Dictionaries

This data structure is one of the most useful and versatile tools available to
you in the Python language.  Once you learn how to use them, you will find that
they are the answer to many of your programming problems!

This data structure exists in many other programming languages, but it goes by many different names:

*   Hash tables
*   Hash maps
*   Hashes
*   Associative arrays
*   "Objects" in JavaScript are actually hash tables

Dictionaries may be created with the `dict()` constructor function or as a
comma-separated list of colon-separated key/value pairs within curly braces
`{}`.  Always remember that when constructing a dictionary using curly braces
that the presence of **colons**  determines whether the result will be a *set*
or a *dictionary*.

As with lists and tuples, items in a dictionary are retrieved with a subscript
written within square brackets `[]`.  Unlike a list which is always subscripted
with integers, a dictionary's key may be a string, a tuple, or a number.
Lists, sets, and other dictionaries may *not* be used as keys.  The rule of
thumb is that **immutable** objects can be used as keys.  This means that you
can use *real* and *complex* numbers as keys, but this is seldom a good idea.

```
>>> d = dict(name="Erik Falor", anumber="Nice Try ;)", phone=4357974118)

>>> d
{'name': 'Erik Falor', 'anumber': 'Nice Try ;)', 'phone': 4357974118}

>>> type(d)
<class 'dict'>

>>> d['name']
'Erik Falor'  
```

New elements are added to a dictionary by assigning directly to a key:

```
>>> d['astrological sign'] = 'Aries'

>>> d[(0, 1, 2)] = "Indexed by a tuple"

>>> d
{'name': 'Erik Falor', 'anumber': 'Nice Try ;)', 'phone': 4357974118,
'astrological sign': 'Aries', (0, 1, 2): 'Indexed by a tuple'}
```

Assigning a value to a key that is already present *overwrites* the existing value:

```
>>> d['astrological sign'] = 'Taurus is a sign, right?'

>>> d['name'] = 'Revx Snybe'

>>> d
{'name': 'Revx Snybe', 'anumber': 'Nice Try ;)', 'phone': 4357974118,
'astrological sign': 'Taurus is a sign, right?',
(0, 1, 2): 'Indexed by a tuple'}
```


Elements can be removed from a dictionary with the `del` keyword:

```
>>> del d['phone']

>>> del d['astrological sign']

>>> d
{'name': 'Revx Snybe', 'anumber': 'Nice Try ;)', (0, 1, 2): 'Indexed by a tuple'}
```


### Sets

Sets are constructed with the `set()` constructor or as a comma-separated list of values within curly braces `{}`.

```
>>> s = set(range(7))

>>> s
{0, 1, 2, 3, 4, 5, 6}

>>> type(s)
<class 'set'>

>>> s.add(20)

>>> s
{0, 1, 2, 3, 4, 5, 6, 20}

>>> 6 in s
True
```

A set literal is distinguished from a dictionary by the absence of `:` in between its values.

Unlike dictionaries, items are removed from sets with the `discard()` and `remove()` methods:

```
>>> s.discard(6)
>>> s.remove(4)
```


The difference between these methods is their behavior when the item is *not* in the set: `remove()` raises `KeyError` while `discard()` silently fails:

```
>>> s.discard(4)

>>> s.discard(4)  # no error the 2nd time

>>> s.remove(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 4
```

Sets are useful for answering the question "have I seen *X* before?".  You can do the same thing with a dictionary by giving all keys some value, and just never looking at the value.  This tip is useful in programming languages which do not provide a `set` data type.



## Nesting data structures within data structures

All of these data structures can be placed within other data structures without restriction:


### Tuples within tuples (a.k.a. read-only 2D arrays)

```python
t_of_t = (
    ('ZERO', 'ONE', 'TWO'),
    ('THIRTY', 'THIRTY-ONE', 'THIRTY-TWO'),
    ('THREE-HUNDRED', 'THREE-HUNDRED-ONE', 'THREE-HUNDRED-TWO')
    )
```

#### Accessing elements within the nested tuple

```python
# print element 1 from each tuple naively:
print(t_of_t[0][1])
print(t_of_t[1][1])
print(t_of_t[2][1])


# print element 2 from each tuple using a loop:
for tup in t_of_t:
	print(tup[2])


# print every element of each tuples
for tup in t_of_t:
	for e in tup:
		print(e, end=', ')
	print()
```


### Lists within lists (a.k.a. 2D arrays)

```python
l_of_l = [
    ['zero', 'one', 'two'],
    ['thirty', 'thirty-one', 'thirty-two'],
    ['three-hundred', 'three-hundred-one', 'three-hundred-two']
    ]
```


#### Accessing, changing, adding and removing elements within the nested list

```python
# Accessing 2nd column of 3rd row (i.e. 301)
print(l_of_l[2][1])


# Replacing "thirty-one" with 1337
l_of_l[1][1] = 1337
print(l_of_l[1][1])


# Adding new elements to the list in the middle
l_of_l[1].append(42)
l_of_l[1].append("Hello")
l_of_l[1].append("World")


# Deleting the middle element of the 0th row ("one")
del l_of_l[0][1]


# Printing the whole thing takes two loops
for row in l_of_l:
	for col in row:
		print(col, end=', ')
	print()
```



### Dictionaries within dictionaries


#### Nested dictionaries created with the `dict()` type constructor

```python
roles = dict(
	Knight=dict(strength=15, intelligence=8, wisdom=15, dexterity=8, constitution=11, charisma=17),
	Rogue=dict(strength=15, intelligence=14, wisdom=14, dexterity=18, constitution=14, charisma=8),
	Tourist=dict(strength=11, intelligence=13, wisdom=9, dexterity=11, constitution=15, charisma=16),
	Wizard=dict(strength=15, intelligence=18, wisdom=10, dexterity=13, constitution=13, charisma=10))
```

#### Creating the same with dictionary literal syntax:

```python
roles = {
	'Knight' : {
		'strength': 15,
		'intelligence':  8,
		'wisdom':  15,
		'dexterity':  8,
		'constitution':  11,
		'charisma': 17
		},

	'Rogue' : {
		'strength': 15,
		'intelligence': 14,
		'wisdom': 14,
		'dexterity': 18,
		'constitution': 14,
		'charisma': 8
		},

	'Tourist' : {
		'strength': 11,
		'intelligence': 13,
		'wisdom': 9,
		'dexterity': 11,
		'constitution': 15,
		'charisma': 16
		},

	'Wizard' : {
		'strength': 10,
		'intelligence': 18,
		'wisdom': 10,
		'dexterity': 13,
		'constitution': 13,
		'charisma': 10
		},
}
```


#### Accessing, changing, adding and removing elements within the nested dictionary

```python
# Accessing the Rouge's charisma stat
print(roles['Rogue']['charisma'])


# Buff the Wizard's strength to equal that of the Knight
roles['Wizard']['strength'] = roles['Knight']['strength']


# Give the Rouge a new "deviousness" stat
roles['Rogue']['deviousness'] = 16


# Remove the Tourist's dexterity stat (he wasn't using it, anyway)
del roles['Tourist']['dexterity']


# Add a new "Barbarian" role to the game
roles['Barbarian'] = {
		'strength': 18,
		'intelligence': 7,
		'wisdom': 7,
		'dexterity': 17,
		'constitution': 18,
		'charisma': 6
		}


# print all stats for all roles
for role in roles:
	print(f"Stats for the {role} role:")
	for stat in roles[role]:
		print(f"\t{stat} = {roles[role][stat]}")
	print()
```


### Mixing types

There are, of course, no restrictions on which types of collections that can be stored within another collection.  This is a list of dictionaries that is equivalent to the dictionary of dictionaries defined above.  This time the name of the role is stored within each dictionary:

```python
roles = [
    {
        'rolename': 'Knight',
        'strength': 15,
        'intelligence':  8,
        'wisdom':  15,
        'dexterity':  8,
        'constitution':  11,
        'charisma': 17
    },

    {
        'rolename': 'Rogue',
        'strength': 15,
        'intelligence': 14,
        'wisdom': 14,
        'dexterity': 18,
        'constitution': 14,
        'charisma': 8
    },

    {
        'rolename': 'Tourist',
        'strength': 11,
        'intelligence': 13,
        'wisdom': 9,
        'dexterity': 11,
        'constitution': 15,
        'charisma': 16
    },

    {
        'rolename': 'Wizard',
        'strength': 10,
        'intelligence': 18,
        'wisdom': 10,
        'dexterity': 13,
        'constitution': 13,
        'charisma': 10
    },
    ]

for role in roles:
    print(f"Stats for the {role['rolename']} role:")
    for stat in role:
        if stat == 'rolename':
            continue
        print(f"\t{stat} = {role[stat]}")
    print()
```
