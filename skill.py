class Skill:
	"""The class used for holding, and processing, the data for skills"""
	name = "filler_name"
	row = 0
	col = 0
	duration = None
	cooldown = None
	reqLevel = None
	buyInCost = 3
	startRanks = 0
	numRanks = 0
	limit = 1
	isUlt = False
	desc = "filler \\nskill name"
	requiredSkills = []
	requiredLevel = []
	vars = []
	numRanks = 0
	def __init__(root):
		if 'dataVersion' in root.attrib:
			temp = root.attrib['dataVersion']
			if temp == '1'
				initV1(root)
		else:
			initV1(root)
	def initV1(root):
		attr = root.attrib
		row = int(attr['row'])
		col = int(attr['col'])
		name = attr['name']
		limit = int(attr['limit'])
		desc = root.find('desc')
		for x in root.findall('var'):
			var[root.attrib['id']
		if 'isUlt' in attr:
			isUlt = attr['isUlt'] == 'True'
		if 'startRanks' in attr:
			startRanks = int(attr['startRanks'])
		if 'buyInCost' in attr:
			buyInCost = int(attr['buyInCost'])
		if root.find('duration') is not None:
			duration = VarList(root.find('duration'))
		if root.find('cooldown') is not None:
			cooldown = VarList(root.find('cooldown'))
		
		
	def getText(string,vars):
	def rankUp():
		numRanks = min(limit,numRanks+1)
	def rankDown():
		numRanks = max(startRanks,numRanks-1)
	def getReqLevel():
		return reqLevel[numRanks]

class VarList:
	isPredictive = False
	vals = []
	def __init__(node):
		for q in node.text.split(','):
			vals.append(int(q))
		if 'type' in node.attrib:
			isPredictive = node.attrib['type'] == 'predict'
	#to help accomodate things like duration that are automatically predictive
	def __init(node, type)
		__init__(node)
		isPredictive = type == 'predict'
	def __getItem__(obj, dex):
		if len(vals) is 0:
			return None
		if isPredictive:
			return getPredictedVal(vals,index)
		return getCutoffVal(vals,index)
	def getCutoffVal(nums, index):
		if len(nums) >= index:
			return nums[-1]
		return nums[index]
	def getPredictedVal(nums, index):
		if index < len(nums):
			return nums[index]
		perLevel = nums[-2] - nums[-1]
		diff = index - len(nums)
		return nums[-1] + perLevel*diff