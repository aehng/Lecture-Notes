class Sequence:
    def __init__(self, start=0, end=101):
        if type(self) is Sequence:
            raise NotImplementedError("You cannot create a Sequence object; you must instantiate a concrete subclass")
        else:
            self.start = start
            self.pos = start
            self.end = end
            self.n = None

    def get_pos(self):
        """Return the current position in the stream"""
        return self.pos

    def set_pos(self, new_pos):
        """Set the current position in the stream with error checking"""
        if self.start > new_pos:
            raise IndexError(f"New position {new_pos} can't come before the beginning position of {self.start}")
        elif (self.end is not None and new_pos >= self.end):
            raise IndexError(f"New position {new_pos} can't be >= the ending position of {self.end}")
        else:
            self.pos = new_pos

    def previous(self):
        """Rewind the stream by 1 position"""
        if self.pos >= self.start:
            self.pos -= 1

    def next(self):
        """Advance the stream by 1 position"""
        if self.end is None or self.pos < self.end:
            self.pos += 1

    def beginning(self):
        """Reset the stream to start position"""
        self.pos = self.start

    def run(self):
        """Automatically advance the stream, printing each value
        one line at a time, until the stream is exhausted"""
        while self.end is None or self.pos < self.end:
            self.next()
            n = self.value()
            if n is not None:
                print(n)

    def value(self):
        raise NotImplementedError("You must override the value() method in a sub-class of Sequence")
