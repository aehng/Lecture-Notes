#!/usr/bin/python3

import sys
import time


def usage():
    print(f"Usage: {sys.argv[0]} FILENAME -file|-list|-tuple|-set\n")
    sys.exit(1)


def main():
    if len(sys.argv) > 2 and sys.argv[2] in ('-file', '-list', '-tuple', '-set'):

        crypted_file = sys.argv[1]
        wc = word_count(crypted_file)

        # Choose a data structure for the wordlist by the user's preference
        if sys.argv[2] == '-file':
            print(f"Checking {wc} words against an English dictionary stored in a FILE")
            wordlist = 'data/words'
        elif sys.argv[2] == '-list':
            print(f"Checking {wc} words against an English dictionary stored in a LIST")
            wordlist = words_to_list('data/words')
        elif sys.argv[2] == '-tuple':
            print(f"Checking {wc} words against an English dictionary stored in a TUPLE")
            wordlist = words_to_tuple('data/words')
        elif sys.argv[2] == '-set':
            print(f"Checking {wc} words against an English dictionary stored in a SET")
            wordlist = words_to_set('data/words')
        else:
            usage()

        # Note the time this program began
        began = time.time()

        # Brute force - attempt each possible rotation
        for rotation in range(26):
            progress(rotation)
            plaintext = caesar_decipher_file(crypted_file, rotation)
            words = plaintext.split()
            num_words = len(words)

            # count the number of legible English words in the deciphered plaintext
            good_words = 0
            for word in words:
                if word_in_collection(word, wordlist):
                    good_words += 1

            # print plaintext when it's mostly legible English (at least 20%)
            if good_words / num_words > .20:
                print("\n\n=====================================================\n"
                        f"Input was rotated by {26 - rotation:2} positions "
                        f"({good_words / num_words:.2%} confidence)\n"
                        "=====================================================\n")
                print(plaintext)

        progress(e="\n")
        finished = time.time()
        print(f"Done in {finished - began:.5f} seconds!")

    else:
        usage()


## Functions that decrypt the Caesar cipher

def rotate_letter(c, n):
    """Rotate a single alphabetic character.
    Non-alphabetic characters are returned unchanged"""
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
        return c;


def caesar_decipher_file(fil, dist):
    """Given a filename, return its contents rotated by distance `dist`"""
    chars = []
    secret = open(fil)
    for line in secret:
        for c in line:
            chars.append(rotate_letter(c, dist))
    secret.close()
    return ''.join(chars)



## Functions that check whether a plaintext word is English

def word_in_collection(word, collection):
    """Unified interface for checking whether a word occurs in a collection"""
    if collection == 'data/words':
        return word_in_file(word, collection)
    else:
        return word in collection


def word_in_file(word, fil):
    """Predicate: is `word` contained in file `fil`?
    Note: `item in TextIOWrapper` matches lines in a textfile; this means that
    `item` must end with the EOL symbol.
    
    Therefore, I must manually append "\n" for this use case
    """
    word += "\n"
    f = open(fil)
    found = word in f
    f.close()
    return found


## Functions that put the wordlist into various data structures

def words_to_list(fil):
    """Given a file containing a list of words, return a list of those words"""
    f = open(fil)
    words = [line.strip() for line in f]
    f.close()
    return words


def words_to_tuple(fil):
    """Given a file containing a list of words, return a tuple of those words"""
    return tuple(words_to_list(fil))


def words_to_set(fil):
    """Given a file containing a list of words, return a set of those words"""
    return set(words_to_list(fil))


## Miscellaneous

def word_count(fil):
    """Return the number of words found in a file"""
    words = 0
    f = open(fil)
    for line in f:
        words += len(line.split())
    f.close()
    return words


def progress(n=26, d=26, e=''):
    print(f"\r{n}/{d} ({n/d:.2%})", end=e)


if __name__ == '__main__':
    main()
