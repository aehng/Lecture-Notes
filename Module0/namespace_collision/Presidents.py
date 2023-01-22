def george():
    return "My name is George Washington, and I kinda got this whole thing started"


def john():
    return "My name is John Adams. You probably forgot about me, but I was pretty popular a few years ago thanks to McCullough's biography"


def thomas():
    return "My name is Thomas Jefferson, and lately I've become really controversial"


def james():
    return "My name is James Madison, and I wrote things which you've heard of but probably never read"


# Any code in the module is run as soon as the module is loaded
if __name__ == '__main__':
    print("You are running this as a command-line program")
    print(george())
    print(john())
    print(thomas())
    print(james())
else:
    print("You have loaded the module named", __name__)
