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


class Student(Person):

    rollNumber = 0
    marks = 100

    def takeClass(self):
        print("Taking class")


def example1():
    student = Student("John", 20, "Male", 170)
    print("Name :", student.getName(), ", Age :", student.getAge())
    student.eat()
    student.takeClass()


if __name__ == '__main__':
    print_new_line()
    example1()

