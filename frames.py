import tkinter as TK
import skill as SK
from tkinter import ttk
import snip
import os


class ControlFrame(ttk.Frame):
	'''TODO: add dropdown menu for classes
	'''
	def __init__(self,master):
		TK.Frame.__init__(self,master)
		serverPrompt = TK.Label(self,text='server : ')
		serverPrompt.grid(column=0,row=0,sticky=TK.W+TK.N)
		
		serverList = []
		for x in os.listdir('./data/'):
			if os.path.isdir('./data/' + x):
				serverList.append(x)
		serverVar = TK.StringVar(self)
		serverDropdown = TK.OptionMenu(self,serverVar, *serverList)
		serverDropdown.grid(column=1,row=0,sticky=TK.W+TK.N)
		serverVar.trace('w',self.serverchange)
		
		classList = ['filler']
		classVar = TK.StringVar(self)
		classDropdown = TK.OptionMenu(self,serverVar, *classList)
		classDropdown.grid(column=1,row=1,sticky=TK.W+TK.N)
		
		
	def serverchange():
		dir = './data/' + serverVar.get()
		classList = []
		for x in os.listdir(dir):
			if os.path.isdir(dir + x):
				classList.append(x)
		
		
		

class SkillDescFrame(ttk.Label):
	def __init__(self,master):
		TK.Label.__init__(self,master,text="filler",width=40,
							justify=TK.LEFT,wraplength=275,
							anchor=TK.NW)
		self.grid(column=1,row=0,sticky=TK.W+TK.N,pady=10)
	def touch(self,skill):
		self['text']=skill.getDesc()
		
		
class SkillButtonFrame(ttk.Frame):
	#will be used to hold the skill buttons 
	def __init__(self,master,xmlroot,dpane):
		TK.Frame.__init__(self,master)
		self.descpane=dpane
		self.skills=snip.twoD(int(xmlroot.attrib['numRows']),int(xmlroot.attrib['numCols']),None)
		for i in xmlroot:
			#print(i.attrib['name'])
			r = int(i.attrib['row'])
			c = int(i.attrib['col'])
			self.skills[r][c]=SkillButton(self,dpane,i)
		for r in range(0,len(self.skills)):
			for c in range(0,len(self.skills[r])):
				if self.skills[r][c] == None:
					self.skills[r][c]=SkillButton(self)
				self.skills[r][c].grid(column=c,row=r,padx=2*5,pady=2*5)
		
		
		
class SkillButton(ttk.Button):
	'''
		TODO: add a parameter or some mechanism to update the skill
		description pane once that has been implemented.
	'''
	def __init__(self, master,dpane,sk=None):
		TK.Button.__init__(self,master,command=None,
							width=8,height=4,wraplength=60,
							background='cyan')
		if sk == None:
			self.skill=None
			self.configure(text=".")
		else:
			self.skill = SK.Skill(sk)
			self.descpane=dpane
			self.update()
			self.bind('<Button-3>',self.rClick)
			self.bind('<Button-1>',self.lClick)
			self.bind('<Enter>',self.update)
	def rClick(self,event):
		self.skill.rankDown()
		self.update()
		#print('right click. rank down',self.skill.name)
	def lClick(self,event):
		self.skill.rankUp()
		self.update()
		#print('left click. rank up',self.skill.name)
	def update(self,event=None):
		self.config(text=self.gettext())
		self.descpane.touch(self.skill)
	def gettext(self):
		return self.skill.name + "\n(" + str(self.skill.numRanks) + '/' + str(self.skill.limit)+")"