#!/usr/bin/python3

# This example uses the `*` symbol in a few interesting ways, but these arent
# what make this example "functional".
#
# The first `*` is a "star expression" as described in PEP 448
# https://www.python.org/dev/peps/pep-0448/.  It converts a sequence container
# (such as a list or a tuple) into a series of parameters to a function.
#
# The `print()` function can take any number of parameters.  The star `*` in
# front of the call to the `map()` function "unpacks" the resulting map object
# into a series of parameters which are passed to `print()`
#
# If you remove this star, you will instead see the `__str__()` representation
# of the map object, which looks like "<map object at 0x7f5169943fd0>"

# The 2nd and 3rd `*` are Python's "repeat" operator.  Just as `+` has a
# special meaning when applied to collections like lists or strings, , an
# attempt to "multiply" an integer with a container appends that many copies of
# the container onto itself.
#
# It turns out that Python treats the boolean value True as 1 in this context,
# and False becomes 0.  A string repeated 0 times is the empty string.

print(*
    map(
        lambda n: "Fizz"*(not n%3) + "Buzz"*(not n%5) or n,
        range(1, 101)),
    sep='\n')
