import config

import xml.etree.ElementTree as ET

import tkinter as TK
import skill as SK
from tkinter import ttk

import snip
import os

if config.image:
	from PIL import Image, ImageTk

class ControlFrame(ttk.Frame):
	def __init__(self,master):
		TK.Frame.__init__(self,master)
		self.w=35

		self.spendingsp =[0,0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48,51,54,57,60,63,66,69,72,75,78,81,84,87,90,93,96,99,102,105,108,111,114,117,120,123,126,129,132,135,138,141,144,147,149,151,153,155,157,159,161,163,165,167,169,171,173,175,177,179,181,183,185,187,189,191,193,195,197,199,201,203,205,207]
		self.maxsp      =[
			[0,0,3,6,9,12,15,18,21,24,27,30,33,36,39,26,28,30,31,33,35,37,39,41,43,45,46,48,50,52,54,56,58,60,61,63,65,67,69,71,73,75,76,78,80,82,84,86,88,90,91,93,94,95,96,98,99,100,101,103,104,105,106,108,109,110,111,113,114,115,116,118,119,120,121,123,124,125,126,128,129],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,27,29,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,90,92,94,96,97,98,99,101,102,103,105,106,107,109,110,111,112,114,115,116,118,119,120,121,123,124,125,127,128,129,130,132,133],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,82,84,86,88,90,91,93,94,95,96,98,99,100,101,103,104,105,106,108,109,110,111,113,114,115,116,118,119,120,121,123,124,125,126,128,129]]
		self.level=80

		self.levelsetbutton = TK.Button(self,text='set level',command=self.setlevel)
		self.levelsetbutton.grid(column=0,row=0)

		self.levelentry = TK.Entry(self)
		self.levelentry.grid(column=1,row=0)
		self.levelentry.insert(0,'80')

		self.serverPrompt = TK.Label(self,text='server : ')
		self.serverPrompt.grid(column=0,row=0+1,sticky=TK.W+TK.N)
		self.classPrompt  = TK .Label(self,text='class : ')
		self.classPrompt.grid(column=0,row=1+1,sticky=TK.W+TK.N)

		self.serverList = []
		for x in os.listdir('./data/'):
			if os.path.isdir('./data/' + x):
				self.serverList.append(x)
		self.serverVar = TK.StringVar(self)
		self.serverDropdown = TK.OptionMenu(self,self.serverVar, *self.serverList)
		self.serverDropdown.grid(column=1,row=0+1,sticky=TK.E+TK.W)
		self.serverDropdown.configure(width=15)
		self.serverVar.trace('w',self.serverchange)

		self.classList     = ['filler']
		self.classVar      = TK.StringVar(self)
		self.classDropdown = TK.OptionMenu(self,self.classVar, *self.classList)
		self.classDropdown.grid(column=1,row=1+1,sticky=TK.E+TK.W)
		self.classVar.trace('w',self.classchange)

		self.allbutton=TK.Button(self,text='All',command=self.showall)
		self.allbutton.grid(row=2+1,column=0,sticky='ew',columnspan=2)

		self.classonebutton=TK.Button(self,text='class 1',command=self.showc1)
		self.classonebutton.grid(row=2+1+1,column=0,sticky='ew',columnspan=2)

		self.classtwobutton=TK.Button(self,text='class 2',command=self.showc2)
		self.classtwobutton.grid(row=2+2+1,column=0,sticky='ew',columnspan=2)

		self.classthreebutton=TK.Button(self,text='class 3',command=self.showc3)
		self.classthreebutton.grid(row=2+3+1,column=0,sticky='ew',columnspan=2)

		self.splabel = TK.Label(self,justify=TK.LEFT)
		self.splabel.grid(row=2+4+1,column=0,sticky='wn',columnspan=2)

		self.warninglabel = TK.Label(#self,justify=TK.LEFT,width=self.w,wraplength=self.w*7)
									self,text="",width=self.w,justify=TK.LEFT,wraplength=self.w*7,anchor='nw')
		self.warninglabel.grid(row=2+4+1+1,column=0,sticky='nw',columnspan=2)

		self.pages = []
	def setlevel(self,event=None):
		self.level= int(self.levelentry.get())
		config.update()
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
		while len(self.pages) > 0:
			self.pages[0].grid_remove()
			del self.pages[0]
		self.pages=[]
		self.dir = './data/'+self.serverVar.get()+'/'
		self.pages.insert(0,SkillButtonFrame(config.skillpane,ET.parse(self.dir+self.classVar.get()).getroot()))
		while self.pages[0].superclass != 'none':
			self.pages.insert(0,SkillButtonFrame(config.skillpane,ET.parse(self.dir+'superclasses/'+self.pages[0].superclass).getroot()))
		for i in range(0,len(self.pages)):
			self.pages[i].grid(column=i,row=0,sticky='ns')
		self.classonebutton['text']   =self.pages[0].classname
		self.classtwobutton['text']   =self.pages[1].classname
		self.classthreebutton['text'] =self.pages[2].classname
		config.update()
	def skilltotal(self):
		total = 0
		self.nums = []
		for x in range(0,len(self.pages)):
			temp = self.pages[x].sp()
			total += temp
			self.nums.append(temp)
		text = 'SP Spent : ' + str(total) + '\n'
		text+= self.pages[0].classname + ' : ' + str(self.nums[0]) + '/'+str(self.maxsp[0][self.level])+'\n'
		text+= self.pages[1].classname + ' : ' + str(self.nums[1]) + '/'+str(self.maxsp[1][self.level])+'\n'
		text+= self.pages[2].classname + ' : ' + str(self.nums[2]) + '/'+str(self.maxsp[2][self.level])+'\n'
		text+= 'SP remaining : ' + str(self.spendingsp[self.level]-total)
		self.splabel['text']=text
		text='Warnings: \n'
		for x in self.validate():
			text+= x + '\n'
		self.warninglabel['text']=text

	def skillreset(self):
		for i in self.pages:
			i.skillreset()
		config.update()
	def validate(self):
		warnings = []
		bools = []
		ults=[]
		ultwarnings=[]
		skills = []
		for p in self.pages:
			skills.append(p.skills)
		for l in range(0,len(skills)):
			for r in range(0,len(skills[l])):
				for c in range(0,len(skills[l][r])):
					result = None
					skill = skills[l][r][c].skill if skills[l][r][c] is not None else None
					if skill is not None and skill.numranks > 0:
						if not skill.enoughsp():
							warnings.append(skill.name + ': requires ' + str(skill.spreq) + ' SP total from prev class')
						if skill.reqlevel is not None:
							#checking for level requirements
							if skill.getreqlevel(False) > self.level:
								warnings.append(skill.name + ' requires level ' + str(skill.getreqlevel(False)))
						if skill.reqskills is not None:
							#Checking for the requisite skills
							for pr in skill.reqskills:
								otherskill=skills[pr.classlevel][pr.row][pr.col].skill
								if otherskill is not None:
									if otherskill.numranks < pr.numranks:
										if not skill.isult:
											warnings.append(skill.name + ': needs '+str(pr.numranks)+' rank(s) in ' + otherskill.name)
										else:
											ultwarnings.append(skill.name + ': needs '+str(pr.numranks)+' rank(s) in ' + otherskill.name)
										result=False
									else:
										result = True if result == None else result
								else:
									print('None requirement found')
							if skill.isult:
								ults.append(skills[l][r][c])
								bools.append(result)
		#ults need to be checked separately
		#since one ult can be the requirement for the other one
		for i in range(0,len(ults)):
			if bools[i] is not None and bools[i] == False:
				if bools[i-1] is None or not bools[i-1]:
					while len(ultwarnings) > 0:
						warnings.append(ultwarnings.pop(0))
		return warnings

	def update(self):
		for x in self.pages:
			x.update()
		self.skilltotal()

class SkillDescFrame(ttk.Frame):
	def __init__(self,master):
		self.w=35
		self.line= '-'*self.w
		TK.Frame.__init__(self,master,bg='white')
		self.header=TK.Label(self,text="",anchor='nw',font=('default',20,),bg='white',justify=TK.LEFT)
		self.header.grid(column=0,row=0,sticky='nwe')

		self.textbox = TK.Label(self,text="",width=self.w,
							justify=TK.LEFT,wraplength=self.w*7,
							anchor='nw',bg='white')
		self.textbox.grid(column=0,row=1,sticky='wne')
		self.grid(column=1,row=0,sticky='nsw')

	def touch(self,skill):
		self.header['text']=skill.name
		temp = 'Skill Rank : ' + str(skill.numranks) + '\n'
		temp += 'cooldown : ' + str(skill.getcd())  + '\n' if skill.getcd() is not None else ''
		temp += self.line + '\n'
		if skill.levelreq() is not None:
			t = skill.levelreq()
			temp += 'level up requirements:\n'
			temp += 'Character level: ' + str(t[0]) + '\n'
			temp += 'SP required    : ' + str(t[1]) + '\n'
			temp += self.line + '\n'

		self.textbox['text']=temp + skill.getDesc()

class SkillButtonFrame(ttk.Frame):
	def __init__(self,master,xmlroot):
		TK.Frame.__init__(self,master,bg='black')
		self.superclass=xmlroot.attrib['superclass']
		self.classname=xmlroot.attrib['name']
		self.classLevel=int(xmlroot.attrib['classLevel'])
		self.skills=snip.twoD(int(xmlroot.attrib['numRows']),int(xmlroot.attrib['numCols']),None)
		for i in xmlroot:
			r = int(i.attrib['row'])
			c = int(i.attrib['col'])
			self.skills[r][c]=SkillButton(self,self.classLevel,i)
		for r in range(0,len(self.skills)):
			for c in range(0,len(self.skills[r])):
				if self.skills[r][c] != None:
					self.skills[r][c].grid(column=c,row=r,padx=1*5,pady=1*5)
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
	def update(self):
		for x in self.skills:
			for y in x:
				if y is not None:
					y.update()

class SkillButton(ttk.Frame):
	buttonbg=config.buttonbg
	def __init__(self, master,cl,sk=None):
		TK.Frame.__init__(self,master,width=8,height=4,bg='gray')
		if sk == None:
			self.skill=None
		else:
			self.button= TK.Button(self,command=None,width=8,height=4,wraplength=60,bd=0)
			self.button.grid(row=0)

			self.ranklabel= TK.Label(self,text='',bg='gray',fg='white')
			self.ranklabel.grid(row=1)

			self.skill = SK.Skill(sk,cl)
			self.button.bind('<Button-3>',self.rClick)
			self.button.bind('<Button-1>',self.lClick)
			self.button.bind('<Shift-Button-3>',self.shiftrclick)
			self.button.bind('<Shift-Button-1>',self.shiftlclick)
			self.bind('<Enter>',self.prod)
			self.seticon()
			
	def sp(self):
		if self.skill==None:
			return 0
		return self.skill.sp()
	def minimize(self):
		if self.skill != None:
			self.skill.minimize()
		if not config.resetting:
			config.update()
	def shiftrclick(self, event):
		self.skill.minimize()
		config.update()
	def shiftlclick(self, event):
		self.skill.maximize()
		config.update()
	def rClick(self,event):
		self.skill.rankDown()
		config.update()
	def lClick(self,event):
		self.skill.rankUp()
		config.update()
	def prod(self,event):
		config.descpane.touch(self.skill)
	def update(self):
		self.button['text']    = self.skill.name
		self.ranklabel['text'] = str(self.skill.numranks) + '/' + str(self.skill.limit)
		self.seticon()
	def gettext(self):
		return self.skill.name + "\n" + str(self.skill.numranks) + '/' + str(self.skill.limit)
	def seticon(self):
		if self.skill.geticon() is not None and config.image:
			try:
				self.icon = ImageTk.PhotoImage(file='./icons/' + self.skill.geticon())
				self.button.configure(image=self.icon,width=65,height=65)
			except:
				config.image=False