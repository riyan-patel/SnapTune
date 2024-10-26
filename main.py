from face_exp_fer import compute_face_exp
from color_pal import compute_color
from trans_download_heic import compute_caption
from mood import compute_mood
import os

def process_image_and_analyze(image_path):
    # Check if the image exists
    if not os.path.exists(image_path):
        return f"File does not exist at: {image_path}"

    # Face expression analysis
    face_count, dominant_emotion = compute_face_exp(image_path)  # Adjust unpacking
    print(f"Detected {face_count} faces.")

    # Mood analysis
    top_two_moods = compute_mood(image_path)  # Ensure this function is not printing the caption
    print(f"Top moods: {top_two_moods}")  # Added for clarity

    # Caption generation
    caption = compute_caption(image_path)
    print("Generated Caption:", caption)

    # Color analysis
    color_results = compute_color(image_path)
    print(color_results)

    return {
        "face_count": face_count,
        "dominant_emotion": dominant_emotion,
        "top_two_moods": top_two_moods,
        "caption": caption,
        "color_results": color_results,
    }

# Example usage:
if __name__ == "__main__":
    image_path = "/Users/daanish/Downloads/party.jpeg"  # Update the path as needed
    results = process_image_and_analyze(image_path)
