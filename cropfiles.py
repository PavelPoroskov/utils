from PIL import Image

def cropm(_strF):
	strF = "c:\\temp\\2\\" + _strF + ".png"
	strTo = "c:\\temp\\2\\" + _strF + "_22.png"
	img = Image.open(strF)

	width = img.size[0]
#	height = img.size[1]

	img2 = img.crop((62, 66, width, 298))
	img2.save(strTo)

cropm("1")
cropm("2")
cropm("3")
cropm("4")
cropm("5")
cropm("6")