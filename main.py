"""
author: Stuart Taylor
"""
import config
import xml.etree.ElementTree as ET
import skill as SK
import frames as FR

import tkinter as TK
from tkinter import ttk
import os

def skillreset(event):
	config.resetting=True
	config.control.skillreset()
	config.resetting=False
'''
	add in an update to ctrl to fix the screen when reset
'''
root = TK.Tk()
root.title('Dn Sim: a Dragon Nest skill simulator.')
#control frame
config.control = FR.ControlFrame(root)
config.control.grid(column=0,row=0,sticky=TK.N+TK.W+TK.E)
config.updatelist['control'] = config.control.update
root.bind('<Control-Key-r>',skillreset)

#frame for skill boxes
config.skillpane = TK.Frame(root)
config.skillpane.grid(column=1,row=0)
#config.updatelist['skills']=config.skillpane.update

#skill description frame
config.descpane = FR.SkillDescFrame(root)
config.descpane.grid(column=2,row=0)
config.updatelist['desc']=config.descpane.update

root.mainloop()
