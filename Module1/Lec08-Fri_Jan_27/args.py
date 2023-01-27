# make the list variable "sys.argv" available to your code
import sys


print(f'My arguments are {sys.argv}')


# A Python program that prints its command line arguments, one to a line
for arg in sys.argv:
    print(arg)


# A Python program that counts its command line arguments
print(f"There were {len(sys.argv)} arguments passed to this program")


# A Python program that prints each command-line argument, one to a line,
# prefixed with its position in the argument list


# A Python program that prints the sum of its numeric arguments without
# crashing.  Non-numeric arguments are ignored.


# A Python program that prints the product of its numeric arguments without
# crashing.  Non-numeric arguments are ignored.


## Your challenge:
# Make this program print either the sum or the product of its numeric
# arguments without crashing.
# **Program Requirements**
# 
# *   Non-numeric arguments are ignored
# *   Whether the sum or product is printed is controlled by the presence of the flags `-sum` or `-product` in the command line
# *   It is an error if this flag is not present
# *   It is also an error if *both* flags are present
