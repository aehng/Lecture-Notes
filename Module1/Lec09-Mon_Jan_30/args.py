# make the list variable "sys.argv" available to your code
import sys


# A Python program that prints its command line arguments, one to a line
for arg in sys.argv:
    print("\t", arg)



# A Python program that counts its command line arguments
print("This program was called with", len(sys.argv), "argument(s)")



# A Python program that prints each command-line argument, one to a line,
# prefixed with its position in the argument list
for i in range(len(sys.argv)):
    print("\t", i, sys.argv[i])



# A Python program that prints the sum of its numeric arguments without
# crashing.  Non-numeric arguments are ignored.
result = 0
for arg in sys.argv:
    if arg.isdigit():
        result += int(arg)
print("The sum of the arguments is", result)



# A Python program that prints the product of its numeric arguments without
# crashing.  Non-numeric arguments are ignored.
result = 1
for arg in sys.argv:
    if arg.isdigit():
        result *= int(arg)
print("The product of the arguments is", result)


# Make this program print either the sum or the product of its numeric
# arguments without crashing.
# **Program Requirements**
# 
# *   Non-numeric arguments are ignored
# *   Whether the sum or product is printed is controlled by the presence of the flags `-sum` or `-product` in the command line
# *   It is an error if this flag is not present
# *   It is also an error if *both* flags are present
if '-sum' in sys.argv and '-product' in sys.argv:
    print("ERROR: both -sum and -product were asked for!")
elif '-sum' in sys.argv:
    result = 0
    for arg in sys.argv:
        if arg.isdigit():
            result += int(arg)
    print("The sum of the arguments is", result)
elif '-product' in sys.argv:
    result = 1
    for arg in sys.argv:
        if arg.isdigit():
            result *= int(arg)
    print("The product of the arguments is", result)
else:
    print("ERROR: one of -sum or -product must be present in argument list!")
