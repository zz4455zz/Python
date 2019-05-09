from tkinter import *


root = Tk()
radioInt = IntVar()
my_entry1 = Entry(root)
labelStr1 = StringVar()
labelStr2 = StringVar()
labelStr3 = StringVar()
labelStr4 = StringVar()
labelStr5 = StringVar()
labelStr6 = StringVar()
labelStr7 = StringVar()
labelStr8 = StringVar()
labelStr9 = StringVar()
labelStr10 = StringVar()

my_label1 = Label(root, textvariable=labelStr1, bg="green")
my_label2 = Label(root, textvariable=labelStr2, bg="yellow")
my_label3 = Label(root, textvariable=labelStr3, bg="pink")
my_label4 = Label(root, textvariable=labelStr4, bg="brown")
my_label5 = Label(root, textvariable=labelStr5, bg="blue")
my_label6 = Label(root, textvariable=labelStr6, bg="cyan")
my_label7 = Label(root, textvariable=labelStr7, bg="magenta")
my_label8 = Label(root, textvariable=labelStr8, bg="gray")
my_label9 = Label(root, textvariable=labelStr9, bg="red")
my_label10 = Label(root, textvariable=labelStr10, bg="purple")


def print_new_line():
    print("=================")


def showTable():
    tmpVal = my_entry1.get()
    labelStr1.set(tmpVal + " x 1 =" + str(int(tmpVal) * 1))
    labelStr2.set(tmpVal + " x 2 =" + str(int(tmpVal) * 2))
    labelStr3.set(tmpVal + " x 3 =" + str(int(tmpVal) * 3))
    labelStr4.set(tmpVal + " x 4 =" + str(int(tmpVal) * 4))
    labelStr5.set(tmpVal + " x 5 =" + str(int(tmpVal) * 5))
    labelStr6.set(tmpVal + " x 6 =" + str(int(tmpVal) * 6))
    labelStr7.set(tmpVal + " x 7 =" + str(int(tmpVal) * 7))
    labelStr8.set(tmpVal + " x 8 =" + str(int(tmpVal) * 8))
    labelStr9.set(tmpVal + " x 9 =" + str(int(tmpVal) * 9))
    labelStr10.set(tmpVal + " x 10 =" + str(int(tmpVal) * 10))


def example1():

    root.geometry("300x300")

    labelStr1.set("-----")
    labelStr2.set("-----")
    labelStr3.set("-----")
    labelStr4.set("-----")
    labelStr5.set("-----")
    labelStr6.set("-----")
    labelStr7.set("-----")
    labelStr8.set("-----")
    labelStr9.set("-----")
    labelStr10.set("-----")

    my_entry1.insert(END, "0")
    my_entry1.pack()

    my_button1 = Button(root, text="Show Table", command=showTable)
    my_button1.pack()

    my_label1.pack()
    my_label2.pack()
    my_label3.pack()
    my_label4.pack()
    my_label5.pack()
    my_label6.pack()
    my_label7.pack()
    my_label8.pack()
    my_label9.pack()
    my_label10.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

