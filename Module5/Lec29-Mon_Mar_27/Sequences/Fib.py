from math import sqrt


class Fib:
    __PHI = (1.0 + sqrt(5.0)) / 2.0
    __PSI = (1.0 - sqrt(5.0)) / 2.0
    __RECIP_SQRT5 = 1.0 / sqrt(5)

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
            self.n = int(Fib.__RECIP_SQRT5 * (Fib.__PHI ** self.pos - Fib.__PSI ** self.pos))
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
