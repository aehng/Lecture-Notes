# What happens when we change the order of the call to print() and the
# increment operation in this iterative algorithm?
def iCount(i, n):
    """Iteratively count from i to n"""
    while i <= n:
        print(i)
        i += 1


# Head vs. Tail recursion
# Question #0: What happens when we change the order of the print() and the
# recursive call?
#
# Question #1: Where is the base case in this function?
def rCount(i, n):
    """Recursively count from i to n"""
    if i <= n:
        print(i)
        rCount(i+1, n)


def rCountWrapper(n):
    """Wrapper function to make recursive call more user-friendly
    Count from 1 to n"""
    rCount(1, n)


def rFactorial(n):
    """Is this function tail recursive?"""
    if n < 2:
        return 1
    else:
        return n * rFactorial(n-1)


def tailFactorial(n, accum):
    """Tail recursive factorial algorithm: the final expression is a function call.
    Users ought not directly call this function.
    The parameter @accum should be set to 1 on the initial call.
    """
    if n < 2:
        return accum
    else:
        return tailFactorial(n-1, n * accum)


def factorialWrapper(n):
    """User-friendly interface to the tail-recursive factorial"""
    return tailFactorial(n, 1)
