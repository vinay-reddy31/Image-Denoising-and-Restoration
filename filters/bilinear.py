# -*- coding: utf-8 -*-
"""bilinear.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bXHILab9A_2B9L4Mt9txSMt0_RM0IX1H
"""

!pip install lpips

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import cifar10
from skimage.transform import resize
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
import torch
import lpips
from tqdm import tqdm
import time
import pandas as pd

# Load CIFAR-10 dataset
(X_train, _), (X_test, _) = cifar10.load_data()

# Normalize images
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Use a subset of the dataset for quicker execution
X_train = X_train[:1000]
X_test = X_test[:100]

# Create low-resolution images by downscaling
def create_lr_images(images, scale_factor=3):
    lr_images = []
    for i in range(images.shape[0]):
        lr_img = resize(images[i],
                        (images.shape[1] // scale_factor, images.shape[2] // scale_factor),
                        anti_aliasing=True)
        lr_images.append(lr_img)
    return np.array(lr_images)

X_train_lr = create_lr_images(X_train)
X_test_lr = create_lr_images(X_test)

# Apply bilinear interpolation to upscale the images
def apply_bilinear_interpolation(lr_images, original_shape):
    hr_images = np.zeros(original_shape)
    for i in range(lr_images.shape[0]):
        hr_img = resize(lr_images[i], original_shape[1:], anti_aliasing=True, order=1)  # order=1 for bilinear interpolation
        hr_images[i] = hr_img
    return hr_images

X_train_bilinear = apply_bilinear_interpolation(X_train_lr, X_train.shape)
X_test_bilinear = apply_bilinear_interpolation(X_test_lr, X_test.shape)

# Calculate PSNR
def calculate_psnr(original, generated):
    return psnr(original, generated)

# Calculate SSIM
def calculate_ssim(original, generated):
    return ssim(original, generated, multichannel=True)

# Calculate LPIPS using PyTorch
def calculate_lpips(original, generated):
    loss_fn = lpips.LPIPS(net='vgg')
    original_torch = torch.tensor(original.transpose(2, 0, 1)).unsqueeze(0).float()
    generated_torch = torch.tensor(generated.transpose(2, 0, 1)).unsqueeze(0).float()
    lpips_value = loss_fn(original_torch, generated_torch)
    return lpips_value.item()

# Evaluate the bilinear interpolation method
psnr_values = []
ssim_values = []
lpips_values = []

start_time = time.time()

for i in tqdm(range(len(X_test_lr)), desc="Processing images"):
    lr_img = X_test_lr[i]
    hr_img = X_test[i]
    sr_img = X_test_bilinear[i]

    psnr_value = calculate_psnr(hr_img, sr_img)
    ssim_value = calculate_ssim(hr_img, sr_img)
    lpips_value = calculate_lpips(hr_img, sr_img)

    psnr_values.append(psnr_value)
    ssim_values.append(ssim_value)
    lpips_values.append(lpips_value)

# Calculate total time taken
end_time = time.time()
total_time = end_time - start_time

# Calculate average metrics
avg_psnr = np.mean(psnr_values)
avg_ssim = np.mean(ssim_values)
avg_lpips = np.mean(lpips_values)

print(f"Average PSNR: {avg_psnr}")
print(f"Average SSIM: {avg_ssim}")
print(f"Average LPIPS: {avg_lpips}")
print(f"Total time taken: {total_time} seconds")

# Create a DataFrame with the metrics
data = {
    'Average PSNR': [avg_psnr],
    'Average SSIM': [avg_ssim],
    'Average LPIPS': [avg_lpips]
}
df = pd.DataFrame(data, index=['Bilinear'])

# Save the DataFrame to an Excel file
df.to_excel('metrics_bilinear.xlsx')

print("Excel file created successfully.")

# Function to show images
def show_images(lr_img, sr_img, hr_img):
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.title('Low Resolution')
    plt.imshow(lr_img)
    plt.subplot(1, 3, 2)
    plt.title('Bilinear Interpolation')
    plt.imshow(sr_img)
    plt.subplot(1, 3, 3)
    plt.title('High Resolution')
    plt.imshow(hr_img)
    plt.show()

# Show predictions on test images
for i in range(5):
    show_images(X_test_lr[i], X_test_bilinear[i], X_test[i])

