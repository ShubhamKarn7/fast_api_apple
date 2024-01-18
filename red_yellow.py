from PIL import Image, ImageDraw, ImageFont

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
