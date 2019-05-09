from tkinter import *


def print_new_line():
    print("=================")


def example1():

    root = Tk()
    root.geometry("150x150")

    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="Open")
    subMenu.add_command(label="Quit")

    root.mainloop()


def openClicked(labelStr):
    labelStr.set("Open")
    print("Open was clicked")


def undoClicked(labelStr):
    labelStr.set("Undo")


def redoClicked(labelStr):
    labelStr.set("Redo")


def quitApplication():
    quit()


def example2():

    root = Tk()
    root.geometry("150x150")

    labelStr = StringVar()
    my_label1 = Label(root, textvariable=labelStr)

    menu = Menu(root)
    root.config(menu=menu)

    subMenu1 = Menu(menu, tearoff=0)
    subMenu1.add_command(label="Open", command=lambda: openClicked(labelStr))
    subMenu1.add_separator()
    subMenu1.add_command(label="Quit", command=quitApplication)

    subMenu2 = Menu(menu, tearoff=0)
    subMenu2.add_command(label="Undo", command=lambda: undoClicked(labelStr))
    subMenu2.add_command(label="Redo", command=lambda: redoClicked(labelStr))

    menu.add_cascade(label="File", menu=subMenu1)
    menu.add_cascade(label="Edit", menu=subMenu2)

    labelStr.set("-----")
    my_label1.pack()

    root.mainloop()


if __name__ == '__main__':
    print_new_line()
    example1()

    print_new_line()
    example2()

