from tkinter import *


def print_new_line():
    print("=================")


def example1():

    root = Tk()
    root.geometry("150x100")

    my_label1 = Label(root, text="Lebel 1", bg="red")
    my_label2 = Label(root, text="Lebel 2", bg="green")
    my_label3 = Label(root, text="Lebel 3", bg="pink")
    my_label4 = Label(root, text="Lebel 4", bg="blue")

    my_label1.grid(row=0, column=0)
    my_label2.grid(row=0, column=1)
    my_label3.grid(row=1, column=0)
    my_label4.grid(row=1, column=1)

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

