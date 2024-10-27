from colorthief import ColorThief
from PIL import Image
import pyheif
import os

def compute_color(image_path):
    """
    Process an image to extract the dominant color and classify it as Warm, Cool, or Neutral.

    Parameters:
    image_path (str): The path to the image file (can be HEIC or JPG).

    Returns:
    str: A string summarizing the dominant color classification percentages or an error message.
    """

    # Function to classify the color as Warm, Cool, or Neutral based on RGB values
    def classify_color(rgb):
        r, g, b = rgb
        total = r + g + b
        warm_percentage = (r / total)
        cool_percentage = (b / total)
        neutral_percentage = (g / total)
        
        return warm_percentage, cool_percentage, neutral_percentage

    # Function to handle .HEIC images and convert them to JPG
    def convert_heic_to_jpg(heic_path):
        heif_file = pyheif.read(heic_path)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data, 
            "raw", 
            heif_file.mode, 
            heif_file.stride
        )
        jpg_path = heic_path.replace('.heic', '.jpg')
        image.save(jpg_path, "JPEG")
        return jpg_path

    # Check if the file exists
    if not os.path.exists(image_path):
        return f"File does not exist at: {image_path}"

    # Handle HEIC format by converting to JPG if necessary
    if image_path.lower().endswith('.heic'):
        print("Converting HEIC to JPG...")
        image_path = convert_heic_to_jpg(image_path)

    # Open the image and use ColorThief to get the dominant color
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color(quality=1)  # Extract dominant color (RGB)
    
    # Classify the image based on the dominant color
    warm, cool, neutral = classify_color(dominant_color)

    # Return the classification result as percentages
    return [warm, cool, neutral]

# Example usage
# image_path = "/Users/daanish/Downloads/picture.heic"  # Replace with your image path
# result = process_and_classify_color(image_path)
# print(result)
