from tkinter import *


root = Tk()
radioInt = IntVar()
labelStr = StringVar()
my_label1 = Label(root, text="Which is your favourite weather?")
my_label2 = Label(root, textvariable=labelStr, bg="black", fg="white")
my_radio1 = Radiobutton(root, text="Sunny", value=1, variable=radioInt)
my_radio2 = Radiobutton(root, text="Rainy", value=2, variable=radioInt)
my_radio3 = Radiobutton(root, text="Wet", value=3, variable=radioInt)
my_radio4 = Radiobutton(root, text="Dry", value=4, variable=radioInt)
my_radio5 = Radiobutton(root, text="Cloudy", value=5, variable=radioInt)


def print_new_line():
    print("=================")


def showValue():
    labelStr.set(str(radioInt.get()))


def example1():

    root.geometry("300x200")

    radioInt.set(0)
    labelStr.set(str(radioInt.get()))

    my_label1.pack()
    my_label2.pack()

    my_radio1.pack()
    my_radio2.pack()
    my_radio3.pack()
    my_radio4.pack()
    my_radio5.pack()

    my_button1 = Button(root, text="Show radio value", command=showValue)
    my_button1.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

