from math import sqrt

from Sequence import Sequence

class Pell(Sequence):
    """Stream from the interval [start, end); end=None is an inf. stream"""
    __PHI = (1.0 + sqrt(2.0))
    __PSI = (1.0 - sqrt(2.0))
    __TWO_SQRT2 = 2.0 * sqrt(2.0)

    def value(self):
        """Return the value of the stream at the current position"""
        if self.start < self.pos \
                and (self.end is None or self.pos < self.end):
            self.n = round((Pell.__PHI ** self.pos - Pell.__PSI ** self.pos)
                           / Pell.__TWO_SQRT2)
        else:
            self.n = None
        return self.n
