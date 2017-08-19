from tkinter import *
from tkinter import ttk


root = Tk()

labelUser = ttk.Label(root, text="Username:")
labelUser.pack()
labelPass = ttk.Label(root, text="Password:")
labelPass.pack()


entryUser = ttk.Entry(root, width=30)
entryUser.pack()

entryPass = ttk.Entry(root, width=30)
entryPass.pack()

# entry.delete(0, 1) - delete indexes
# entry.delete(0, END) - will delete all from start
# entry.insert(0, "enter your password')

entryPass.config(show='*')

#entry.state(['disabled'])

logInButton = ttk.Button(root, text='Log In')
logInButton.pack()

checkRemember = ttk.Checkbutton(root, text='Remember user?')
checkRemember.pack()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month)

combobox.pack()

combobox.config(values = ('January', 'February', 'March', 'April', 'May','June'))

year = StringVar()

Spinbox(root, from_ = 1990, to = 2017, textvariable = year).pack()





if __name__ == '__main__':
    mainloop()