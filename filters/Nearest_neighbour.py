from PIL import Image
import numpy as np

def nearest_neighbors_upscale(image_path, scale_factor):
    img = Image.open(image_path)
    img_array = np.array(img)

    orig_height, orig_width, num_channels = img_array.shape

    new_height = orig_height * scale_factor
    new_width = orig_width * scale_factor

    new_img_array = np.zeros((new_height, new_width, num_channels), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            orig_i = i // scale_factor
            orig_j = j // scale_factor
            new_img_array[i, j] = img_array[orig_i, orig_j]

    new_img = Image.fromarray(new_img_array)
    return new_img

image_path = '/content/dog.jpeg'
upscaled_image = nearest_neighbors_upscale(image_path, 2)
upscaled_image.show() 
upscaled_image.save('upscaled_image_nearest_neighbors.jpg')
