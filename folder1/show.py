from PIL import Image

image = Image.open("noise_removed.png")
image_array = image.load()

for i in range(image.size[0]):
    for j in range(image.size[1]):
        pixel_value = int(sum(image_array[i, j]) / 3)
        print(f"Pixel ({i}, {j}): {pixel_value:3d}")