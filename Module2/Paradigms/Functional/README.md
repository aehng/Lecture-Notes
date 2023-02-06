# Functional Programming with Lambdas

*   [LambdaFunctional.py](./LambdaFunctional.py)
    *   FizzBuzz sequence using a `lambda` expression, with explanatory commends and formatted for ease of reading
*   [LambdaOneLine.py](./LambdaOneLine.py)
    *   The same program as above, but all in one line of code

Functional programming may be considered a subset of the declarative paradigm.

In this paradigm large programs are built from many small, simple functions which may be created and modified at *runtime*, and may be the input or output of other functions.  Functional programming languages are characterized by the notion of functions being "first-class objects", meaning that functions are values that may be stored in variables, just like numbers, strings, and booleans.

Functional programs emphasize *action* over *state*, meaning that collections of global data are discouraged or impossible.  *Purely* functional languages do not have the notion of assignment as all side-effecting can be defined in terms of functions that encapsulate the changed data.

Functional programs perform their computations with *expressions* rather than *statements*.  Expressions are phrases of code which return a value, such as `2 * 4 + 1` (which results in an integer value) or `fips.isnumeric() and not fips.endswith("000")` (which results in a boolean value).

Statements, by contrast, do not return a value.  In an imperative language a
`for` loop does not result in a value that could be passed to a function.  You
cannot assign the result of an `if/elif/else` tree to a variable.

These examples don't really work in Python because the constructs `if` and
`for` are statements which do not yield values.

```python
# Print a different message based upon the magnitude of `x`
msg = if x > 100:
          "x is a BIG dawg"
      elif x > 50:
          "x is a medium number"
      else:
          "x is just a teeny-weeny little guy"
print(msg)

# print squares of the integers 0-99
print( for i in range(100): i*i )
```


However, the equivalent expressions in a functional language are not only possible, but downright commonplace.  This is the functional Python way to print the result of the above `for` loop using Python's `map()` function with a lambda function created on-the-fly:

```python
print(* map(lambda i: i*i, range(100)) )
```


Examples: LISP, Scheme, Haskell, ML, Prolog, SQL, Make



## FizzBuzz in the Functional style w/ lambda expression

A "lambda expression" is a way to create a "function literal".  Just as you can make a string literal "with quote marks",and a list literal 

    [ "with", "square", "brackets" ]

or a dictionary literal

    { 'using': "curly", 'braces': "like this" } 

you can make a new function value with the `lambda` keyword.  Like any other literal value, you can either store this into a variable or use it in-place.

The example in this directory uses the function literal in-place without storing it into a variable.  Such functions are called "anonymous" since they are never given, nor need a name.  The notion of *not* assigning a name to a function may seem strange to you, but it is a very, very common idiom in functional languages 
