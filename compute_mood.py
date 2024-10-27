import clip
import torch
from PIL import Image
import pyheif
import os

def convert_heic_to_jpg(image_path):
    # If the file is HEIC, convert it to JPG using pyheif
    if image_path.lower().endswith('.heic'):
        heif_file = pyheif.read(image_path)
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        # Save as a temporary JPG file
        jpg_path = image_path.replace('.heic', '.jpg')
        image.save(jpg_path, "JPEG")
        return jpg_path
    else:
        return image_path

def compute_mood(image_path) -> float:
    # Convert HEIC to JPG if necessary
    image_path = convert_heic_to_jpg(image_path)

    # Load the CLIP model and preprocessing pipeline
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)

    # Define descriptors for the atmospheres we want
    atmosphere_descriptions = ["calm", "nostalgic", "romantic", "mysterious", "joyful", "energetic"]

    # Tokenize the text descriptions
    text_tokens = clip.tokenize(atmosphere_descriptions).to(device)

    # Load and preprocess your image
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

    # Encode the image and text to get their features
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_tokens)

    # Calculate cosine similarity between image and each text descriptor
    similarities = (image_features @ text_features.T).squeeze(0).softmax(dim=0)

    # Display the scores for each atmosphere description
    atmosphere_scores = {}
    
    for description, score in zip(atmosphere_descriptions, similarities):
        atmosphere_scores[description] = score.item()  # `score.item()` to get a scalar value from a tensor if needed
    
    # Get the top two moods by sorting
    top_two_moods = sorted(atmosphere_scores.items(), key=lambda item: item[1], reverse=True)[:2]

    # Print the top two moods
    for mood, score in top_two_moods:
        if score > 0.1:
            return mood 


