#!/usr/bin/python3

# This example is equivalent to the example in ../Functional/Functional.py
print(* [ "Fizz"*(not i%3) + "Buzz"*(not i%5) or i for i in range(1, 101) ], sep='\n')
