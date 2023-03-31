from math import sqrt

from Sequence import Sequence


class Fib(Sequence):
    """Stream from the interval [start, end); end=None is an inf. stream"""
    __PHI = (1.0 + sqrt(5.0)) / 2.0
    __PSI = (1.0 - sqrt(5.0)) / 2.0
    __RECIP_SQRT5 = 1.0 / sqrt(5)

    def value(self):
        """Return the value of the stream at the current position"""
        if self.start < self.pos \
                and (self.end is None or self.pos < self.end):
            self.n = int(Fib.__RECIP_SQRT5 * (Fib.__PHI ** self.pos - Fib.__PSI ** self.pos))
        else:
            self.n = None
        return self.n
