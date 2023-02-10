import sys

# Convert cat() into a function called sum_csv() which takes `N >= 1` filenames
# as input and displays:
# 0. The per-line sum of the numbers on each line
# 1. The per-file total of all lines in a file
# 2. A grand total across all files named on the command line
#
# And because you are a trusting soul, use eval() to convert strings into numbers


def sum(args):
    '''concatenate files and print on the standard output'''
    grand_total = 0
    for fname in args:
        file_total = 0
        f = open(fname)
        for line in f:
            line = line.strip()
            nums = line.split(',')
            line_total = 0
            for num in nums:
                num = eval(num)  # <== HERE BE DRAGONS!
                line_total += num
            print(f"line total = {line_total}")
            file_total += line_total
        f.close()
        grand_total += file_total
        print(f"file total = {file_total}")
    print(f"GRAND TOTAL = {grand_total}")


if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} CSV_FILE...")
else:
    sum(sys.argv[1:])
