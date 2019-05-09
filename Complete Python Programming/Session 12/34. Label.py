from tkinter import *


def print_new_line():
    print("=================")


def example1():
    root = Tk()
    root.geometry("100x100")

    var = StringVar()
    var.set("Hey!? How are you doing?")

    my_label = Label(root, textvariable=var, relief=RAISED)
    my_label.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

