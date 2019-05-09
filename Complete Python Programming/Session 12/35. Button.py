from tkinter import *
from tkinter import messagebox


def print_new_line():
    print("=================")


def buttonTapped():
    messagebox.showinfo("Hello Python", "Hello World")


def example1():
    root = Tk()
    root.geometry("100x100")

    var = StringVar()
    var.set("Click")
    
    my_button = Button(root, textvariable=var, command=buttonTapped)
    my_button.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

