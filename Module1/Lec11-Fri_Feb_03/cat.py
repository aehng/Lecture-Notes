def cat(args):
    """
    for each filename in args
        open a file
        for each line in the file
            print(line), but don't add an extra \n
        close the file
    """
    for file in args:
        f = open(file)
        for line in f:
            print(line, end='')
        f.close()


cat(["README.md", "file.py", "cat.py"])