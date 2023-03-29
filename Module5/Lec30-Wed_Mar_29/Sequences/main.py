import sys

from Fib import Fib
from Pell import Pell
from FizzBuzz import FizzBuzz
from FogBag import FogBag


def usage():
    print(f"Usage: {sys.argv[0]} [fib|fizzbuzz|fogbag|pell [[START] END]]")


if len(sys.argv) >= 4:
    if sys.argv[1].lower() == 'fib':
        Fib(start=int(sys.argv[2]), end=int(sys.argv[3])).run()
    elif sys.argv[1].lower() == 'fizzbuzz':
        FizzBuzz(start=int(sys.argv[2]), end=int(sys.argv[3])).run()
    elif sys.argv[1].lower() == 'fogbag':
        FogBag(start=int(sys.argv[2]), end=int(sys.argv[3])).run()
    elif sys.argv[1].lower() == 'pell':
        Pell(start=int(sys.argv[2]), end=int(sys.argv[3])).run()
    else:
        usage()
        sys.exit(1)

elif len(sys.argv) == 3:
    if sys.argv[1].lower() == 'fib':
        Fib(end=int(sys.argv[2])).run()
    elif sys.argv[1].lower() == 'fizzbuzz':
        FizzBuzz(end=int(sys.argv[2])).run()
    elif sys.argv[1].lower() == 'fogbag':
        FogBag(end=int(sys.argv[2])).run()
    elif sys.argv[1].lower() == 'pell':
        Pell(end=int(sys.argv[2])).run()
    else:
        usage()
        sys.exit(1)

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'fib':
        Fib().run()
    elif sys.argv[1].lower() == 'fizzbuzz':
        FizzBuzz().run()
    elif sys.argv[1].lower() == 'fogbag':
        FogBag().run()
    elif sys.argv[1].lower() == 'pell':
        Pell().run()
    else:
        usage()
        sys.exit(1)
else:
    Fib().run()
