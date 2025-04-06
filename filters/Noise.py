import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load your images
image1 = mpimg.imread('/content/Fig0504(a)(gaussian-noise).tif')
image2 = mpimg.imread('/content/Fig0504(b)(rayleigh-noise).tif')
image3 = mpimg.imread('/content/Fig0504(c)(gamma-noise).tif')
image4 = mpimg.imread('/content/Fig0504(g)(neg-exp-noise).tif')
image5 = mpimg.imread('/content/Fig0504(h)(uniform-noise).tif')
image6 = mpimg.imread('/content/Fig0504(i)(salt-pepper-noise).tif')

# List of images and titles
images = [image1, image2, image3, image4, image5, image6]
titles = ['Gaussian Noise', 'Rayleigh Noise', 'Gamma Noise', 'Negative Exponential Noise', 'Uniform Noise', 'Salt & Pepper Noise']

# Create a 3x4 grid for images and their histograms
fig, axs = plt.subplots(3, 4, figsize=(20, 15))

for i, (image, title) in enumerate(zip(images, titles)):
    # Plot the image
    ax_img = axs[i//2, (i%2)*2]
    ax_img.imshow(image, cmap='gray')
    ax_img.set_title(title)
    ax_img.axis('off')  # Hide the axes ticks

    # Plot the histogram
    ax_hist = axs[i//2, (i%2)*2 + 1]
    ax_hist.hist(image.ravel(), bins=256, color='gray', alpha=0.7, edgecolor='black')
    ax_hist.set_title(f'Histogram of {title}')
    ax_hist.set_xlabel('Pixel Intensity')
    ax_hist.set_ylabel('Frequency')

plt.tight_layout()
plt.show()