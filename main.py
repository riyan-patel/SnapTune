import streamlit as st
from compute_face_exp import compute_face_exp
from compute_color import compute_color
from compute_caption import compute_caption
from compute_mood import compute_mood
from attributeCalculator import calculate_music_attributes
from filter import filter
from lyrics import lyrics
from artwork import get_album_artwork
import os


def process_image_and_analyze(image_path):
    # Check if the image exists
    if not os.path.exists(image_path):
        return f"File does not exist at: {image_path}"

    # Face expression analysis
    face_count, dominant_emotion = compute_face_exp(image_path)
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

    attribute_caluation = calculate_music_attributes(image_path)
    print(attribute_caluation)
    st.write(attribute_caluation)

    # title_array, artist_array, artwork_array = filter(image_path)
    # st.header("Recommended Tracks")

    # for title, artist, artwork in zip(title_array, artist_array, artwork_array):
    #     # Create two columns
    #     col1, col2 = st.columns([3, 1])  # Adjust column width ratio as needed
        
    #     with col1:
    #         st.subheader(title)
    #         st.write(f"Artist: {artist}")
        
    #     with col2:
    #         st.image(artwork, caption=title, use_column_width=True)

    songs = lyrics(image_path)
    for song in songs:
        col1, col2 = st.columns([1, 3])
        image,artist = get_album_artwork(song)
        with col1:
            st.image(image, caption=song, use_column_width=True)
        with col2:
            st.subheader(song)
            st.write(f"Artist: {artist}")
        

    

    return {
        # "face_count": face_count,
        # "dominant_emotion": dominant_emotion,
        # "top_two_moods": top_two_moods,
        # "caption": caption,
        # "color_results": color_results,
        # "attribute_caluation": attribute_caluation
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

    # Clean up the temporary file
    os.remove(temp_file_path)
else:
    st.write("Please upload an image to analyze.")
