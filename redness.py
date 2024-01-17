import cv2
import numpy as np

def calculate_red_percentage(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Define the lower and upper bounds for the red color
    lower_red = np.array([0, 0, 100], dtype="uint8")
    upper_red = np.array([100, 100, 255], dtype="uint8")

    # Create a mask to extract the red portion
    red_mask = cv2.inRange(rgb_image, lower_red, upper_red)

    # Count the number of red pixels
    red_pixel_count = cv2.countNonZero(red_mask)

    # Calculate the percentage of red pixels
    total_pixels = image.shape[0] * image.shape[1]
    red_percentage = (red_pixel_count / total_pixels) * 100

    return red_percentage

# Example usage
image_path = "red-del1.jpeg"
percentage_red = calculate_red_percentage(image_path)
print(f"Percentage of red portion on the apple: {percentage_red}%")
