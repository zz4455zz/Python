def print_new_line():
    print("=================")


def example1():
    for obj in range(5):
        print(obj, end=', ')
        # 0, 1, 2, 3, 4

    print("")

    for obj in range(-2, 3):
        print(obj, end=', ')
        # -2, -1, 0, 1, 2

    print("")

    for obj in range(0, 50):
        print(obj, end=', ')
        # 0, 1, 2, 3, ..., 50

    print("")

    for obj in range(0, 10, 2):
        print(obj, end=', ')
        # 0, 2, 4, 6, 8

    print("")


if __name__ == '__main__':
    print_new_line()
    example1()
