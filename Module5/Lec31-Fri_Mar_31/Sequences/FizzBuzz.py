from Sequence import Sequence


class FizzBuzz(Sequence):
    """Stream from the interval [start, end); end=None is an inf. stream"""
    __FIZZ = 3
    __BUZZ = 5

    def is_fizz(self):
        return self.pos % FizzBuzz.__FIZZ == 0

    def is_buzz(self):
        return self.pos % FizzBuzz.__BUZZ == 0

    def value(self):
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
