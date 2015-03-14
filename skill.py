import re
class Skill:
	"""The class used for holding, and processing, the data for skills"""
	
	def __init__(self, root,cl):
		self.classlevel=cl
		self.name = "filler_name"
		self.row = 0
		self.col = 0
		self.duration = None
		self.cooldown = None
		self.reqlevel = None
		self.buyInCost = 3
		self.startRanks = 0
		self.numRanks = 0
		self.limit = 1
		self.isUlt = False
		self.desc = "filler \\nskill name"
		self.reqskills = None
		self.vars = dict()
		self.numRanks = 0
		if 'dataVersion' in root.attrib:
			temp = root.attrib['dataVersion']
			if temp == '1':
				self.initV1(root)
		else:
			self.initV1(root)
	def getDesc(self):
		if self.numRanks >= 1:
			s1 = self.getText(self.desc,self.vars,self.numRanks-1)
			s2 = self.getText(self.desc,self.vars,self.numRanks)
		else:
			s1 = self.getText(self.desc,self.vars,self.numRanks)
			s2 = self.getText(self.desc,self.vars,self.numRanks+1)
		
		if s1 != s2:
			return s1 + '\n' + '-'*15 + '\n' + s2
		return s1
	def initV1(self, root):
		attr = root.attrib
		self.row = int(attr['row'])
		self.col = int(attr['col'])
		self.name = attr['name']
		self.limit = int(attr['limit'])
		self.desc = root.find('desc').text
		
		if 'isUlt' in attr:
			self.isUlt = attr['isUlt'] == 'True'
		if 'startRanks' in attr:
			self.startRanks = int(attr['startRanks'])
			self.numRanks=self.startRanks
		if 'buyInCost' in attr:
			self.buyInCost = int(attr['buyInCost'])
		if root.find('duration') is not None:
			self.duration = VarList(root.find('duration'))
		if root.find('cooldown') is not None:
			self.cooldown = VarList(root.find('cooldown'))
		
		for x in root.findall('var'):
			self.vars[x.attrib['id']] = VarList(x)
		if root.find('reqlevel') is not None:
			for x in root.find('reqlevel'):
				self.reqlevel=VarList(x.text,'yes')
		if root.find('reqskills') != None:
			self.reqskills = []
			for x in root.find('reqskills').text.split(','):
				self.reqskills.append(PreReq(x,self,self.classlevel))
	def minimize(self):
		self.numRanks = self.startRanks
	def maximize(self):
		self.numRanks = self.limit
	def getText(self, string, vars, level):
		while string.find('{') >= 0:
			start = string.find('{')
			end = string.find('}')
			string = string[0:start] + vars[string[start+1:end]][level] + string[end+1:]
		string = string.replace("\\n","\n")
		return string
	def rankUp(self):
		self.numRanks = min(self.limit,self.numRanks+1)
	def rankDown(self):
		self.numRanks = max(self.startRanks,self.numRanks-1)
	def getreqlevel(self):
		if self.reqlevel is None:
			return 1
		return self.reqlevel[self.numRanks]
	def sp(self):
		if self.numRanks > 0:
			if self.numRanks > 1:
				return self.buyInCost + self.numRanks - 1
			return self.buyInCost
		return 0

class VarList:
	def __init__(self, node, type='nope'):
		self.predict = False
		self.vals = []
		if 'type' in node.attrib:
			self.predict = node.attrib['type'] == 'yes'
		else:
			self.predict = type == 'yes'
		if self.predict:
			for q in node.text.split(','):
				self.vals.append(int(q))
		else:
			for q in node.text.split(','):
				self.vals.append(q)
	def __getitem__(self, dex):
		if len(self.vals) is 0:
			return None
		if self.predict:
			return self.getPredictedVal(self.vals,dex)
		return self.getCutoffVal(self.vals,dex)
	def getCutoffVal(self, nums, index):
		if len(nums) <= index:
			return nums[-1]
		return nums[index]
	def getPredictedVal(self, nums, index):
		if index < len(nums):
			return nums[index]
		perLevel = nums[-1] - nums[-2]
		diff = index - len(nums)
		return nums[-1] + perLevel*diff


class PreReq:
	def __init__(self,pr,skill,cl):
		self.classlevel=cl
		self.row=skill.row
		self.col=skill.col
		self.numranks=1
		temp = pr.split(':')
		if re.match('[nsew].*',pr):
			if temp[0] == 'n':
				self.row-=1
			elif temp[0] == 's':
				self.row+= 1
			elif temp[0] == 'e':
				self.col+= 1
			elif temp[0] == 'w':
				self.col-= 1
			if ':' in pr:
				self.numranks = int(temp[-1])
		else:
			#if it uses a non-default # of ranks
			if re.match('\\d+:\\d+:\\d+:\\d+',pr):
				self.numranks = int(temp[-1])
			self.classlevel=int(temp[0])
			self.row=int(temp[1])
			self.col=int(temp[2])