from tkinter import *

'''
counter = 0

def update():
    global counter
    counter = counter + 1
    menu.entryconfig(0, label=str(counter))

root = Tk()

menubar = Menu(root)

menu = Menu(menubar, tearoff=0, postcommand=update)
menu.add_command(label=str(counter))
menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Test", menu=menu)

root.config(menu=menubar)
root.mainloop()
'''
thing = {}
thing['one'] = '#1'
thing['two'] = '#2'
thing['three'] = '#3'

for x in thing:
	print(x)