from math import sqrt, floor


class NonSquare:
    """
    A000037 Numbers that are not squares (or, the nonsquares).
    https://oeis.org/A000037
    """
    def __init__(self, start=0, end=101):
        self.start = start
        self.pos = start
        self.end = end
        self.n = None

    def next(self):
        """Advance the stream by 1 position"""
        if self.end is None or self.pos < self.end:
            self.pos += 1

    def value(self):
        return self.pos + floor(1/2 + sqrt(self.pos))

    def run(self):
        """Automatically advance the stream, printing each value
        one line at a time, until the stream is exhausted"""
        while self.end is None or self.pos < self.end:
            self.next()
            n = self.value()
            if n is not None:
                print(n)
