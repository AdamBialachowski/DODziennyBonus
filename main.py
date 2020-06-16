import function
from tkinter import *
import stringSpacePL


def writeAllAccount():
    accountList.delete(0, END)#czyści liste
    for accoun in range(function.amountOfAccont()):
        # Wczytuje tylko nazwe konta bo w lini zapisana jest nazwa i hasło
        accountList.insert(END, function.readAccount(accoun).split(' ')[0]+"")

def writeAccountToList():
    f = open("account.txt", "a")
    f.write(login.get()+" ")
    f.write(password.get()+"\n")
    f.close()
    writeAllAccount()

###################################################



root = Tk()
root.title(stringSpacePL.dailyBonus)

#textbox = Text(root, width=50, height=10)
accountList = Listbox(root, width=50, height=10)
loginLb = Label(root, text=stringSpacePL.login)
passwordLb = Label(root, text=stringSpacePL.password)
login = Entry(root, width=35, borderwidth=2)
password = Entry(root, width=35, borderwidth=2)
addAccount = Button(root, text=stringSpacePL.add, command=writeAccountToList, width=30, height=2)


writeAllAccount()#on textbox


#textbox.grid(rowspan=10, column=0, padx=20, pady=20)
accountList.grid(rowspan=10, column=0, padx=20, pady=20)
loginLb.grid(row=0, column=1, padx=0, pady=(20, 0))
login.grid(row=0, column=2, padx=0, pady=(20, 0))
passwordLb.grid(row=1, column=1, padx=10, pady=(0, 0))
password.grid(row=1, column=2, padx=0, pady=0)
addAccount.grid(row=2, column=2, padx=10, pady=(0, 10))
root.mainloop()