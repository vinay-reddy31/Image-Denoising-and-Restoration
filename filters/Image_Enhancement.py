import numpy as np
import cv2
import matplotlib.pyplot as plt

def apply_histogram_equalization(image_path):
    image = cv2.imread(image_path)
    num_array = np.array(image)

    flattened_array = num_array.flatten()
    value_counts = {i: 0 for i in range(256)}
    for value in flattened_array:
        if 0 <= value < 256:
            value_counts[value] += 1

    new_dict = {}
    for i in value_counts:
        if value_counts[i] != 0:
            new_dict[i] = value_counts[i]

    sum_of_all_values = sum(new_dict.values())

    prob_new_dict = {}
    for i in new_dict:
        prob_new_dict[i] = new_dict[i] / sum_of_all_values

    size = len(prob_new_dict)
    prob_new_dict_values = list(prob_new_dict.values())

    cumulative_prob_new_dict_sum = 0
    cumsum_list = []
    for i in prob_new_dict.values():
        cumulative_prob_new_dict_sum += i
        cumsum_list.append(cumulative_prob_new_dict_sum)
    s = []
    for i in cumsum_list:
        s.append(round(255 * i))

    new_values = {}
    for j, value in zip(prob_new_dict.keys(), s):
        new_values[j] = value
    replacement_dict = new_values
    replaced_array = np.vectorize(replacement_dict.get)(num_array)

    return num_array, replaced_array

def plot_histogram(image, title):
    pixel_intensities = image.flatten()
    plt.hist(pixel_intensities, bins=range(0, 256), color='blue', alpha=0.7)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(True)

def process_and_display_image(image_path):
    original_image, replaced_image = apply_histogram_equalization(image_path)

    plt.figure(figsize=(16, 4))
    # Plot original image and histogram
    plt.subplot(1, 4, 1)
    plt.imshow(original_image, cmap="gray")
    plt.axis("off")
    plt.title('Original Image')

    plt.subplot(1, 4, 2)
    plot_histogram(original_image, 'Histogram of Original Image')

    # Plot modified image and histogram
    plt.subplot(1, 4, 3)
    plt.imshow(replaced_image, cmap="gray")
    plt.axis("off")
    plt.title('Modified Image')

    plt.subplot(1, 4, 4)
    plot_histogram(replaced_image, 'Histogram of Modified Image')

    plt.tight_layout()
    plt.show()

def main(image_paths):
    for image_path in image_paths:
        process_and_display_image(image_path)


image_paths = ["/content/Fig0320(1)(top_left).tif",
               "/content/Fig0320(2)(2nd_from_top).tif",
               "/content/Fig0320(3)(third_from_top).tif",
               "/content/Fig0320(4)(bottom_left).tif"]

main(image_paths)

