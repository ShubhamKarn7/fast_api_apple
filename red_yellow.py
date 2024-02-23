from PIL import Image, ImageDraw, ImageFont

import os
import time
import requests

def send_image(filename, server_url):
    try:
        with open(filename, 'rb') as file:
            files = {'file': (filename, file, 'image/jpeg')}
            response = requests.post(server_url, files=files)
            print(f'Sent {filename}, Status Code: {response.status_code}')
            print(response.text)
    except Exception as e:
        print(f'Error sending {filename}: {e}')

def send_images_from_folder(folder_path, server_url):
    while True:
        try:
            image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            for image_file in image_files:
                image_path = os.path.join(folder_path, image_file)
                send_image(image_path, server_url)
                time.sleep(0.3)  # Wait for 1 second before sending the next image
        except KeyboardInterrupt:
            print("Script terminated by user.")
            break
        except Exception as e:
            print(f'Error: {e}')
            time.sleep(1)  # Wait for 1 second before retrying
            
def calculate_average_rgb(image_path, box_size=100):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Calculate the coordinates for the bounding box
    left = max(0, width // 2 - box_size // 2)
    top = max(0, height // 2 - box_size // 2)
    right = min(width, width // 2 + box_size // 2)
    bottom = min(height, height // 2 + box_size // 2)

    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))

    # Calculate the average RGB value
    average_rgb = tuple(int(x) for x in cropped_img.resize((1, 1)).getpixel((0, 0)))

    # Return the average RGB value as a color
    return average_rgb

# Test the function


apple_colors = {
    "green": [(0, 150, 0), (150, 255, 255)],  # Adjust ranges as needed
    "yellow": [(150, 150, 0), (255, 255, 255)],  # Adjust ranges as needed
    "lime_yellow": [(150, 80, 0), (225, 150, 255)],
    "red": [(0, 0, 0), (255, 60, 255)]
}

def find_color_range(rgb_value, color_ranges):
    for color, ranges in color_ranges.items():
        min_range, max_range = ranges
        if all(min_val <= val <= max_val for val, (min_val, max_val) in zip(rgb_value, zip(min_range, max_range))):
            return color
    return "Unknown"

# Example usage:
image_path = 'download (6).jpeg'
print(calculate_average_rgb(image_path))
rgb_value_to_check = calculate_average_rgb(image_path)
result = find_color_range(rgb_value_to_check, apple_colors)
print(f"The RGB value {rgb_value_to_check} belongs to the {result} color range.")
