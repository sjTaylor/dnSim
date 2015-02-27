import xml.etree.ElementTree as ET

import tkinter as TK
import skill as SK
from tkinter import ttk
import snip
import os


class ControlFrame(ttk.Frame):
	def __init__(self,master):
		TK.Frame.__init__(self,master)
		
		self.serverPrompt = TK.Label(self,text='server : ')
		self.serverPrompt.grid(column=0,row=0,sticky=TK.W+TK.N)
		self.classPrompt = TK.Label(self,text='class : ')
		self.classPrompt.grid(column=0,row=1,sticky=TK.W+TK.N)
		
		self.serverList = []
		for x in os.listdir('./data/'):
			if os.path.isdir('./data/' + x):
				self.serverList.append(x)
		self.serverVar = TK.StringVar(self)
		self.serverDropdown = TK.OptionMenu(self,self.serverVar, *self.serverList)
		self.serverDropdown.grid(column=1,row=0,sticky=TK.E+TK.W)
		self.serverDropdown.configure(width=15)
		self.serverVar.trace('w',self.serverchange)
		
		self.classList = ['filler']
		self.classVar = TK.StringVar(self)
		self.classDropdown = TK.OptionMenu(self,self.classVar, *self.classList)
		self.classDropdown.grid(column=1,row=1,sticky=TK.E+TK.W)
		self.classVar.trace('w',self.classchange)
		
		self.allbutton=TK.Button(self,text='All',command=self.showall)
		self.allbutton.grid(row=2,column=0,sticky='ew',columnspan=2)
		
		self.classonebutton=TK.Button(self,text='class 1',command=self.showc1)
		self.classonebutton.grid(row=2+1,column=0,sticky='ew',columnspan=2)
		
		self.classtwobutton=TK.Button(self,text='class 2',command=self.showc2)
		self.classtwobutton.grid(row=2+2,column=0,sticky='ew',columnspan=2)
		
		self.classthreebutton=TK.Button(self,text='class 3',command=self.showc3)
		self.classthreebutton.grid(row=2+3,column=0,sticky='ew',columnspan=2)
		
		
		self.splabel = TK.Label(self,justify=TK.LEFT)
		self.splabel.grid(row=2+4,column=0,sticky='wn',columnspan=2)
		
		self.pages = []
	def showc1(self,event=None):
		self.showclass(0)
	def showc2(self,event=None):
		self.showclass(1)
	def showc3(self,event=None):
		self.showclass(2)
	def showclass(self,classnum):
		for c in self.pages:
			c.grid_remove()
		if len(self.pages) > classnum:
			self.pages[classnum].grid()
	def showall(self,event=None):
		for c in self.pages:
			c.grid()
		
	def serverchange(self,arg1,arg2,arg3):
		dir = './data/' + self.serverVar.get()
		temp = []
		for x in os.listdir(dir):
			if os.path.isfile(dir +'/'+ x):
				temp.append(x)
		self.classDropdown['menu'].delete(0,'end')
		for s in temp:
			self.classDropdown['menu'].add_command(label=s,command=TK._setit(self.classVar,s))
	def classchange(self,arg1,arg2,arg3):
		self.dpane.switch=False
		while len(self.pages) > 0:
			self.pages[0].grid_remove()
			del self.pages[0]
		self.pages=[]
		self.dir = './data/'+self.serverVar.get()+'/'
		self.pages.insert(0,SkillButtonFrame(self.skillFrame,ET.parse(self.dir+self.classVar.get()).getroot(),self.dpane))
		while self.pages[0].superclass != 'none':
			self.pages.insert(0,SkillButtonFrame(self.skillFrame,ET.parse(self.dir+'superclasses/'+self.pages[0].superclass).getroot(),self.dpane))
		for i in range(0,len(self.pages)):
			self.pages[i].grid(column=i,row=0,sticky='ns')
		self.classonebutton['text']=self.pages[0].classname
		self.classtwobutton['text']=self.pages[1].classname
		self.classthreebutton['text']=self.pages[2].classname
		self.pages[1].configure(bg='#CCFFFF')
		self.pages[2].configure(bg='#ADFF5C')
		self.dpane.switch=True
	def skilltotal(self):
		total = 0
		self.nums = []
		for x in range(0,len(self.pages)):
			temp = self.pages[x].sp()
			total += temp
			self.nums.append(temp)
		text = 'SP Spent : ' + str(total) + '\n'
		text+= self.pages[0].classname + ' : ' + str(self.nums[0]) + '/129\n'
		text+= self.pages[1].classname + ' : ' + str(self.nums[1]) + '/133\n'
		text+= self.pages[2].classname + ' : ' + str(self.nums[2]) + '/129\n'
		text+= 'SP remaining : ' + str(207-total)
		self.splabel['text']=text
	def skillreset(self):
		self.dpane.switch=False
		for i in self.pages:
			i.skillreset()
		self.dpane.switch=True
		self.skilltotal()
			
			
		
class SkillDescFrame(ttk.Label):
	def __init__(self,master,ccframe):
		self.w=35
		TK.Label.__init__(self,master,text="filler",width=self.w,
							justify=TK.LEFT,wraplength=self.w*7,
							anchor=TK.NW,bg='white')
		'''
			todo:
			1. add skill title
			2. add curr, next rank titles
			3. cooldown(when applicable
			4. required level
			5. required skills (when applicable)
		'''
		self.switch=False
		self.cframe=ccframe
		self.grid(column=1,row=0,sticky='nsw')
	def touch(self,skill):
		self['text']=skill.getDesc()
		if self.switch:
			self.cframe.skilltotal()
		
		
class SkillButtonFrame(ttk.Frame):
	#will be used to hold the skill buttons 
	def __init__(self,master,xmlroot,dpane):
		TK.Frame.__init__(self,master,bg='white')
		self.descpane=dpane
		self.skills=snip.twoD(int(xmlroot.attrib['numRows']),int(xmlroot.attrib['numCols']),None)
		for i in xmlroot:
			r = int(i.attrib['row'])
			c = int(i.attrib['col'])
			self.skills[r][c]=SkillButton(self,dpane,i)
		for r in range(0,len(self.skills)):
			for c in range(0,len(self.skills[r])):
				if self.skills[r][c] != None:
					self.skills[r][c].grid(column=c,row=r,padx=1*5,pady=1*5)
		self.superclass=xmlroot.attrib['superclass']
		self.classname=xmlroot.attrib['name']
		self.classLevel=int(xmlroot.attrib['classLevel'])
	def sp(self):
		total = 0
		for x in self.skills:
			for y in x:
				if y != None:
					total += y.sp()
		return total
	def skillreset(self):
		for x in self.skills:
			for y in x:
				if y != None:
					y.minimize()
	
		
class SkillButton(ttk.Button):
	'''
		TODO: add a parameter or some mechanism to update the skill
		description pane once that has been implemented.
	'''
	def __init__(self, master,dpane=None,sk=None):
		TK.Button.__init__(self,master,command=None,
							width=8,height=4,wraplength=60)
		if sk == None:
			self.skill=None
			self.configure(text=".")
		else:
			self.skill = SK.Skill(sk)
			self.descpane=dpane
			self.update()
			self.bind('<Button-3>',self.rClick)
			self.bind('<Button-1>',self.lClick)
			self.bind('<Shift-Button-3>',self.shiftrclick)
			self.bind('<Shift-Button-1>',self.shiftlclick)
			self.bind('<Enter>',self.update) 
	def sp(self):
		if self.skill==None:
			return 0
		return self.skill.sp()
	def minimize(self):
		if self.skill != None:
			self.skill.minimize()
		self.update()
	def shiftrclick(self, event):
		self.skill.minimize()
		self.update()
	def shiftlclick(self, event):
		self.skill.maximize()
		self.update()
	def rClick(self,event):
		self.skill.rankDown()
		self.update()
	def lClick(self,event):
		self.skill.rankUp()
		self.update()
	def update(self,event=None):
		self.config(text=self.gettext())
		self.descpane.touch(self.skill)
	def gettext(self):
		return self.skill.name + "\n" + str(self.skill.numRanks) + '/' + str(self.skill.limit)