def print_new_line():
    print("=================")


def example1():
    print(2 + 3)
    # 5

    print(50 - 20)
    # 30

    print(1.2 * 5.8)
    # 6.96

    print(40 / 2)
    # 20.0


def example2():
    twenty = 20
    fifty = 50
    sum = twenty + fifty
    negative = -80

    print("twenty :", twenty)
    # twenty : 20

    print("fifty :", fifty)
    # fifty : 50

    print("sum :", sum)
    # sum : 70

    print("negative :", negative)
    # negative : -80


def example3():
    print("2 ^ 3 :", 2 ** 3)
    # 2 ^ 3 : 8

    print("6 ^ 2 :", 6 ** 2)
    # 6 ^ 2 : 36


def example4():
    number1 = 50
    number2 = 2

    print("number1 + number2 =", number1 + number2)
    # number1 + number2 = 52

    print("number1 - number2 =", number1 - number2)
    # number1 - number2 = 48

    print("number1 * number2 =", number1 * number2)
    # number1 * number2 = 100

    print("number1 / number2 =", number1 / number2)
    # number1 / number2 = 25.0

    print("number1 ** number2 =", number1 ** number2)
    # number1 ** number2 = 2500

    print("number1 // number2 =", number1 // number2)
    # number1 // number2 = 25

    print("50 * number2 + number1 =", 50 * number2 + number1)
    # 50 * number2 * number1 = 150

    print("50 * (number2 + number1) =", 50 * (number2 + number1))
    # 50 * (number2 + number1) = 2600


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()

    print_new_line()
    example3()

    print_new_line()
    example4()
