from math import sqrt, floor

from Sequence import Sequence


class NonSquare(Sequence):
    """
    A000037 Numbers that are not squares (or, the nonsquares).
    https://oeis.org/A000037
    """

    def value(self):
        return self.pos + floor(1/2 + sqrt(self.pos))
