#!/usr/bin/python3

# This example represents a more idiomatic style for list comprehensions.
# IRL it would most likely be scrunched up onto one line.
print(*
    [ "FizzBuzz" if i % 15 == 0
            else "Fizz" if i % 3 == 0
            else "Buzz" if i % 5 == 0
            else i
        for i in range(1, 101) ],
    sep='\n')
