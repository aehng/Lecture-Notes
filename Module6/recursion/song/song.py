#!/usr/bin/env python3

from __future__ import print_function
import sys
import time


# You might try running this program with greater recursion limits
# The default is to limit recursion to 1000 calls
#
# sys.setrecursionlimit(20000)

class CircularList:
    def __init__(self, l):
        if not len(l):
            raise "CircularList must have at least one element"
        self._data = l

    def __repr__(self):
        return repr(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, i):
        return self._data[i]

    def turn(self):
        first = self._data.pop(0)
        self._data.insert(-1, first)

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]


def usleep(usec):
    time.sleep(usec / 1000000.0)


def iterative(cl):
    while cl:
        print(cl.first(), end='', flush=True)
        usleep(1000)
        cl.turn()


def recursive(cl):
    print(cl.first(), end='', flush=True)
    usleep(1000)
    cl.turn()
    recursive(cl)


lyrics = """This is the song that never ends
It just goes on and on my friends
Some people started singing it, not knowing what it was
And they'll continue singing it forever just because

"""

cl = CircularList(list(lyrics))


print("This is the Python3 version")

if len(sys.argv) == 1:
    print("Singing recursively\n")
    time.sleep(1.5)
    recursive(cl)
else:
    print("Singing iteratively\n")
    time.sleep(1.5)
    iterative(cl)
