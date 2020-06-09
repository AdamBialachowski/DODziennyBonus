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



###############################################################
#Write to textbox
def readAccount(line):
    f = open("account.txt","r")
    accontName = f.readlines()
    f.close()
    return accontName[line]

def amountOfAccont():
    f = open("account.txt")
    amountAccont = len(f.readlines())
    f.close()
    return amountAccont


