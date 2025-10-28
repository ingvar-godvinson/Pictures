from PIL import Image

image1 = Image.open("red.jpg")
image2 = Image.open("green.jpg")
image3 = Image.open('blue.jpg')
new_image = Image.merge("RGB", (image1, image2, image3))
new_image.save("monro_1.jpg")
image = Image.open("monro_1.jpg")
image.thumbnail((80, 70))
image.save("monro_2.jpg")