import Modules


def fizz(n):
    if n % 3 == 0:
        print('Fizz', end='')
        Modules.FIZZ_OR_BUZZ = True
