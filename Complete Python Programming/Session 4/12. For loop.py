def print_new_line():
    print("=================")


def example1():
    fruits = ["apple", "orange", "mango"]
    for value in fruits:
        print(value)
        # apple, orange, mango


def example2():
    for value in range(1, 5):
        print(value, end=",")
        # 1, 2, 3, 4

    print("")

    for value in range(-2, 3):
        print(value, end=", ")
        # -2, -1, 0, 1, 2

    print("")

    for value in range(-2, 3, 2):
        print(value, end=", ")
        # -2, 0, 2


def example3():
    name = "Hello Word!"
    for value in name:
        print(value, end=", ")
        # H, e, l, l, o,  , W, o, r, d, !


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()

    print_new_line()
    example3()
