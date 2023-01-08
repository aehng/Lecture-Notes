def george():
    return "My name is George Harrison, and I sing and play guitar"


def john():
    return "My name is John Lennon, and I sing and play guitar"


def paul():
    return "My name is Paul McCartney, and I sing and play bass"


def ringo():
    return "My name is Ringo Starr, and I'm the drummer.  Nobody likes the drummer :("


# Any code in the module is run as soon as the module is loaded
if __name__ == '__main__':
    print("You are running this as a command-line program")
    print(ringo())
else:
    print(f"You have loaded the module named '{__name__}'")
