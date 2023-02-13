import sys


def cut(args):
    """remove sections from each line of files"""
    print("TODO: remove sections from each line of files")


# Test with
#  python Partial.py paste data/names8 data/ages8 data/colors8 data/verbs8
def paste(args):
    """merge lines of files"""
    if len(args) < 1:
        print("Error: paste requires at least one filename")
        sys.exit(1)

    files = []
    for file in args:
        files.append(open(file))

    while True:
        lines = []
        for file in files:
            lines.append(file.readline())

        if any(lines):
            stripped = []
            for line in lines:
                stripped.append(line.rstrip('\n'))
            print(','.join(stripped))
        else:
            break

    for file in files:
        file.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'cut':
            cut(sys.argv[2:])
        elif sys.argv[1] == 'paste':
            paste(sys.argv[2:])
        else:
            print(f"Usage: {sys.argv[0]} cut|paste FILE...")
    else:
        print(f"Usage: {sys.argv[0]} cut|paste FILE...")
