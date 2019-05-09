from tkinter import *


root = Tk()
labelStr = StringVar()
my_label1 = Label(root, text="Which one is your favourite?")
my_label2 = Label(root, textvariable=labelStr)
my_entry1 = Entry(root)
my_entry2 = Entry(root, bg="black", fg="white")


def print_new_line():
    print("=================")


def clearEntry():
    my_entry1.delete(0, END)


def saveToLabel():
    labelStr.set(my_entry1.get())
    labelStr.set(my_entry1.get())


def example1():

    root.geometry("300x150")

    labelStr.set("------")

    my_label1.pack()
    my_label2.pack()
    my_entry1.insert(END, "Default text")
    my_entry1.pack()
    my_entry2.pack()

    my_button1 = Button(root, text="Clear entry1 text", command=clearEntry)
    my_button2 = Button(root, text="Save text to label2", command=saveToLabel)
    my_button1.pack()
    my_button2.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

