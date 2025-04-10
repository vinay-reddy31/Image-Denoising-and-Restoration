# -*- coding: utf-8 -*-
"""harmonic_mean.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gEQKWDmVIgfwtLyhudEeHq8vYOBcWdMM
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_harmonic_mean_filter(image, kernel_size):
    padded_image = cv2.copyMakeBorder(image, kernel_size//2, kernel_size//2, kernel_size//2, kernel_size//2, cv2.BORDER_REFLECT)
    output_image = np.zeros_like(image, dtype=np.float32)
    for i in range(kernel_size//2, padded_image.shape[0] - kernel_size//2):
        for j in range(kernel_size//2, padded_image.shape[1] - kernel_size//2):
            neighborhood = padded_image[i - kernel_size//2:i + kernel_size//2 + 1, j - kernel_size//2:j + kernel_size//2 + 1]
            harmonic_mean = kernel_size * kernel_size / np.sum(1.0 / (neighborhood + 1e-7))
            output_image[i - kernel_size//2, j - kernel_size//2] = harmonic_mean
    return np.uint8(output_image)

# Paths to images
image_path = '/content/drive/MyDrive/imageProcessing-nitw/Fig0507(b)(ckt-board-gauss-var-400).tif'
additional_image_path = '/content/drive/MyDrive/imageProcessing-nitw/Fig0507(a)(ckt-board-orig).tif'

# Read images
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
additional_image = cv2.imread(additional_image_path, cv2.IMREAD_GRAYSCALE)

# Check if images are loaded
if image is None:
    print(f"Failed to load image from {image_path}")
elif additional_image is None:
    print(f"Failed to load image from {additional_image_path}")
else:
    # Apply harmonic mean filter
    filtered_harmonic_mean = apply_harmonic_mean_filter(image, 3)

    # Display images
    plt.figure(figsize=(16, 4))
    plt.subplot(1, 4, 1)
    plt.imshow(additional_image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(image, cmap='gray')
    plt.title('Gaussian Noise')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(filtered_harmonic_mean, cmap='gray')
    plt.title('Harmonic Mean Filter (3x3)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

