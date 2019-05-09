def print_new_line():
    print("=================")


def example1():
    list1 = [1, 2, 3]
    list2 = [1, "abc", 3]
    list3 = [1, "abc", [30, "HelloWord"], 4, 5]

    print(list1)
    # [1, 2, 3]

    print(list2)
    # [1, 'abc', 3]

    print(list3)
    # [1, 'abc', [30, 'HelloWord'], 4, 5]

    print(list3[1])
    # abc
    print(list3[0: 2])
    # [1, 'abc']
    print(list3[2:])
    # [[30, 'HelloWord'], 4, 5]
    print(list3[: 3])
    # [1, 'abc', [30, 'HelloWord']]
    print(list3[2][1])
    # HelloWord
    print(list3[1][1])
    # b


def myKey(elm):
    return len(elm)


def example2():
    fruits = ["apple", "orange"]

    print("fruits :", fruits)
    # fruits : ['apple', 'orange']

    fruits.append("mango")
    print("fruits :", fruits)
    # fruits : ['apple', 'orange', 'mango']

    fruits.append(100)
    print("fruits :", fruits)
    # fruits : ['apple', 'orange', 'mango', 100]

    fruits.extend("banana")
    print("fruits :", fruits)
    # fruits : ['apple', 'orange', 'mango', 100, 'b', 'a', 'n', 'a', 'n', 'a']

    fruits.insert(0, "banana")
    print("fruits :", fruits)
    # fruits : ['banana', 'apple', 'orange', 'mango', 100, 'b', 'a', 'n', 'a', 'n', 'a']

    fruits.insert(0, "banana")
    print("fruits :", fruits)
    # fruits : ['banana', 'banana', 'apple', 'orange', 'mango', 100, 'b', 'a', 'n', 'a', 'n', 'a']
    print('fruits count("banana"):', fruits.count("banana"))
    # fruits count("banana"): 2
    print('fruits index("orange"):', fruits.index("orange"))
    # fruits index("orange"): 3

    fruits.remove("banana")
    fruits.remove(100)
    print("fruits :", fruits)
    # fruits : ['banana', 'apple', 'orange', 'mango', 'b', 'a', 'n', 'a', 'n', 'a']

    fruits.sort(key=myKey)
    print("fruits :", fruits)
    # fruits : ['b', 'a', 'n', 'a', 'n', 'a', 'apple', 'mango', 'banana', 'orange']

    fruits.sort(reverse=True)
    print("fruits :", fruits)
    # fruits : ['orange', 'n', 'n', 'mango', 'banana', 'b', 'apple', 'a', 'a', 'a']

    fruits.sort()
    print("fruits :", fruits)
    # fruits : ['a', 'a', 'a', 'apple', 'b', 'banana', 'mango', 'n', 'n', 'orange']

    fruit = fruits.pop(0)
    print("fruit :", fruit)
    # fruit : a
    print("fruits :", fruits)
    # fruits : ['a', 'a', 'apple', 'b', 'banana', 'mango', 'n', 'n', 'orange']


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()
