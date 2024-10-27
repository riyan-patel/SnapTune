import requests
import base64
from attributeCalculator import calculate_music_attributes
# Replace these with your client ID and secret
def filter (image_path):
    client_id = "12e72de55dc441619997bfe071625bcf"
    client_secret = "0dd60f24978c431e931e62c49b88d595"

    # Get token
    auth_url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(auth_url, headers=headers, data=data)
    token = response.json().get("access_token")

    # Define headers and parameters
    headers = {
        "Authorization": f"Bearer {token}"
    }

    attributes = calculate_music_attributes(image_path)
    print(attributes["energyRange"][1])
    params = {
        "seed_genres": 'rock,pop',
        "min_danceability": attributes["danceabilityRange"][0],
        "max_danceability": attributes["danceabilityRange"][1],
        "min_energy": attributes["energyRange"][0],
        "max_energy": attributes["energyRange"][1],
        # "min_tempo": attributes["tempoRange"][0],
        # "max_tempo": attributes["tempoRange"][1],
        "min_valence": attributes["valenceRange"][0],
        "max_valence": attributes["valenceRange"][1]
    }

    # Send request to Search API
    # Send request to Get Recommendations API
    print("params",params)
    url = "https://api.spotify.com/v1/recommendations"
    response = requests.get(url, headers=headers, params=params)
    recommendations = response.json()
    
    # Display recommended track names and artists
    title_array = []
    artist_array = []
    artwork_array = []

    # Loop through the first two recommended tracks
    for track in recommendations["tracks"][:20]:  # Slice to get the first two tracks
        title_array.append(track["name"])  # Add track name to title_array
        artist_array.append(track["artists"][0]["name"]) 
        artwork_array.append(track["album"]['images'][0]["url"]) # Add artist name to artist_array
    return title_array, artist_array, artwork_array
