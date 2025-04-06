# -*- coding: utf-8 -*-
"""median_filter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M9Mo4PpM6dgQUcworOAA3lS7OUgUd0DG
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to apply median filter without using built-in functions
def median_filter(image, kernel_size=3):
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_window = padded_image[i:i+kernel_size, j:j+kernel_size]
            filtered_image[i, j] = np.median(local_window)

    return filtered_image

# Load images
image1_path = '/content/drive/MyDrive/imageProcessing-nitw/Fig0512(a)(ckt-uniform-var-800).tif'
image2_path = '/content/drive/MyDrive/imageProcessing-nitw/Fig0512(b)(ckt-uniform-plus-saltpepr-prob-pt1).tif'

image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

# Check if images are loaded
if image1 is None:
    print(f"Failed to load image from {image1_path}")
elif image2 is None:
    print(f"Failed to load image from {image2_path}")
else:
    # Apply median filter to the second image
    median_filtered_image = median_filter(image2)

    # Display the images
    titles = ['Original Image 1', 'Original Image 2', 'Median Filter']
    images = [image1, image2, median_filtered_image]

    plt.figure(figsize=(12, 8))
    for i in range(3):
        plt.subplot(2, 2, i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.tight_layout()
    plt.show()

