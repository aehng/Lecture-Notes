#!/usr/bin/python3

# IRL, this functional code would be written as a one-liner:
print(*map(lambda n: "Fizz"*(not n%3) + "Buzz"*(not n%5) or n, range(1, 101)), sep='\n')
