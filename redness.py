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

    # Show the cropped image
    cropped_img.show()

    # Return the average RGB value as a color
    return 'rgb{}'.format(average_rgb)

# Test the function
image_path = 'download (5).jpeg'
print(calculate_average_rgb(image_path))