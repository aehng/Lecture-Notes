# Demonstration of mutual recursion


def headCount(i, n):
    """A function making a recursive call in head position"""
    if i <= n:
        tailCount(i+1, n)
        print(i)


def tailCount(i, n):
    """A function making a recursive call in tail position"""
    if i <= n:
        print(i)
        headCount(i+1, n)


def mutualRecursion(n):
    """A wrapper function to more easily kick off mutually recursive calls"""
    headCount(1, n)
