import snip
import xml.etree.ElementTree as ET
tree = ET.parse('./data/NA/assassin.xml')
root = tree.getroot()
skill = root[16]
if skill.find('duration') is not None:
	print('it worked')
