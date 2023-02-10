colors = {}
f = open('favorite_colors.dat')
for line in f:
    # Lines are tab-separated and end in a newline
    values = line.rstrip().split('\t')
    # values[0] is the "key" and values[1] is the "value"
    colors[values[0]] = values[1]


letters = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
        'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
        's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
        }

for key in colors:
    first_letter = key[0].lower()
    letters[first_letter] += 1

for key in sorted(letters):
    print(f"Names beginning with {key} occur {letters[key]} times")
