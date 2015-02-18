import tkinter as tki
import skill as SK
from tkinter import ttk

class SkillButton(ttk.Frame):
	'''
		TODO: add a parameter or some mechanism to update the skill
		description pane once that has been implemented.
	'''
	def __init__(self, master, sk=None):
		tki.Button.__init__(self,master,command=None,width=10,height=5)
		if sk == None:
			self.configure(text=".")
		else:
			self.skill = SK.Skill(sk)
			self.update()
			self.bind('<Button-3>',self.rClick)
			self.bind('<Button-1>',self.lClick)
	def rClick(self,event):
		self.skill.rankDown()
		self.update()
		print('right click. rank down',self.skill.name)
	def lClick(self,event):
		self.skill.rankUp()
		self.update()
		print('left click. rank up',self.skill.name)
	def update(self):
		self.config(text=self.gettext())
	def gettext(self):
		return self.skill.name + "\n(" + str(self.skill.numRanks) + ")"