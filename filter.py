import requests
import base64
# Replace these with your client ID and secret
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
params = {
    "seed_genres": "pop,rock",
    "seed_artists": "4NHQUGzhtTLFvgF5SZesLK",
    "min_danceability": 0.5,
    "max_danceability": 0.8,
    "target_energy": 0.7,
    "min_tempo": 100,
    "max_tempo": 130,
    "target_valence": 0.6,
    "min_popularity": 50
}

# Send request to Search API
# Send request to Get Recommendations API

url = "https://api.spotify.com/v1/recommendations"
response = requests.get(url, headers=headers, params=params)
recommendations = response.json()
# Display recommended track names and artists
title_array = []
artist_array = []

# Loop through the first two recommended tracks
for track in recommendations["tracks"][:3]:  # Slice to get the first two tracks
    title_array.append(track["name"])  # Add track name to title_array
    artist_array.append(track["artists"][0]["name"])  # Add artist name to artist_array
print(title_array)
print(artist_array)
