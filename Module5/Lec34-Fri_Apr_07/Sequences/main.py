import sys

from SequenceFactory import make_sequence

def usage():
    print(f"Usage: {sys.argv[0]} [fib|fizzbuzz|fogbag|pell|nonsquare [[START] END]]")

make_sequence(sys.argv[1:]).run()  # this is the polymorphic line of code
