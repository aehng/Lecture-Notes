# Starting from a straightforward, iterative function...
def iterativeFactorial(n):
    print(f"At this call n = {n}")
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


def middleman0(n):
    print(f"I'm a lazy middleman, and n = {n}")
    return iterativeFactorial(n)


def middleman1(n):
    print(f"I'm a lazy middleman, and n = {n}")
    if n < 2:
        return 1
    return iterativeFactorial(n)


def middleman2(n):
    print(f"I'm a lazy middleman, and n = {n}")
    if n < 2:
        return 1
    return n * iterativeFactorial(n-1)


def middleman3(n):
    print(f"I'm a lazy middleman, and n = {n}")
    if n < 2:
        return 1
    return n * middleman3(n-1)


# ...Can you derive a simple, recursive function?
def recursiveFactorial(n):
    print(f"At this call n = {n}")
    if n < 2:
        return 1
    else:
        return n * recursiveFactorial(n - 1)
