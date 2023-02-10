# =Explain mapping collections in Python=

def clobber():
    # curly braces create an empty dictionary object
    colors = {}

    f = open('favorite_colors.dat')
    for line in f:
        # remove the newline at the end of the string
        line = line.strip()

        # The data is tab-delimited; split it into a pair
        name, favorite = line.split('\t')

        # U
        colors[favorite] = name

    f.close()

    # print our mapping
    for key in colors:
        print(f"{key} is liked by {colors[key]}")

    print(f"there are {len(colors)} pairs in colors")



def no_clobber():
    # curly braces create an empty dictionary object
    colors = {}

    f = open('favorite_colors.dat')
    for line in f:
        # remove the newline at the end of the string
        line = line.strip()

        # The data is tab-delimited; split it into a pair
        name, favorite = line.split('\t')

        if favorite in colors:
            # if a color is already liked, add the 2nd person who likes it
            colors[favorite].append(name)
        else:
            # if a color isn't liked, add a list with one name to the dictionary
            colors[favorite] = [ name ]

    f.close()

    # print our mapping
    for key in colors:
        print(f"{key} is liked by {colors[key]}")

    print(f"there are {len(colors)} pairs in colors")
