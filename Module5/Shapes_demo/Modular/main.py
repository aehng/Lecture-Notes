import circle
import rectangle
import square

if __name__ == '__main__':
    shape1 = rectangle.Rectangle("red", 5, 3)
    print(f"Made a {rectangle.pretty(shape1)}")

    shape2 = square.Square("blue", 4.5)
    print(f"Made a {square.pretty(shape2)}")

    shape3 = circle.Circle("green", 6)
    print(f"Made a {circle.pretty(shape3)}\n")

    print(f"The {rectangle.pretty(shape1)} has a perimeter of {rectangle.perimeter(shape1)}.")

    print(f"The {square.pretty(shape2)} has a perimeter of {square.perimeter(shape2)}.")

    print(f"The {circle.pretty(shape3)} has a perimeter of {circle.perimeter(shape3)}.\n")

    print(f"The {rectangle.pretty(shape1)} has an area of {rectangle.area(shape1)}.")

    print(f"The {square.pretty(shape2)} has an area of {square.area(shape2)}.")

    print(f"The {circle.pretty(shape3)} has an area of {circle.area(shape3)}.")
