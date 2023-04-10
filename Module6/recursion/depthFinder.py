import sys

# Use sys.setrecursionlimit() to control how far Python will go.
# By default its limit is around 1000

# sys.setrecursionlimit(2000)


def depthfinder(n):
    if n > 0:
        depthfinder(n - 1)


if len(sys.argv) > 2:
    sys.setrecursionlimit(int(sys.argv[2]))
    depthfinder(int(sys.argv[1]))
    print("Didn't crash!  w00t!!!")
elif len(sys.argv) > 1:
    depthfinder(int(sys.argv[1]))
    print("Didn't crash!  w00t!!!")
else:
    print("Usage: depthFinder.py DEPTH [RECURSIONLIMIT]")
