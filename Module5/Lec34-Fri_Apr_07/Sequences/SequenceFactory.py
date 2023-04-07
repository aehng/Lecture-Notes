from Fib import Fib
from Pell import Pell
from FizzBuzz import FizzBuzz
from FogBag import FogBag
from NonSquare import NonSquare


def make_sequence(args):
    if len(args) >= 3:
        if args[0].lower() == 'fib':
            seq = Fib(start=int(args[1]), end=int(args[2]))
        elif args[0].lower() == 'fizzbuzz':
            seq = FizzBuzz(start=int(args[1]), end=int(args[2]))
        elif args[0].lower() == 'fogbag':
            seq = FogBag(start=int(args[1]), end=int(args[2]))
        elif args[0].lower() == 'pell':
            seq = Pell(start=int(args[1]), end=int(args[2]))
        elif args[0].lower() == 'nonsquare':
            seq = NonSquare(start=int(args[1]), end=int(args[2]))
        else:
            usage()
            sys.exit(1)

    elif len(args) == 2:
        if args[0].lower() == 'fib':
            seq = Fib(end=int(args[1]))
        elif args[0].lower() == 'fizzbuzz':
            seq = FizzBuzz(end=int(args[1]))
        elif args[0].lower() == 'fogbag':
            seq = FogBag(end=int(args[1]))
        elif args[0].lower() == 'pell':
            seq = Pell(end=int(args[1]))
        elif args[0].lower() == 'nonsquare':
            seq = NonSquare(end=int(args[1]))
        else:
            usage()
            sys.exit(1)

    elif len(args) == 1:
        if args[0].lower() == 'fib':
            seq = Fib()
        elif args[0].lower() == 'fizzbuzz':
            seq = FizzBuzz()
        elif args[0].lower() == 'fogbag':
            seq = FogBag()
        elif args[0].lower() == 'pell':
            seq = Pell()
        elif args[0].lower() == 'nonsquare':
            seq = NonSquare()
        else:
            usage()
            sys.exit(1)
    else:
        seq = Fib()

    return seq
