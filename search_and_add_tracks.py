import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace with your own Client ID, Client Secret, and Redirect URI
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'

# Set up authentication with updated scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-public playlist-modify-private"))

def add_song_to_playlist(playlist_id, song_name, artist_name):
    # Search for the song
    results = sp.search(q=f"track:{song_name} artist:{artist_name}", type="track", limit=1)
    
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        # Add the song to the playlist
        sp.playlist_add_items(playlist_id, [track_uri])
        print(f"Added {song_name} by {artist_name} to the playlist.")
    else:
        print(f"Could not find {song_name} by {artist_name}.")

# Replace with your playlist ID
playlist_id = 'your_playlist_id'

# Main loop
while True:
    song_name = input("Enter song name (or 'quit' to exit): ")
    if song_name.lower() == 'quit':
        break
    artist_name = input("Enter artist name: ")
    add_song_to_playlist(playlist_id, song_name, artist_name)

print("Script finished.")
