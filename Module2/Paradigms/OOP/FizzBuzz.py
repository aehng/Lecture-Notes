class FizzBuzz:
    def __init__(self, start=0, end=15):
        self.start = start
        self.end = end
        self.n = self.start
        self.fizzbuzzed = False
        self.keepGoing = True

    def isFizz(self):
        if self.n % 3 == 0:
            print('Fizz', end='')
            self.fizzbuzzed = True

    def isBuzz(self):
        if self.n % 5 == 0:
            print('Buzz', end='')
            self.fizzbuzzed = True

    def next(self):
        if self.n < self.end:
            self.n += 1
            self.fizzbuzzed = False
        else:
            self.keepGoing = False

    def run(self):
        #print(f"Fizzbuzzing from {self.start} to {self.end}")
        while self.keepGoing:
            self.isFizz()
            self.isBuzz()
            if not self.fizzbuzzed:
                print(self.n)
            else:
                print()
            self.next()
