from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def print_new_line():
    print("=================")


def buttonTapped():
    messagebox.showinfo("Hello Python", "Hello World")


def example1():
    root = Tk()
    root.geometry("150x150")
    
    my_button1 = Button(root, text="tkinter Button", command=buttonTapped)

    my_button2 = ttk.Button(root, text="ttk Button", command=buttonTapped)

    my_button1.pack()
    my_button2.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

