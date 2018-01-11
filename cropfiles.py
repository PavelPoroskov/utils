#from PIL import Image
from PIL import Image

def cropm(_strF):
	strF = "/home/*/Pictures/" + _strF + ".png"
	strTo = "/home/*/Pictures/" + _strF + "_22.png"
	img = Image.open(strF)

	width = img.size[0]
#	height = img.size[1]

	img2 = img.crop((1, 116, width-1, 270))
	img2.save(strTo)

cropm("2.1")
cropm("2.2")
cropm("2.2gr")
cropm("2.3")
cropm("2.4")
cropm("2.5")
