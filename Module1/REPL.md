# The Read, Eval, Print, Loop (REPL)

Perhaps Python's most important feature for the beginning programmer is the REPL.

#### REPL: Read Eval Print Loop

The REPL is an interactive environment where you can play with the language and see for yourself how stuff works.  It is a great way to ![Experiment](./assets/6.experiment.png) **Experiment** with the language and to try out new ideas.

The idea of the REPL was born in the LISP language (as so many good ideas were), and all self-respecting "modern" languages have this feature nowadays.


[Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)


Enter the REPL simply by running `python` with no arguments.

You are in the REPL when you see the `>>>` prompt.

You may also launch the REPL after your script has run by running

    $ python -i scriptname.py


![Don't get Frustrated](./assets/7.dont_get_frustrated.png) **Don't get Frustrated** *Windows users: if running this command causes your Git+Bash terminal to freeze, scroll to the bottom of this document for a workaround.*


Once you're in the REPL you can try things out.

    $ python
    Python 3.7.6 (default, Dec 20 2019, 13:54:57)
    [GCC 9.2.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.

    >>> "yabba dabba" + ' ' + "doo"
    'yabba dabba doo'

    >>> 2 + 7
    9

    >>> 2 * 7
    14

    >>> 2 ** 7
    128


## Two important functions: `help()` and `dir()`

### The `help()` function

![Start with What You Know](./assets/2.start_with_what_you_know.png) **Start with What You Know** Besides being a great base for experimentation, the REPL gives you access to Python's built-in documentation through the `help()` function.


#### `help()` called with no arguments

Calling `help()` in the REPL opens an interactive help system.  The prompt will change from `>>>` to `help>`.  Enter the name of a topic to read about it.  High-level topics include "modules", "keywords", "symbols", and "topics".

Leave the help system by typing `"quit"`.


#### `help()` called with one argument

```
help(OBJ)
```

Displays the built-in documentation for Python object `OBJ`.

`OBJ` may be a number, a string, a function, a class, a module; basically, anything that can be assigned to a variable in Python can be passed to the help function.

When `help()` is passed a non-empty string, that string is interpreted as a topic accessible by the interactive help system as described above.

Other types of values (lists, dictionaries, classes) bring up their own help article.

When `OBJ` is a function its *signature* is displayed along with its help article.  This tells you how many parameters this function accepts, their names and what order they appear.

*   `...` means that many more parameters may be accepted
*   `*` means that an arbitrary number of parameters may be accepted
*   `/` marks the end of *positional* parameters
*   The presence of a 1st parameter called `self` usually indicates this is a method of a class


Remember `help()` any time you have a question about how to use some aspect of the language.

    $ python
    Python 3.7.1 (default, Dec 14 2018, 19:28:38) 
    [GCC 7.3.0] :: Anaconda, Inc. on linux
    Type "help", "copyright", "credits" or "license" for more information.

    >>> help(int)
    # Shows the help for the 'int' class

    >>> help(3 + 7)
    # Idem.

    >>> help(list)
    # Shows the help for 'list' objects, including valid methods that may be
    used on lists.

    >>> help([])
    # Idem.


### The `dir` function

You can see a more compact list of possibilities with the `dir()` function.  This function gives a directory listing of members and methods on an object in Python.  This listing is given as a list of strings, so you can use the ordinary Python list and string operations on it:


    >>> dir(list)
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
    '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__',
    '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__',
    '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count',
    'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


    # Cut the list of methods down to the public ones
	>>> for s in dir(list):
	...     if not s.startswith('__'): print(s)
	... 
	append
	clear
	copy
	count
	extend
	index
	insert
	pop
	remove
	reverse
	sort


## Special instructions for Windows users

Windows users who have installed "Git for Windows" recently should not encounter any trouble with the Python REPL.  Those who installed "Git for Windows" more than a year ago may find that running Python interactively freezes their console.  You can resolve this by re-installing or re-configuring "Git for Windows" on your computer, paying special care to **enable experimental support for pseudo consoles**.


#### If that doesn't fix it...

...you can instead use the command `winpty python` instead of running `python` alone.

For convenience' sake you can create a new Bash command called `repl` which invokes the Python REPL with `winpty` for you.  Edit `~/.bash_profile` in the Nano editor and add this line of code, taking care to copy the white space *exactly* as shown:

    alias repl=`winpty python`

After saving this file close and re-open your Bash console to activate this command.

    $ repl


You can use the `-i` argument described above with this command.

    $ repl -i scriptname.py
