# Starting from a straightforward, iterative function...
def iterativeFactorial(n):
    print(f"At this call n = {n}")
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


# ...Can you derive a simple, recursive function?
def recursiveFactorial(n):
    if n <= 2:
        return n
    else:
        return n * recursiveFactorial(n - 1)
