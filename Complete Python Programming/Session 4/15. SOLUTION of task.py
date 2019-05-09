def print_new_line():
    print("=================")


def example1():
    number = input("Enter Number: ")

    for value in range(1, 11):
        multiply = value * int(number)
        line = str(number) + " x " + str(value) + " = " + str(multiply)
        print(line)


if __name__ == '__main__':
    print_new_line()
    example1()
