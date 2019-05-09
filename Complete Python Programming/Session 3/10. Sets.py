def print_new_line():
    print("=================")


def example1():
    set1 = set("abc")
    print(set1)
    # {'a', 'b', 'c'}

    set2 = set("abcaaa")
    print(set2)
    # {'a', 'b', 'c'}


def example2():
    set1 = set(["apple", "orange", "banana"])
    print(set1)
    # {'apple', 'orange', 'banana '}

    set2 = set(["apple", "orange", "banana", "apple"])
    print(set2)
    # {'apple', 'orange', 'banana '}


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()
