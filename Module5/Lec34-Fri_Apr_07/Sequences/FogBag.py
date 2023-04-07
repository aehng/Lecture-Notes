from Sequence import Sequence


class FogBag(Sequence):
    """Stream from the interval [start, end); end=None is an inf. stream"""
    __FOG = 5
    __BAG = 7

    def is_fog(self):
        return self.pos % FogBag.__FOG == 0

    def is_bag(self):
        return self.pos % FogBag.__BAG == 0

    def value(self):
        """Return the value of the stream at the current position"""
        if self.start < self.pos \
                and (self.end is None or self.pos < self.end):
            val = ""
            if self.is_fog():
                val = "Fog"
            if self.is_bag():
                val += "Bag"
            if val == "":
                val = self.pos
            self.n = val
        else:
            self.n = None
        return self.n
