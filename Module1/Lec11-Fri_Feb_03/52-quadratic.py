import math


def firstRoot(a, b, disc):
    return (-b + disc) / (2 * a)     # <======= PLACE A BREAKPOINT HERE


def secondRoot(a, b, disc):
    return (-b - disc) / (2 * a)


def demo(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:                        # <======= PLACE A BREAKPOINT HERE
        disc = math.sqrt(d)
        root1 = firstRoot(a, b, disc)
        root2 = secondRoot(a, b, disc)
        return root1, root2
    elif d == 0:
        return firstRoot(a, b, 0)
    else:
        return "This equation has no roots"


# Our customer complains that this program crashes when a == 0.
# Why is that?

while True:
    a = int(input("Input the value of a: "))
    if a == 0:
        print("The 'a' term cannot be zero, try again")
        continue
    b = int(input("Input the value of b: "))
    c = int(input("Input the value of c: "))
    result = demo(a, b, c)           # <======= PLACE A BREAKPOINT HERE
    print(result)


# Zero roots
#     a = 8   b = 3    c = 10
#
# One root
#     a = 1   b = -10  c = 25
#
# Two roots
#     a = 10  b = 20   c = 4
