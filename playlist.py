import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Playlist:
    def __init__(self):
        self.spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
        self.spotify_secret = os.environ["SPOTIFY_SECRET"]
        self.redirect_uri = "http://127.0.0.1:8888/callback"
        self.scopes = "user-read-private user-read-email user-top-read"
        self.access_token = self.get_access_token()

    def get_access_token(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.spotify_client_id,
            client_secret=self.spotify_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scopes
        ))
        return sp
    def create_playlist(self):
        pass

    def search_song(self,song_name, **artist):
        track_name = song_name
        artist_name = artist

        if artist_name != "":
            query = f"{track_name} {artist}"
        else:
            query = {track_name}

        result = self.access_token.search(q=query, type="track", limit=1)
        if result["tracks"]["items"]:
            track = result['tracks']['items'][0]
            print("Track:", track['name'])
            print("Artist:", track['artists'][0]['name'])
            print("Spotify URI:", track['uri'])
        else:
            print("Track not found")