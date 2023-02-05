from Modules.Fizz import fizz
from Modules.Buzz import buzz
import Modules


def main():
    i = 1
    while i <= 100:
        Modules.FIZZ_OR_BUZZ = False
        fizz(i)
        buzz(i)
        if not Modules.FIZZ_OR_BUZZ:
            print(i, end='')
        print()
        i += 1
