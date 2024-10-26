from fer import FER
from PIL import Image
import pyheif
import numpy as np

def compute_face_exp(image_path, confidence_threshold=0.5):
    """
    Analyzes the facial expressions in an image and returns the count of detected faces
    and the most prominent emotion.

    Args:
        image_path (str): The path to the image file.
        confidence_threshold (float): The threshold for considering a detected emotion.

    Returns:
        tuple: A tuple containing the count of detected faces and the most prominent emotion.
    """
    
    # Load the image
    if image_path.lower().endswith('.heic'):
        heif_file = pyheif.read(image_path)
        image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data,
                                 "raw", heif_file.mode, heif_file.stride)
    else:
        image = Image.open(image_path)

    # Convert the PIL image to a NumPy array
    image_np = np.array(image)

    # Initialize the FER detector
    detector = FER()

    # Analyze the image for facial expressions
    results = detector.detect_emotions(image_np)

    # Initialize variables
    total_faces = 0
    most_prominent_emotion = None

    if results:  # If faces are detected
        total_faces = len(results)  # Count of detected faces
        for result in results:
            emotions = result['emotions']
            # Get the most prominent emotion from the first detected face
            if most_prominent_emotion is None or max(emotions.values()) > emotions[most_prominent_emotion]:
                most_prominent_emotion = max(emotions, key=emotions.get)

            # Check confidence threshold
            if emotions[most_prominent_emotion] < confidence_threshold:
                most_prominent_emotion = None  # Reset if below threshold
        
    return total_faces, most_prominent_emotion