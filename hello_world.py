from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()
new_image = Image.merge("RGB", (red, green, blue))
red_1 = red.crop((100, 0, 696, 522))
red_2 = red.crop((50, 0, 646, 522))
red_3 = Image.blend(red_1, red_2, 0.5)
blue_1 = blue.crop((0, 0, 596, 522))
blue_2 = blue.crop((50, 0, 646, 522))
blue_3 = Image.blend(blue_1, blue_2, 0.5)
green_1 =green.crop((50, 0, 646, 522))
new_image = Image.merge("RGB", (red_3, green_1, blue_3))
new_image.save("monro_2.jpg")

new_image.thumbnail((80, 70))
image.save("monro_3.jpg")