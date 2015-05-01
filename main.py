"""
author: Stuart Taylor
"""
#elwakjfhlakwerhalkwjflakwbfalwrajfe
#lsdjfksldjfskdfjklsdjfklsjdflsdkl
import xml.etree.ElementTree as ET
import skill as SK
import frames as FR

import tkinter as TK
from tkinter import ttk
import os

def skillreset(event):
	controlFrame.skillreset()
'''
	add in an update to ctrl to fix the screen when reset
'''
root = TK.Tk()
root.title('Dn Sim: a Dragon Nest skill simulator.')
#control frame
controlFrame = FR.ControlFrame(root)
controlFrame.grid(column=0,row=0,sticky=TK.N+TK.W+TK.E)
root.bind('<Control-Key-r>',skillreset)

#frame for skill boxes
skillFrame = TK.Frame(root)
skillFrame.grid(column=1,row=0)
controlFrame.skillFrame=skillFrame

#skill description frame
descPane = FR.SkillDescFrame(root,controlFrame)
descPane.grid(column=2,row=0)
controlFrame.dpane=descPane

root.mainloop()
