FIZZ_OR_BUZZ = False


def fizz(n):
    global FIZZ_OR_BUZZ
    if n % 3 == 0:
        print('Fizz', end='')
        FIZZ_OR_BUZZ = True


def buzz(n):
    global FIZZ_OR_BUZZ
    if n % 5 == 0:
        print('Buzz', end='')
        FIZZ_OR_BUZZ = True


def main():
    global FIZZ_OR_BUZZ
    i = 1
    while i <= 100:
        FIZZ_OR_BUZZ = False
        fizz(i)
        buzz(i)
        if not FIZZ_OR_BUZZ:
            print(i, end='')
        print()
        i = i + 1


main()
