from skill import VarList

#image can be changed to False to disable skill icons
image=True
updatelist={}

buttonrankbg='#4F5144'
buttonrankfontcolor='white'

#below has each class section as a different color
skillpagebg = ['black','#003366','black']
#if you want them to all be black comment the line above, and uncomment the one below
#skillpagebg = ['black']

#don't edit stuff below here
control=None
skillpane=None
descpane=None

skillpagebg = VarList(arr=skillpagebg)

def update():
	for x in updatelist:
		updatelist[x]()
try:
	import PIL
except:
	image=False