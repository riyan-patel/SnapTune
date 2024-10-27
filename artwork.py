import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_album_artwork(song_title):
    client_id = "12e72de55dc441619997bfe071625bcf"
    client_secret = "0dd60f24978c431e931e62c49b88d595"
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    # Search for the song by title
    results = sp.search(q=song_title, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        album_art_url = track['album']['images'][0]['url']
        artist = track["artists"][0]["name"]  # Get the largest image URL
        return album_art_url,artist
    else:
        return "No artwork found for this title."