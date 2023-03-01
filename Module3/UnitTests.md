# Writing and Running Unit Tests in Python

There are many code libraries and frameworks used to write unit tests in any
given language.  Deciding which is the "best" can be a contentious religious
issue.  For simplicity's sake we will use Python's standard `unittest` library
in this course.

For more information about the standard `unittest` library please consult the
[unittest official documentation](https://docs.python.org/3/library/unittest.html)


* [Don't Write Trivial Unit Tests](#dont-write-trivial-unit-tests)
* [How to run an individual unit test from the command line](#how-to-run-an-individual-unit-test-from-the-command-line)
* [How to run a test suite from the command line](#how-to-run-a-test-suite-from-the-command-line)
* [How to run all test suites from the command line](#how-to-run-all-test-suites-from-the-command-line)
* [How to run the Bingo! Unit Tests in PyCharm](#how-to-run-the-bingo-unit-tests-in-pycharm)
* [How to run embedded Unit Tests in PyCharm](#how-to-run-embedded-unit-tests-in-pycharm)
* [Unit Test Assertions](#unit-test-assertions)


## Don't Write Trivial Unit Tests

Unit tests are only as useful as the information they can provide about your program.  A unit test that can't possibly fail likely isn't useful.  I don't mean this in the sense of something that should *never* happen in your program, but rather something that is impossible to be false according to mathematical logic.

A tautology is a logical statement constructed in such a way as to be true under every possible interpretation.  In natural language, tautologies are often pointlessly redundant expressions:

*   "An armed gunman"
*   "Died from a mortal wound"
*   "It will either rain tomorrow, or it won't"
*   "The water was wet"


A trivial unit test is just a *tautology* in code.

*   `self.assertTrue(True)`
*   `self.assertGreater(2, 1)`
*   `self.assertIsNot("hello", "world")`
*   `self.assertIn(10, range(100))`


The outcome of such tests cannot possibly be affected by errors in your program.  When these tests pass, they tell you nothing about your program.  A Unit Test is a canary in the coalmine that alerts you to problems.  Don't write unit tests that cannot fail simply to bump up the number of passing tests.


## How to run an individual unit test from the command line

From a command prompt in the `src/` directory run

`$ python -m unittest Testing.testDeck.TestDeck.test_getCard`

| Argument       | Meaning
|----------------|---------------------------------------------------------------------------
| `-m unittest`  | Instruct Python to import the `unittest` module before running any more code
| `Testing`      | The name of the directory containing Unit Test files
| `testDeck`     | A Python source file's name, minus `.py`
| `TestDeck`     | Name of a class within the file `TestDeck.py`
| `test_getCard` | Name of a unit test function within the class `TestDeck`



## How to run a test suite from the command line

A *suite* is a collection of tests.

From a command prompt in the `src/` directory run

`$ python -m unittest Testing.testDeck`



## How to run all test suites from the command line

I wrote a convenience script called `runTests.py`.  If you add new test suites
to your project you should update this program accordingly.  This is how the
graders will run your tests.

From a command prompt in the `src/` directory run

`$ python runTests.py`



## How to run the Bingo! Unit Tests in PyCharm

In the project explorer, right click the 'Testing' folder -> Run Python tests in 'Testing'

Look in PyCharm's debugging pane at the bottom of the window.  It will either list the tests in the projects, or tell you **No tests were found**.

*   If you see the list of unit tests, you're done!
*   If you're unlucky, you'll need to clean up the run configuration that PyCharm created for you.

Depending on your version of PyCharm, there are two ways this can go down:

### Option #0: PyCharm auto-detected Unittests tests

*   Click the run configurations drop down -> **Edit configurations**
*   Find the Unittests configuration that PyCharm created
*   Replace the **Script Path** with 'Testing' (just that one word)
*   Set **working directory** to your project's `src/` folder, and *not* the path ending in `Testing`
*   Ensure the **interpreter** is set to your copy of Python 3
*   All other text boxes should be empty
*   Press OK to save the configuration


### Option #1: PyCharm auto-detected Python tests

*   Click the run configurations drop down -> **Edit configurations**
*   Delete the **Python tests** configuration that PyCharm created for you
*   Press the **+** button in the upper-left corner of the **Run/Debug Configurations** dialog
*   Find **Unittests** in the tree of options
*   Choose **Module name** as the target, and enter 'Testing' (just that one word)
*   Press OK to save the configuration


## How to run embedded Unit Tests in PyCharm

Follow this procedure to run Unit Tests that are embedded in a script (like `rotate.py`):

*   Click the run configurations drop down -> **Edit configurations**
*   Press the **+** button in the upper-left corner of the **Run/Debug Configurations** dialog
*   Find **Unittests** in the tree of options
*   Choose **Module name** as the target, and enter the name of the Python file *without* the `.py` extension
*   Press OK to save the configuration



## Unit Test Assertions

#### Assertion

An *assertion* is a code statement that *may* cause your program to crash.
Usually we fear our program crashing, but crashing on an assertion is regarded
as a *Good Thing*.

In many languages an assertion appears as a function which performs a test that
is expected to pass 100% of the time.  When the test fails it is accepted that
there is no point in the program proceeding.  The most sensible thing to do is
to crash right then and there instead of carrying on in an unexpected state.

The assertion will display a helpful error message that tells the developer
exactly what went wrong and where it happened.  Thus, crashing in the face of a
failed assertion is a useful debugging tool.

Python's `unittest` library offers a variety of convenient assertions that let
you write expressive unit tests.

Here is a summary pulled from the [unittest documentation](https://docs.python.org/3/library/unittest.html?highlight=unittest#test-cases):

| Method                       | Checks that
|------------------------------|-----------------------
| `assertEqual(a, b)`          | `a == b`
| `assertNotEqual(a, b)`       | `a != b`
| `assertTrue(x)`              | `bool(x) is True`
| `assertFalse(x)`             | `bool(x) is False`
| `assertIs(a, b)`             | `a is b`
| `assertIsNot(a, b)`          | `a is not b`
| `assertIsNone(x)`            | `x is None`
| `assertIsNotNone(x)`         | `x is not None`
| `assertIn(a, b)`             | `a in b`
| `assertNotIn(a, b)`          | `a not in b`
| `assertIsInstance(a, b)`     | `isinstance(a, b)`
| `assertNotIsInstance(a, b)`  | `not isinstance(a, b)`
| `assertAlmostEqual(a, b)`    | `round(a-b, 7) == 0`
| `assertNotAlmostEqual(a, b)` | `round(a-b, 7) != 0`
| `assertGreater(a, b)`        | `a > b`
| `assertGreaterEqual(a, b)`   | `a >= b`
| `assertLess(a, b)`           | `a < b`
| `assertLessEqual(a, b)`      | `a <= b`
| `assertRegex(s, r)`          | `r.search(s)`
| `assertNotRegex(s, r)`       | `not r.search(s)`
| `assertCountEqual(a, b)`     | `a` and `b` have the same elements in the same number, regardless of their order.

See the program [Assertions.py](./Assertions.py) to see how many of these
assertions may be used in a working example.


*Updated Tue Feb 28 22:23:41 MST 2023*
