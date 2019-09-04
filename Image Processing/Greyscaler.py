from PIL import Image

source = input("Enter a source filepath:")
output = input("Enter a destination filepath:")

img = Image.open(source)
pix = img.load()

size = img.size

for i in range(0, img.size[0]):
	for j in range(0, img.size[1]):

		col = img.getpixel((i, j))
		grey = int((col[0] + col[1] + col[2])/3)
		pix[i, j] = (grey, grey, grey)

img.save(output + ".png")
print("Greyscaling finished!")