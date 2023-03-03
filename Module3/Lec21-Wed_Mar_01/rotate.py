import unittest


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
            return chr(o + n - 26)
        else:
            return chr(o + n)
    elif c.isupper():
        if o + n > ord('Z'):
            return chr(o + n - 26)
        else:
            return chr(o + n)
    else:
        return c


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
    return ''.join(rotated)


class RotateTester(unittest.TestCase):

    def test_rotate_UPPER(self):
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
        for i in range(len(uppercase)):
            r = rotate(uppercase[i], 1)
            # rotating last letter should wrap-around back to 0th
            if i == len(uppercase) - 1:
                self.assertEqual(r, uppercase[0])
            # rotating a letter by 1 turns it into the next letter
            else:
                self.assertEqual(r, uppercase[i+1])

    def test_rotate_lower(self):
        lowercase = "abcdefghijklmnopqrstuvwxyz" 
        for i in range(len(lowercase)):
            r = rotate(lowercase[i], 1)
            # rotating last letter should wrap-around back to 0th
            if i == len(lowercase) - 1:
                self.assertEqual(r, lowercase[0])
            # rotating a letter by 1 turns it into the next letter
            else:
                self.assertEqual(r, lowercase[i+1])

    def test_rotate_punctuation(self):
        punctuation = """ ["]#'^_`&{|}\t"""
        for i in range(len(punctuation)):
            self.assertEqual(punctuation[i], rotate(punctuation[i], 1))

    def test_rotate_digit(self):
        digit = "0123456789"
        for i in range(len(digit)):
            self.assertEqual(digit[i], rotate(digit[i], 1))


    def test_rotateLine(self):
        hello0 =  'Hello, World!'
        self.assertEqual(hello0, rotateLine(hello0, 0))
        self.assertEqual('Ifmmp, Xpsme!', rotateLine(hello0, 1))
        self.assertEqual('Olssv, Dvysk!', rotateLine(hello0, 7))
        self.assertEqual('Uryyb, Jbeyq!', rotateLine(hello0, 13))
        self.assertEqual('Axeeh, Phkew!', rotateLine(hello0, 19))
        self.assertEqual('Gdkkn, Vnqkc!', rotateLine(hello0, 25))


# When this file is run as a program it tests itself.
# According to my own tests, how did I do?
if __name__ == '__main__':
    unittest.main()



# vim: set ft=python:
