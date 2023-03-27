from math import sqrt
import sys


FIB_PHI = (1.0 + sqrt(5.0)) / 2.0
FIB_PSI = (1.0 - sqrt(5.0)) / 2.0
FIB_RECIP_SQRT5 = 1.0 / sqrt(5)

PELL_PHI = (1.0 + sqrt(2.0))
PELL_PSI = (1.0 - sqrt(2.0))
PELL_TWO_SQRT2 = 2.0 * sqrt(2.0)

FIZZBUZZ_FIZZ = 3
FIZZBUZZ_BUZZ = 5

def usage():
    print(f"Usage: {sys.argv[0]} fib|fizzbuzz|pell [[START] END]")


class Fib:
    """Stream from the interval [start, end); end=None is an inf. stream"""
    def __init__(self, start=0, end=101):
        self.start = start
        self.pos = start
        self.end = end
        self.n = None

    def set_pos(self, new_pos):
        """Set the current position in the stream with error checking"""
        if self.start > new_pos:
            raise IndexError(f"New position {new_pos} can't come before the beginning position of {self.start}")
        elif (self.end is not None and new_pos >= self.end):
            raise IndexError(f"New position {new_pos} can't be >= the ending position of {self.end}")
        else:
            self.pos = new_pos

    def next(self):
        """Advance the stream by 1 position"""
        if self.end is None or self.pos < self.end:
            self.pos += 1

    def get_n(self):
        """Return the value of the stream at the current position"""
        if self.start < self.pos \
                and (self.end is None or self.pos < self.end):
            self.n = int(FIB_RECIP_SQRT5 * (FIB_PHI ** self.pos - FIB_PSI ** self.pos))
        else:
            self.n = None
        return self.n

    def print_sequence(self):
        """Automatically advance the stream, printing each value
        one line at a time, until the stream is exhausted"""
        while self.end is None or self.pos < self.end:
            self.next()
            n = self.get_n()
            if n is not None:
                print(n)


class FizzBuzz:
    """Stream from the interval [start, end); end=None is an inf. stream"""
    def __init__(self, start=0, end=101):
        self.start = start
        self.end = end
        self.pos = start
        self.n = None

    def position(self):
        """Return the current position in the stream"""
        return self.pos

    def advance(self):
        """Advance the stream by 1 position"""
        if self.end is None or self.pos < self.end:
            self.pos += 1

    def previous(self):
        """Rewind the stream by 1 position"""
        if self.pos >= self.start:
            self.pos -= 1

    def rewind(self):
        """Rewind the stream to start position"""
        self.pos = self.start

    def is_fizz(self):
        return self.pos % FIZZBUZZ_FIZZ == 0

    def is_buzz(self):
        return self.pos % FIZZBUZZ_BUZZ == 0

    def fb(self):
        """Return the value of the stream at the current position"""
        if self.start < self.pos \
                and (self.end is None or self.pos < self.end):
            val = ""
            if self.is_fizz():
                val = "Fizz"
            if self.is_buzz():
                val += "Buzz"
            if val == "":
                val = self.pos
            self.n = val
        else:
            self.n = None
        return self.n

    def go(self):
        """Automatically advance the stream, printing each value
        one line at a time, until the stream is exhausted"""
        while self.end is None or self.pos < self.end:
            self.advance()
            n = self.fb()
            if n is not None:
                print(n)


class Pell:
    """Stream from the interval [start, end); end=None is an inf. stream"""
    def __init__(self, start=0, end=101):
        self.start = start
        self.pos = start
        self.end = end
        self.n = None

    def advance(self):
        """Advance the stream by 1 position"""
        if self.end is None or self.pos < self.end:
            self.pos += 1

    def beginning(self):
        """Reset the stream to start position"""
        self.pos = self.start

    def this(self):
        """Return the value of the stream at the current position"""
        if self.start < self.pos \
                and (self.end is None or self.pos < self.end):
            self.n = round((PELL_PHI ** self.pos - PELL_PSI ** self.pos)
                           / PELL_TWO_SQRT2)
        else:
            self.n = None
        return self.n

    def run(self):
        """Automatically advance the stream, printing each value
        one line at a time, until the stream is exhausted"""
        while self.end is None or self.pos < self.end:
            self.advance()
            n = self.this()
            if n is not None:
                print(n)


if len(sys.argv) >= 4:
    if sys.argv[1].lower() == 'fib':
        Fib(start=int(sys.argv[2]), end=int(sys.argv[3])).print_sequence()
    elif sys.argv[1].lower() == 'fizzbuzz':
        FizzBuzz(start=int(sys.argv[2]), end=int(sys.argv[3])).go()
    elif sys.argv[1].lower() == 'pell':
        Pell(start=int(sys.argv[2]), end=int(sys.argv[3])).run()
    else:
        usage()
        sys.exit(1)

elif len(sys.argv) == 3:
    if sys.argv[1].lower() == 'fib':
        Fib(end=int(sys.argv[2])).print_sequence()
    elif sys.argv[1].lower() == 'fizzbuzz':
        FizzBuzz(end=int(sys.argv[2])).go()
    elif sys.argv[1].lower() == 'pell':
        Pell(end=int(sys.argv[2])).run()
    else:
        usage()
        sys.exit(1)

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'fib':
        Fib().print_sequence()
    elif sys.argv[1].lower() == 'fizzbuzz':
        FizzBuzz().go()
    elif sys.argv[1].lower() == 'pell':
        Pell().run()
    else:
        usage()
        sys.exit(1)
else:
    Fib().print_sequence()
