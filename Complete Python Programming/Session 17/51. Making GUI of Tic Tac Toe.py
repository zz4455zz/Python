from tkinter import *
from tkinter import ttk


def print_new_line():
    print("=================")


def buttonPressed(buttonNumber):
    temp = buttonNumber


def example1():

    root = Tk()
    root.geometry("560x375")

    button1 = ttk.Button(root, text="", command=lambda: buttonPressed(1))
    button1.grid(row=0, column=0, ipadx=50, ipady=50)
    button2 = ttk.Button(root, text="", command=lambda: buttonPressed(2))
    button2.grid(row=0, column=1, ipadx=50, ipady=50)
    button3 = ttk.Button(root, text="", command=lambda: buttonPressed(3))
    button3.grid(row=0, column=2, ipadx=50, ipady=50)
    button4 = ttk.Button(root, text="", command=lambda: buttonPressed(4))
    button4.grid(row=1, column=0, ipadx=50, ipady=50)
    button5 = ttk.Button(root, text="", command=lambda: buttonPressed(5))
    button5.grid(row=1, column=1, ipadx=50, ipady=50)
    button6 = ttk.Button(root, text="", command=lambda: buttonPressed(6))
    button6.grid(row=1, column=2, ipadx=50, ipady=50)
    button7 = ttk.Button(root, text="", command=lambda: buttonPressed(7))
    button7.grid(row=2, column=0, ipadx=50, ipady=50)
    button8 = ttk.Button(root, text="", command=lambda: buttonPressed(8))
    button8.grid(row=2, column=1, ipadx=50, ipady=50)
    button9 = ttk.Button(root, text="", command=lambda: buttonPressed(9))
    button9.grid(row=2, column=2, ipadx=50, ipady=50)

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()


