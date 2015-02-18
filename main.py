"""
author: Stuart Taylor
"""

import xml.etree.ElementTree as ET
import skill as SK
import frames as FR

from tkinter import *
from tkinter import ttk



'''
class test:
	def __init__(self):
		self.row=0
		self.col=1
	def p(self):
		print(self.row, self.col, self.stuff)

x = test(row=2)
x.p()
'''
root = Tk()
root.title('Dn Sim: a Dragon Nest skill simulator. Authored by Stuart Taylor')
root.geometry("600x400")
classRoot = ET.parse('./data/NA/assassin.xml').getroot()
testSkill = FR.SkillButton(root,classRoot[1])
testSkill2 = FR.SkillButton(root,classRoot[2])
testSkill.grid(column=0,row=0)
testSkill2.grid(column=1,row=0)
root.mainloop()
'''
sideframe = ttk.Frame(root, width=200)
sideframe.grid(column=0, row=0)

skillpane = ttk.Frame(root, width=200)
skillpane.grid(column=1, row=0)

descframe = ttk.Frame(root, width=200)
descframe.grid(column=2,row=0)

s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s1.set('one')
s2.set('two')
s3.set('three')


ttk.Label(sideframe, textvariable=s1).grid(column=0, row=0)
ttk.Label(skillpane, textvariable=s2).grid(column=0, row=0)
ttk.Label(descframe, textvariable=s3).grid(column=0, row=0)

root.mainloop()
#'''