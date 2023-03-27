from math import sqrt


class Pell:
    __PHI = (1.0 + sqrt(2.0))
    __PSI = (1.0 - sqrt(2.0))
    __TWO_SQRT2 = 2.0 * sqrt(2.0)

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
            self.n = round((Pell.__PHI ** self.pos - Pell.__PSI ** self.pos)
                           / Pell.__TWO_SQRT2)
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
