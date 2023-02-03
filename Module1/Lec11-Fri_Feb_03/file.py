# Open "README.md" and obtain a file object called 'f':
f = open("README.md")

# Print the file object.  It ain't pretty...
print(f)

# Read the first 10 bytes of the file into a variable called 'tenBytes', and print it
tenBytes = f.read(10)
print(tenBytes)

# Read the next 20 bytes of the file and print them immediately; don't use a variable
print(f.read(20))

# Use an extra blank line to separate the previous output from what comes next
print("\n")

# Print a few lines of text from the file, one at a time
# Make the lines appear right next each other without extra blanks.
for i in range(4):
    line = f.readline()
    print(line, end='')


# Because Python's `print()` function automagically adds a newline at the end,
# and because our lines of text already have their own newline,
# you can suppress `print()`'s extra newline with the `end` parameter.

# Print until the end of the file using a for loop
for gabbagabbagoo in f:
    print(gabbagabbagoo, end='')


# Try to print one more line at the end of the file
print("The end is upon us!")
print("===================")
print(f"after the end of the file, I read a '{f.readline()}'")

# Close the file object
f.close()

# What do you think will happen if you try to **read** from the closed file object?*
print(f"after the file is closed, I read a '{f.readline()}'")

