"""
author: Stuart Taylor
"""

import xml.etree.ElementTree as ET
import skill as SK
import frames as FR

import tkinter as TK
from tkinter import ttk
import os

root = TK.Tk()
root.title('Dn Sim: a Dragon Nest skill simulator.')

#skill description frame
descPane = FR.SkillDescFrame(root)
descPane.grid(column=2,row=0)

#data stuffs
baseData = ET.parse('./data/NA/assassin.xml').getroot()
classFrames = []
classFrames.append(FR.SkillButtonFrame(root,baseData,descPane))
classFrames[0].grid(column=1,row=0)

#control frame
controlFrame = FR.ControlFrame(root)
controlFrame.grid(column=0,row=0)

root.mainloop()