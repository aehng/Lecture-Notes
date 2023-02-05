# Smart Caesar Cipher

[This program](caesar.py) demonstrates the differences in performance between
file I/O, lists, tuples and sets.  

This program decrypts files using the Caesar Cipher, which is a simple
substitution file.

Under the Caesar Cipher, a ciphertext is created by "rotating" letters in the
plaintext by a fixed amount.  A rotation of 1 results in `A` -> `B`, `B` ->
`C`, and so on.  At the end of the alphabet, `Z` -> `A`.  As there are 26
letters in the alphabet, there are 25 possible rotations (rotating by 26 is the
same as not rotating at all).

When the wrong rotation is applied to the ciphertext the output is still
scrambled.  To decrypt a Caesar enciphered document one must either know which
rotation was used to create it, or try all 25 possibilities.

This program uses brute force and tries all 25 possible rotations.  To protect
your eyes from pages of garbage, the output is carefully screened by looking
for decoded words in an English language dictionary.  When enough decrypted
words appear to be English, the decryption is considered successful and the
plaintext is displayed.

In Python an item can be sought in a collection using the `in` keyword.  An
`in` expression returns `True` or `False`:

```
if item in collection:
    ...
```

The word list can be one of four collections:

0.  A file
1.  A list
2.  A tuple
3.  A set/dictionary

Which kind of collection is used impacts the performance of our program.

*   By simply changing the file-based lookup to a Python list we see a massive
    improvement in speed - at least two orders of magnitude.

*   By exchanging the list for a set another two-orders-of-magnitude speedup is
    achieved.


## Usage

```
$ python src/caesar.py CIPHERTEXT -file|-list|-tuple|-set
```

This program must be run from within the `smart_caesar` directory as the path
to the word list is hard-coded.

The program expects as command-line arguments the name of an encrypted file
along with one of the flags `-file`, `-list`, `-tuple`, `-set`.  For example:

```
$ python src/caesar.py data/Ydefnomv.oso -file
```



## Notes

The performance differences between file I/O, lists and sets are most striking
when run with a large ciphertext, such as `data/ovt.gkg`.  This takes my
computer ~158 seconds to complete.

Sets, in any case, run in less than 1/10th of a second on my computer.


### Colophon

The words dictionary used is the *5d+2a* dictionary supplied by Alan Beale's
"12dicts Word Lists" project, version 6.0.2.

http://wyrdplay.org/12dicts.html
