from tkinter import *
from tkinter import messagebox


root = Tk()
lableText = StringVar()
my_label = Label(root, textvariable=lableText)


def print_new_line():
    print("=================")


def changeToRed():
    lableText.set("Red")
    my_label.config(bg="red")


def changeToGreen():
    lableText.set("Green")
    my_label.config(bg="green")


def changeToBlue():
    lableText.set("Blue")
    my_label.config(bg="blue")


def example1():
    lableText.set("Label")
    root.geometry("100x100")

    my_label.pack()

    var = StringVar()
    var.set("Red")
    my_button1 = Button(root, textvariable=var, command=changeToRed)
    my_button1.pack()

    var = StringVar()
    var.set("Green")
    my_button2 = Button(root, textvariable=var, command=changeToGreen)
    my_button2.pack()

    var = StringVar()
    var.set("Blue")
    my_button3 = Button(root, textvariable=var, command=changeToBlue)
    my_button3.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

