from PIL import Image

source = input("Source image path: ")
output = input("Output image path: ")

scaleFactor = int(input("Size of blur: "))

img = Image.open(source)
size = img.size

pix = img.load()

def boxAverage(i, j):
	col = (0, 0, 0)
	count = 0
	for x in range(-scaleFactor, scaleFactor-1):
		for y in range(-scaleFactor, scaleFactor-1):
			if((i + x) < 0 or (i + x) >= size[0] or (j + y) < 0 or (j + y) >= size[1]):
				continue

			c = pix[i + x, j + y]
			col = (col[0] + c[0], col[1] + c[1], col[2] + c[2])
			count += 1
	return (int(col[0]/count), int(col[1]/count), int(col[2]/count))

for i in range(0, size[0]) :
	for j in range(0, size[1]) :
		pix[i, j] = boxAverage(i, j)

img.save(output)
print("Blur Finished")