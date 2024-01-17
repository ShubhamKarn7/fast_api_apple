from PIL import Image
import colorsys
import numpy as np

def calculate_percentage(rgb_color, start_color, mid_color, end_color):
    rgb_normalized = [c / 255.0 for c in rgb_color]
    start_normalized = [c / 255.0 for c in start_color]
    mid_normalized = [c / 255.0 for c in mid_color]
    end_normalized = [c / 255.0 for c in end_color]

    start_hsv = colorsys.rgb_to_hsv(*start_normalized)
    mid_hsv = colorsys.rgb_to_hsv(*mid_normalized)
    end_hsv = colorsys.rgb_to_hsv(*end_normalized)
    rgb_hsv = colorsys.rgb_to_hsv(*rgb_normalized)

    if start_hsv[0] <= rgb_hsv[0] <= mid_hsv[0]:
        percentage = (rgb_hsv[0] - start_hsv[0]) / (mid_hsv[0] - start_hsv[0]) * 50
    else:
        percentage = 50 + (rgb_hsv[0] - mid_hsv[0]) / (end_hsv[0] - mid_hsv[0]) * 50

    return max(0, min(100, percentage))

def get_dominant_color(image, box_size):
    center_x, center_y = image.size[0] // 2, image.size[1] // 2
    box_left = max(0, center_x - box_size // 2)
    box_upper = max(0, center_y - box_size // 2)
    box_right = min(image.size[0], center_x + box_size // 2)
    box_lower = min(image.size[1], center_y + box_size // 2)

    box = image.crop((box_left, box_upper, box_right, box_lower))
    np_image = np.array(box)
    r, g, b = np_image[..., :3].mean(axis=(0, 1))

    return r, g, b

green = (136, 181, 3)
yellow = (255, 212, 18)
red = (143, 67, 69)

image = Image.open('Screenshot 2024-01-16 174913.png')
dominant_color = get_dominant_color(image, 50)
percentage = calculate_percentage(dominant_color, green, yellow, red)

print(f'The color of the apple is {percentage}% transitioned from green to red.')