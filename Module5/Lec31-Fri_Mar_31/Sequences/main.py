import sys

from Fib import Fib
from Pell import Pell
from FizzBuzz import FizzBuzz
from FogBag import FogBag
from NonSquare import NonSquare


def usage():
    print(f"Usage: {sys.argv[0]} [fib|fizzbuzz|fogbag|pell|nonsquare [[START] END]]")


if len(sys.argv) >= 4:
    if sys.argv[1].lower() == 'fib':
        seq = Fib(start=int(sys.argv[2]), end=int(sys.argv[3]))
    elif sys.argv[1].lower() == 'fizzbuzz':
        seq = FizzBuzz(start=int(sys.argv[2]), end=int(sys.argv[3]))
    elif sys.argv[1].lower() == 'fogbag':
        seq = FogBag(start=int(sys.argv[2]), end=int(sys.argv[3]))
    elif sys.argv[1].lower() == 'pell':
        seq = Pell(start=int(sys.argv[2]), end=int(sys.argv[3]))
    elif sys.argv[1].lower() == 'nonsquare':
        seq = NonSquare(start=int(sys.argv[2]), end=int(sys.argv[3]))
    else:
        usage()
        sys.exit(1)

elif len(sys.argv) == 3:
    if sys.argv[1].lower() == 'fib':
        seq = Fib(end=int(sys.argv[2]))
    elif sys.argv[1].lower() == 'fizzbuzz':
        seq = FizzBuzz(end=int(sys.argv[2]))
    elif sys.argv[1].lower() == 'fogbag':
        seq = FogBag(end=int(sys.argv[2]))
    elif sys.argv[1].lower() == 'pell':
        seq = Pell(end=int(sys.argv[2]))
    elif sys.argv[1].lower() == 'nonsquare':
        seq = NonSquare(end=int(sys.argv[2]))
    else:
        usage()
        sys.exit(1)

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'fib':
        seq = Fib()
    elif sys.argv[1].lower() == 'fizzbuzz':
        seq = FizzBuzz()
    elif sys.argv[1].lower() == 'fogbag':
        seq = FogBag()
    elif sys.argv[1].lower() == 'pell':
        seq = Pell()
    elif sys.argv[1].lower() == 'nonsquare':
        seq = NonSquare()
    else:
        usage()
        sys.exit(1)
else:
    seq = Fib()

seq.run()  # this is the polymorphic line of code
