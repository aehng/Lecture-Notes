import sys

# Convert cat() into a function called sum_csv() which takes `N >= 1` filenames
# as input and displays:
# 0. The per-line sum of the numbers on each line
# 1. The per-file total of all lines in a file
# 2. A grand total across all files named on the command line
#
# And because you are a trusting soul, use eval() to convert strings into numbers


def cat(args):
    '''concatenate files and print on the standard output'''
    for fname in args:
        f = open(fname)
        for line in f:
            print(line, end='')
        f.close()


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} CSV_FILE...")
else:
    cat(sys.argv[1:])
