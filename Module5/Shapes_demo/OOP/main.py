import circle
import rectangle
import square

# Note, this import is *not* necessary to instantiate a circle, rectangle, or a
#   square. It's used to demo attempting to instante an abstract `Shape` class
import shape

if __name__ == '__main__':
    print("Making a Rectangle")
    shape1 = rectangle.Rectangle("Red", 5, 3)

    print("Making a Square")
    shape2 = square.Square("Blue", 4.5)

    print("Making a Circle")
    shape3 = circle.Circle("Green", 6)

    print(f"The rectangle has a perimeter of {shape1.calculatePerimeter()}.")

    print(f"The square has a perimeter of {shape2.calculatePerimeter()}.")

    print(f"The circle has a perimeter of {shape3.calculatePerimeter()}.")

    print(f"The rectangle has an area of {shape1.calculateArea()}.")

    print(f"The square has an area of {shape2.calculateArea()}.")

    print(f"The circle has an area of {shape3.calculateArea()}.")

    print("Can I make an abstract `Shape` object? Let's see!")
    shape4 = shape.Shape("Black")

    print("If I change the code so I can make the shape, let's try getting it's area and perimeter!")
    print(f"Shape perimeter: {shape4.calculatePerimeter()}")
    print(f"Shape area: {shape4.calculateArea()}")
