from FizzBuzz import FizzBuzz

# Create two distinct objects...
fb_1_to_100 = FizzBuzz(1, 100)
fb_1337_to_2000 = FizzBuzz(1337, 2000)

# ...and run each in turn
fb_1_to_100.run()
fb_1337_to_2000.run()

# What makes this "Object-Oriented" is that the *object* is written
# *first*, followed by the name of the method.
