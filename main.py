import streamlit as st
from face_exp import compute_face_exp
from color import compute_color
from caption import compute_caption
from mood import compute_mood
import os

def process_image_and_analyze(image_path):
    # Check if the image exists
    if not os.path.exists(image_path):
        return f"File does not exist at: {image_path}"

    # Face expression analysis
    face_count, dominant_emotion = compute_face_exp(image_path)
    st.write(f"Detected {face_count} faces.")
    st.write(f"Dominant Emotion: {dominant_emotion}")

    # Mood analysis
    top_two_moods = compute_mood(image_path)
    st.write(f"Top moods: {top_two_moods}")

    # Caption generation
    caption = compute_caption(image_path)
    st.write("Generated Caption:", caption)

    # Color analysis
    color_results = compute_color(image_path)
    st.write(color_results)

    return {
        "face_count": face_count,
        "dominant_emotion": dominant_emotion,
        "top_two_moods": top_two_moods,
        "caption": caption,
        "color_results": color_results,
    }

# Streamlit app
st.title("SnapTune")

# Allow user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "heic"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Perform the analysis
    st.write("Analyzing the uploaded image...")
    results = process_image_and_analyze(temp_file_path)

    # Display the results
    st.write("Analysis Results:")
    st.json(results)

    # Clean up the temporary file
    os.remove(temp_file_path)
else:
    st.write("Please upload an image to analyze.")
