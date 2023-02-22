# When this file is imported as a module it provides two functions:
#   rotate.rotate(c, n)
#   rotate.rotateLine(line, n)

def rotate(c, n):
    """
    Rotate a single alphabetic character `c` by n positions

    Is this function, as written, easy to test?

    Does it do what we expect it to do?
    """
    o = ord(c)
    if c.islower():
        if o + n > ord('z'):
            return chr(o + n - 25)
    else:
        return chr(o + n)


# The original formulation of this function prints its output instead of returning it.
# This makes it diffucult to analyze its output for correctness
def rotateLine(line, n):
    """
    Rotate all alphabetic chars in a line of text `line` by n positions

    Is this function, as written, easy to test?

    Does it do what we expect it to do?
    """
    rotated = []
    for char in line:
        rotated.append(rotate(char, n))
    print(rotated)


# When this file is run as a program it tests itself.
# According to my own tests, how did I do?
if __name__ == '__main__':
    faults = 0

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    print(f"Testing that rotate(c, 1) works for the letters '{uppercase}'...")
    for i in range(len(uppercase)):
        # rotating last letter should wrap-around back to 0th
        if i == len(uppercase) - 1:
            r = rotate(uppercase[i], 1)
            if r != uppercase[0]:
                faults += 1
                print(f"\tFault #{faults}: expected '{uppercase[0]}' but got '{r}'")
        # rotating a letter by 1 turns it into the next letter
        elif rotate(uppercase[i], 1) != uppercase[i+1]:
            faults += 1
            print(f"\tFault #{faults}: expected '{uppercase[i+1]}' but got '{uppercase[i]}'")


    lowercase = "abcdefghijklmnopqrstuvwxyz"
    print(f"Testing that rotate(c, 1) works for the letters '{lowercase}'...")
    print("TODO: write a test for this...")
    faults += 1


    punctuation = """ ["]#'^_`&{|}\t"""
    print(f"Testing that rotate(c, 1) works for the symbols '{punctuation}'...")
    print("TODO: write a test for this...")
    faults += 1


    digits = "0123456789"
    print(f"Testing that rotate(c, 1) works for the digits '{digits}'...")
    print("TODO: write a test for this...")
    faults += 1


    hello0 =  'Hello, World!'
    print("Testing that rotateLine(l, 0) works correctly...")
    print("TODO: write a test for this...")
    faults += 1


    hello1 =  'Ifmmp, Xpsme!'
    hello7 =  'Olssv, Dvysk!'
    hello13 = 'Uryyb, Jbeyq!'
    hello19 = 'Axeeh, Phkew!'
    hello25 = 'Gdkkn, Vnqkc!'

    if faults > 0:
        print(f"{faults} faults encountered.  I am disappoint :(")


# vim: set ft=python:
