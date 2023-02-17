import sys


def cat(args):
    """concatenate files and print on the standard output"""
    for fname in args:
        f = open(fname)
        for line in f:
            print(line, end='')
        f.close()


def startgrep(args):
    """def print lines of files beginning with a pattern"""
    if len(args) < 2:
        print("Usage: startgrep.py PATTERN FILE...")
        sys.exit(1)

    pattern = args[0]
    for fname in args[1:]:
        f = open(fname)
        for line in f:
            if line.startswith(pattern):
                print(line, end='')
        f.close()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        startgrep(sys.argv[1:])
    else:
        print("Usage: startgrep.py PATTERN FILE...")
