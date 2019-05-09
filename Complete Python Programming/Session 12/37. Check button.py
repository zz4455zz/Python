from tkinter import *
from tkinter import messagebox


def print_new_line():
    print("=================")


def example1():
    root = Tk()

    root.geometry("300x100")
    my_label = Label(root, text="Which one is your favourite?")
    my_label.pack()

    my_checkbutton1 = Checkbutton(root, text="Milk")
    my_checkbutton1.pack()

    my_checkbutton2 = Checkbutton(root, text="Apple juice")
    my_checkbutton2.pack()

    my_checkbutton3 = Checkbutton(root, text="Mango shake")
    my_checkbutton3.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

