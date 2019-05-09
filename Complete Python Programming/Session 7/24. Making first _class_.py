def print_new_line():
    print("=================")


class Person:

    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def eat(self):
        print("eating")

    def walk(self):
        print("waking")

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


def example1():
    person1 = Person("John", 20, "Male", 170)
    print("Name :", person1.getName(), ", Age :", person1.getAge())
    person1.eat()
    person1.walk()

    person2 = Person("Peter", 25, "Male", 175)
    print("Name :", person2.name, ", Age :", person2.age)
    person2.eat()
    person2.walk()



if __name__ == '__main__':
    print_new_line()
    example1()

