def print_new_line():
    print("=================")


class Shape:
    width = 0
    height = 0

    def area(self):
        print("Parent class area")


class Rectangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Overrides
    def area(self):
        print("Area of Rectangle is :", self.height * self.width)


class Triangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # Overrides
    def area(self):
        print("Area of Triangle is :", (self.height * self.width) / 2)


def example1():
    rectangle = Rectangle(10, 20)
    rectangle.area()

    triangle = Triangle(2, 10)
    triangle.area()


if __name__ == '__main__':
    print_new_line()
    example1()

