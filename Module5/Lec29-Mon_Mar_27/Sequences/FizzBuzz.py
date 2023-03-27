class FizzBuzz:
    __FIZZ = 3
    __BUZZ = 5

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
        return self.pos % FizzBuzz.__FIZZ == 0

    def is_buzz(self):
        return self.pos % FizzBuzz.__BUZZ == 0

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

