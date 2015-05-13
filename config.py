#image can be changed to False to disable skill icons
image=True
control=None
skillpane=None
descpane=None
updatelist={}

buttonbg='#4F5144'

def update():
	for x in updatelist:
		updatelist[x]()


try:
	import PIL
except:
	image=False