import Modules


def buzz(n):
    if n % 5 == 0:
        print('Buzz', end='')
        Modules.FIZZ_OR_BUZZ = True
