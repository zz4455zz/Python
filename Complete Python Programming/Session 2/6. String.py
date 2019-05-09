def print_new_line():
    print("=================")


def example1():
    print("Hi my name is HELLO WORD")
    # Hi my name is HELLO WORD

    print('Hi my name is HELLO WORD')
    # Hi my name is HELLO WORD


def example2():
    name = "HELLO WORD"

    print("Hi my name is", name)
    # Hi my name is HELLO WORD

    print("Hi my name is", name[0: 8])
    # Hi my name is HELLO WO

    print("Hi my name is", name[1: 8])
    # Hi my name is ELLO WO


def example3():
    long_string = "this is a long string and can be of any length"
    short_string = "a"

    print(long_string)
    # this is a long string and can be of any length

    print(short_string)
    # a


def example4():
    string1 = "HELLO"
    string2 = "WORD"

    new_string = string1 + string2
    print(new_string)
    # HELLOWORD

    new_string = string1 + " " + string2
    print(new_string)
    # HELLO WORD

    new_string = string1 * 2
    print(new_string)
    # HELLOHELLO


def example5():
    name = "Hello Word!"
    # string : Hello Word!
    # index  : 012345678910

    print(name)
    # Hello Word!

    print(name[4])
    # o

    print(name[4: 7])
    # o W

    print(name[4:])
    # o Word!

    print(name[-3:])
    # rd!

    print(name[-3:-2])
    # r


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()

    print_new_line()
    example3()

    print_new_line()
    example4()

    print_new_line()
    example5()
