def print_new_line():
    print("=================")


def example1():
    num = 0

    while num < 5:
        print(num)
        num = num + 1


def example2():
    num = 0
    name = "Hello"

    while num < 10 and name == "Hello":
        print(num)
        num = num + 1

    print("")

    while num < 20 or name == "Hell":
        print(num)
        num = num + 1


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()
