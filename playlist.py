import requests
import os
import spotipy
class Playlist:
    def __init__(self):
        self.spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
        self.spotify_secret = os.environ["SPOTIFY_SECRET"]
        self.redirect_uri = "http://127.0.0.1:8888/callback"
        self.scopes = "user-read-private user-read-email user-top-read"
        self.access_token = ""

    def get_access_token(self):
        body = {
            "response_type": 'code',
            "client_id": self.spotify_client_id,
            "redirect_uri": self.redirect_uri,
            "scopes": self.scopes
        }
        response = requests.get(url="https://accounts.spotify.com/authorize")

    def create_playlist(self):
        pass
