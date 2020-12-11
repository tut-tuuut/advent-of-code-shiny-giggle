from PIL import Image


def reverse_chunks(list, size):
    for i in range(0, len(list), size):
        final = len(list) if i == 0 else -i
        yield list[-i - size : final]


with open(__file__ + ".input") as file:
    img = file.read()

imgWidth = 25
imgHeight = 6
imgSize = 25 * 6

minCountOfZeros = imgSize
checksum = 0
for layer in reverse_chunks(list(img), imgSize):
    countOfZeros = layer.count("0")
    if countOfZeros < minCountOfZeros:
        minCountOfZeros = countOfZeros
        checksum = layer.count("1") * layer.count("2")
print(f"part 1 answer: checksum is {checksum}")

imgFile = Image.new("1", (imgWidth + 4, imgHeight + 6))
for layer in reverse_chunks(list(img), imgSize):
    for k, pixel in enumerate(layer):
        print(k, pixel)
        y = 1 + k // imgWidth
        x = k % imgWidth
        print(x, y)
        if pixel == "0":
            imgFile.putpixel((x, y), 0)
        elif pixel == "1":
            imgFile.putpixel((x, y), 1)

imgFile.show()
