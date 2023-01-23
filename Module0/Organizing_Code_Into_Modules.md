# Organizing Code Into Modules

* [Modular Programming](#modular-programming)
* [What goes into a module?](#what-goes-into-a-module)
* [How to write a module in Python](#how-to-write-a-module-in-python)
* [Using modules in Python](#using-modules-in-python)
* [Namespaces](#namespaces)
* [What file was this module defined in?](#what-file-was-this-module-defined-in)
* [When is the code in a module executed?](#when-is-the-code-in-a-module-executed)
* [Can a Python file tell when it is being used as a program or a module?](#can-a-python-file-tell-when-it-is-being-used-as-a-program-or-a-module)
* [System-Defined Names (how to stay off of Guido's lawn)](#system-defined-names-how-to-stay-off-of-guidos-lawn)


## Modular Programming

> Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality.
>
> - Modular programming on [Wikipedia](https://en.wikipedia.org/wiki/Modular_programming)

Related pieces of code are collected into larger entities called 'Modules'.  Modules may or may not be useful as programs unto themselves, but, what we most often think of as a module is *not* a complete, standalone program.

Modules may be selectively included into a useful program.  Modules encourage code reuse by enabling libraries of commonly desired general-purpose code to be readily shared between different applications.

Examples: Java/Python packages, C/C++ header files (`#include <iostream>`)

[Python Tutorial: 6. Modules](https://docs.python.org/3/tutorial/modules.html)


## What goes into a module?

Pieces of code which serve a *related* purpose can be put together into a module.  In this sense the related purpose is not that "this code is used in the same program".  Code sharing a module should be unified by purpose.

Variables, functions and classes can be moved out of a program and put into a module.  This makes it convenient for other programs to use that same code without copying and pasting it from file to file.

The names of variables and functions are collectively known as *identifiers*.

#### [Identifier](https://en.wikipedia.org/wiki/Identifier#In_computer_languages)
A textual token that identifies a programming entity.

In Python identifiers are the names of variables, functions, modules and classes.  Special words such as `for`, `def` and `class` look like identifiers but are in a special class of *keywords*.

[Python documentation - Identifiers and keywords](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)


| Object                         | Is it an identifier?
|--------------------------------|---------------------------------------
| A variable `y`                 | true
| A variable `__name__`          | true
| A variable `_`                 | true
| The number `0`                 | false (this is a integer literal)
| A function named `all`         | true
| `while`                        | false (this is a keyword)
| The number `3.14`              | false (this is a floating-point literal)
| `+`                            | false (this is an operator)
| `if`                           | false (this is a keyword)
| A class named `Duckie`         | true
| A module named `Colour`        | true
| A function named `rotate`      | true
| The string `"Hello world"`     | false (this is a string literal)
| A list `[all, rotate, y]`      | false (this is a list literal which happens to contain identifiers, but is not an identifier itself)
| `l` in `l =  [all, rotate, y]` | true


## How to write a module in Python

You've been writing modules all along; every Python source file *is* a module!


## Using modules in Python

Modules are *imported* into a running Python program with the `import` keyword.  When importing a file you import it by its file name, dropping the '.py' extension.

You should match the case of the name of the file when importing it as a module, even if your operating system doesn't respect the case of file names.

Suppose I have a file named `CoolCode.py` with these contents (note the capitalization of the file's name):

```python
TEMPERATURE = 32

def srslyCool():
    print("""\x1b[1;36m\
               88888888888888     d8b           d8b
                   888    888     Y8P           Y8P
                   888    888
                   888    88888b. 888.d8888b    888.d8888b
                   888    888 "88b88888K        88888K
                   888    888  888888"Y8888b.   888"Y8888b.
                   888    888  888888     X88   888     X88
                   888    888  888888 88888P'   888 88888P'

                              d8b                        888
                              Y8P                        888
                                                         888
       .d8888b  .d88b. 888d888888 .d88b. 888  888.d8888b 888888  888
       88K     d8P  Y8b888P"  888d88""88b888  88888K     888888  888
       "Y8888b.88888888888    888888  888888  888"Y8888b.888888  888
            X88Y8b.    888    888Y88..88PY88b 888     X88888Y88b 888
        88888P' "Y8888 888    888 "Y88P"  "Y88888 88888P'888 "Y88888
                                                                 888
                                              888888        Y8b d88P
                                              888888         "Y88P"
                                              888888
                       .d8888b .d88b.  .d88b. 888888
                      d88P"   d88""88bd88""88b888888
                      888     888  888888  888888Y8P
                      Y88b.   Y88..88PY88..88P888 "
                       "Y8888P "Y88P"  "Y88P" 888888\x1b[0m""")
```


When I want to import this file into my program, I cannot write this import statement:

```python
import coolcode
```

Although this import statement will work on Windows, it is only by accident.  A program using that import statement will crash on Linux and Mac.  To write programs that work equally well on *all* computers, **always** match the case of the file's name when importing:

```python
import CoolCode
```

When a module is located under a subdirectory (for instance `CoolModules/CoolCode.py` on Linux/Mac or `CoolModules\CoolCode.py` on a game console), replace `/` or `\` in the path with dots `.`.  Thus, the file `CoolModules/CoolCode.py` is imported as

```python
import CoolModules.CoolCode
```

This works for modules deeply nested under many subdirectories.  As another example, the file `This/Is/Getting/Ridiculous/CoolModules/CoolCode.py` is imported as

```python
import This.Is.Getting.Ridiculous.CoolModules.CoolCode
```


### Protip: never treat the directory `src/` as a module!

Students getting started with modules sometimes find themselves in a situation where their `import` statements must include the `src/` directory as a module to clear up errors or IDE warnings.  If you find yourself needing to write import statements like this, stop and get help:

```python
import src.Concatenate
import src.Partial
```

If your main program (the driver) is itself in the directory `src/`, you should not need to include `src` as though it is a module or package.  Never add `src` to your import statements to make your IDE's red squiggles go away.  The problem is that, while this might make your IDE happy, your program will not work on somebody else's computer.  Adding `src` to the module's name is just hacking around a misconfigured IDE.

This can be quite confusing at first, especially when you just want to get your program to run.  If you can't figure out how to fix this yourself, please visit a TA or tutor for assistance.


## Namespaces

When a module is imported, all global identifiers (i.e. names of variables and functions which are not contained within functions) defined therein become accessible in your program.  To access them you first write the name of the module used in the import statement followed by another `.`, followed by the identifier.

As an example, suppose that the file `CoolModules/CoolCode.py` defines a function named `srslyCool()` and a variable named `TEMPERATURE`.  You may use them in your program like so:

```python
import CoolModules.CoolCode


CoolModules.CoolCode.srslyCool()

print("The temperature was")
print(CoolModules.CoolCode.TEMPERATURE)
CoolModules.CoolCode.TEMPERATURE += 1
print("Now the temperature is")
print(CoolModules.CoolCode.TEMPERATURE)
```

In this context, the part of the identifier which names the module is known as a **namespace**.

#### Namespace
A mapping from names to objects

Namespaces are *identifiers* that may contain *other* identifiers.  This means that

*   The name of a namespace *must* follow the rules of identifiers
    *   The name of any *file* that you want to import must adhere to this rule, too!
*   Namespaces contain variables, functions, and *other namespaces*.

[9.2 Python Scopes and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)


Namespaces protect the identifiers you create from being overridden by the same identifiers defined in other modules, and vice versa.  Think of a namespace as an identifier's surname.  In this class there are four students named "Isaac" and four students named "Josh".  How can I refer to a particular "Isaac" or "Josh" if I only used their first names?

Similarly, many Python modules define a variable named `VERSION` which helps you judge whether the module is out of date.  Without putting each of these versions of the identifier `VERSION` within a namespace you'd only be able to access one version of `VERSION`.  Furthermore, you could never be quite sure which version of `VERSION` you were inspecting.

Every line of code you write exists within a namespace.  The "default" namespace is named `__main__`.  Read the section titled [Can a Python file tell when it is being used as a program or a module?](#can-a-python-file-tell-when-it-is-being-used-as-a-program-or-a-module) for more details.


### Warning: modules are *not* classes

Modules and namespaces have a similar appearance to classes and objects, but they are *not* the same things.

*   Modules and objects both use a dot `.` to access items contained therein
*   Just because they share this syntax does not make them equal
*   Namespaces can contain classes and objects, but they *aren't* classes or objects themselves


### Import identifiers into the current namespace with `from`

You may import identifiers from a module directly into the current namespace by writing an import statement in this form:

```python
from MODULE import IDENTIFIER_0, IDENTIFIER_1 ...
```

For example:

```python
from CoolModules.CoolCode import srslyCool, TEMPERATURE
```

From this point on in the file, the function `CoolModules.CoolCode.srslyCool()` may be referred to simply as `srslyCool()`, and the variable `CoolModules.CoolCode.TEMPERATURE` can be accessed just as `TEMPERATURE`.

If you want to import a long list of identifiers from a module, instead of awkwardly listing them all out you can import `*`:

```python
from CoolModules.CoolCode import *
```

The risk of doing this, of course, is that you might import an identifier from one module which overrides an identifier defined in another.  



### Whoops, I clobbered one of Python's built-in functions

You can (accidentally or otherwise) assign a new value to an identifier which is pre-defined by Python.  Python won't warn you about this at the time that you assign the value; this is treated just like an ordinary assignment.

This program is broken because it replaces the built-in functions `len` and `sum` with int values:

```python
ints = [ -2, -27, 30, -70, -49, 22, -99, -5, 41, -82, 67 ]
floats = [ 52.17, -42.57, 98.48, -74.90, 69.77, 28.99, -80.32, 75.70 ]

# Whoopsie!  I just replaced the function len() with an int value!
len = len(ints)
print(f"There are {len} ints and {len(floats)} floats")


# Whoopsie!  I just replaced the function sum() with an int value!
sum = 0

for n in ints:
    sum += n

print(f"According to my for loop, the sum of ints is {sum}")
print(f"According to the built-in sum(), the sum of floats is {sum(floats)}")
```

Fortunately, Python comes with a safety net: the `builtins` module.  The broken program can be "fixed" like so:

```python
import builtins

ints = [ -2, -27, 30, -70, -49, 22, -99, -5, 41, -82, 67 ]
floats = [ 52.17, -42.57, 98.48, -74.90, 69.77, 28.99, -80.32, 75.70 ]

# Whoopsie!  I just replaced the function len() with an int value!
len = len(ints)
print(f"There are {len} ints and {builtins.len(floats)} floats")


# Whoopsie!  I just replaced the function sum() with an int value!
sum = 0

for n in ints:
    sum += n

print(f"According to my for loop, the sum of ints is {sum}")
print(f"According to the built-in sum(), the sum of floats is {builtins.sum(floats)}")
```


You could use `builtins` to "repair" an overridden identifier:

```python
import builtins

str = "hello world"
print = True

if print:
    string = str

    str = builtins.str      # These lines are total hacks,
    print = builtins.print  # and I feel ashamed to write them

    print(string + " " + str(1337) + "!!!")
```


Of course, perhaps the best use of the `builtins` module is to see the list of identifiers that you should *never* use.  At the REPL run this simple loop:

```python
>>> import builtins
>>> for id in dir(builtins):
...     print(id)
... 
ArithmeticError
AssertionError
AttributeError
...
sum
super
tuple
type
vars
zip
```


Only a masochist would do something as self-defeating as this:

```python
import builtins

sum = "I am determined to crash"
builtins.sum = "I am seriously determined to crash"
```


## What file was this module defined in?

*Most* modules correspond to files on your computer (two exceptions are `sys` and `builtins`).  When Python imports a module from a file, it records the location of that file in a special dunder called `__file__` on the module itself.  This lets you find the code that defines the module:

```python
>>> import os
>>> os.__file__
'/usr/lib64/python3.9/os.py'

>>> import turtle
>>> turtle.__file__
'/usr/lib64/python3.9/turtle.py'
```


## When is the code in a module executed?

The code in the module is run at the **moment it is imported**.  This means that any code which is **not** contained inside of a function will be executed at that time.  You can test this out by writing this code in a file called `Running.py`:

```python
print("You have loaded the module named 'Running'")

def run():
    print("You have called 'Running.run()'")
```

Then, import the `Running.py` module in the REPL.  Notice that the **"loaded"** message is printed immediately, before the REPL prompt returns.

```python
$ python
Python 3.9.9 (main, Nov 20 2021, 19:41:34) 
[GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import Running
You have loaded the module named 'Running'

>>> Running.run()
You have called 'Running.run()'
```

*   You should consider whether any code must run at the time a module is imported.
    *   Code which *should not* run at the time of import should be placed in functions so that the user of the module can choose when to run it.
*   The `this` module is a part of the Python standard library that executes its code the moment it is imported.
    *   Import it and use `this.__file__` to find its code.  It's a fun read!



## Can a Python file tell when it is being used as a program or a module?

You may have seen this construct in Python examples you've read online:

```python
if __name__ == '__main__':
    pass
```

The special variable `__name__` is defined for every Python program and module.

*   When a Python script is being run as a program `__name__` contains the string `'__main__'`
*   When a Python script is imported as a module, `__name__` contains the name the module was imported as

We might, then, rewrite `Running.py` such that it does not hard-code its own name:

```python
print("You have loaded the module named '" + __name__ + "'")

def run():
    print("You have called '" + __name__ + ".run()'")
```

Then, import it into the REPL and notice what is printed.  Now, rename the file, import it under its new name and see the difference.

Just as it is sometimes useful for a program to learn its own name by inspecting `sys.argv[0]`, a Python script can look at the value of `__name__` to determine how to behave.

Real-world Python modules may use this feature to run a self-test when called from the command line as a stand-alone program.  Or, a Python file may place its main code inside an `if __name__ == '__main__'` block to simultaneously be a stand-alone program and a module which is used by other stand-alone programs.


## System-Defined Names (how to stay off of Guido's lawn)

`__name__` is an example of a *system-defined name*.  Ordinary programmers are discouraged from creating identifiers beginning and ending with double underscores (the so-called **dunders**) because these identifiers are reserved for the use by the creators of Python (i.e., the aforementioned Guido van Rossum).  New system-defined names can be created and existing ones can be removed from the language at any time.

While the identifier `__cool__` may be unused today, there is nothing preventing Python 3.13 from taking it up.  If that happens your program may cease working as expected when upgrading from Python 3.12 to 3.13.

[Reserved classes of identifiers](https://docs.python.org/3/reference/lexical_analysis.html#reserved-classes-of-identifiers)
