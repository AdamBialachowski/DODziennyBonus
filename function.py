from tkinter import *
import stringSpacePL

def button_add():
    return

def howManyAccounts():
    root = Tk()
    root.title(stringSpacePL.dailyBonus)

    lable = Label(root, text=stringSpacePL.howManyAccount)
    howManyAccounts = Entry(root, width=35, borderwidth=2)
    next = Button(root, text=stringSpacePL.next, padx=20, pady=10, command=button_add())

    lable.grid(row=0, padx=0, pady=20)
    howManyAccounts.grid(row=1, column=0, columnspan=1, padx=10, pady=0)
    next.grid(row=1, column=1, padx=10, pady=10)
    root.mainloop()

def createLayout():
    root = Tk()
    root.title(stringSpacePL.dailyBonus)

    textbox = Text(root, width=50, height=10)
    loginLb = Label(root, text=stringSpacePL.login)
    passwordLb = Label(root, text=stringSpacePL.password)
    login = Entry(root, width=35, borderwidth=2)
    pasword = Entry(root, width=35, borderwidth=2)
    addAccount = Button(root, text=stringSpacePL.add, command=button_add(), width=30, height=2)
    textbox.grid(rowspan=10, column=0, padx=20, pady=20)
    textbox.insert(INSERT, "nazwa konta\n")
    textbox.insert(INSERT, "nazwa konta")

    loginLb.grid(row=0, column=1, padx=0, pady=(20, 0))
    login.grid(row=0, column=2, padx=0, pady=(20, 0))
    passwordLb.grid(row=1, column=1, padx=10, pady=(0, 0))
    pasword.grid(row=1, column=2, padx=0, pady=0)
    addAccount.grid(row=2, column=2, padx=10, pady=(0, 10))
    root.mainloop()