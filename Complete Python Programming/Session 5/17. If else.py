def print_new_line():
    print("=================")


def example1():
    x = 20
    y = 30

    print("x is", x, "y is", y)
    if x > y:
        print("x is greater than y")
    else:
        print("x is less than y")

    x = 50
    y = 30

    print("x is", x, "y is", y)
    if x > y:
        print("x is greater than y")
    else:
        print("x is less than y")


def example2():
    x = 20
    y = 30

    print("x is", x, "y is", y)
    if x > y:
        print("x is greater than y")
    elif x < y:
        print("x is less than y")
    else:
        print("x is equal y")

    x = 30
    y = 30

    print("x is", x, "y is", y)
    if x > y:
        print("x is greater than y")
    elif x < y:
        print("x is less than y")
    else:
        print("x is equal y")


def example3():
    name = "Hello"

    if name == "Hello":
        print("Welcome", name)
    else:
        print("Unknown user", name)

    name = "Word"

    if name == "Hello":
        print("Welcome", name)
    else:
        print("Unknown user :       ", name)


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()

    print_new_line()
    example3()
