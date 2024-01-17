import colorsys
from PIL import Image

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
    dominant_color = box.getcolors(box.size[0]*box.size[1])[0][1]

    # Only return the RGB values, not the alpha channel
    return dominant_color[:3]

def get_apple_color_percentage(image_path, box_size):
    image = Image.open(image_path)
    dominant_color = get_dominant_color(image, box_size)

    green_apple = [136, 181, 3]
    yellow_apple = [255, 212, 18]
    red_apple = [143, 67, 69]

    percentage = calculate_percentage(dominant_color, green_apple, yellow_apple, red_apple)
    return percentage

# Usage
image_path = 'download (6).jpeg'
box_size = 100
print(get_apple_color_percentage(image_path, box_size))