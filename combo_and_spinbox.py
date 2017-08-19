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

progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length = 200)
progressbar.pack()
progressbar.config(mode = 'indeterminate')
progressbar.start()

progressbar2 = ttk.Progressbar(root, orient=HORIZONTAL, length = 200)
progressbar2.config(mode='determinate')
progressbar2.start()
progressbar2.pack()

progressbar3 = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar3.config(value=8.0)
progressbar3.step(5)
progressbar3.config(mode='determinate', maximum = 11.0, value = 4.2)

progressbar3.pack()

value = DoubleVar()

progressbar3.config(variable = value)

scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=value, from_ = 0.0, to = 11)
scale.pack()



if __name__ == '__main__':
    mainloop()