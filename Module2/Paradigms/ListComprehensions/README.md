# Declarative Programming w/ list comprehensions

*   [Declarative.py](./Declarative.py)
    FizzBuzz sequence in a declarative style relying on Python's `*` operator
    being overloaded for `str` and `int` types.
*   [Idiomatic.py](./Idiomatic.py)
    Using `if` and `else` within a Python list comprehension; this style is
    inspired by set notation from mathematics.


List comprehensions in Python were borrowed from the Haskell language:
https://www.haskell.org/onlinereport/haskell2010/haskellch3.html#x8-420003.11

They were introduced into Python by
[PEP 202](https://www.python.org/dev/peps/pep-0202/) and became part of the
language as of Python v2.0.

A list comprehension is created by surrounding certain Python expressions in
between the square brackets '[' and ']', much as one would create a list
literal.  The expressions within the brackets result in a sequence of values,
which forms the list.
