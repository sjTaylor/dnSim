import snip
import xml.etree.ElementTree as ET
import skill
tree = ET.parse('./data/NA/assassin.xml')
root = tree.getroot()
#if skill.find('duration') is not None:
#	print('it worked')

x = skill.Skill(root[9])
y = skill.Skill(root[0])
#x.getDesc()
#"""
for j in range(0,6):
	print(x.getDesc())
	x.rankUp()
	x.rankUp()
	print('\n')
	print(y.getDesc())
	y.rankUp()
	y.rankUp()
	print('\n\n\n')
	

#"""
'''
j = skill.VarList(root[0][2])
print(j[1])
'''