import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Playlist:
    def __init__(self):
        self.spotify_client_id = os.environ["SPOTIFY_CLIENT_ID"]
        self.spotify_secret = os.environ["SPOTIFY_SECRET"]
        self.redirect_uri = "http://127.0.0.1:8888/callback"
        self.scopes = "user-read-private user-read-email user-top-read playlist-modify-public"
        self.access_token = self.get_access_token()
        self.spotify_user = self.get_user_id()
        self.playlist_id = ""


    def get_access_token(self):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.spotify_client_id,
            client_secret=self.spotify_secret,
            redirect_uri=self.redirect_uri,
            scope=self.scopes
        ))
        return sp

    def get_user_id(self):
        user_info = self.access_token.current_user()
        return user_info["id"]

    def create_playlist(self, name, description="N/A"):
        playlist_name = name
        user = self.spotify_user
        playlist_desc = description

        result = self.access_token.user_playlist_create(user=user,name=name,public=True, collaborative=False,
                                                        description=playlist_desc)
        self.playlist_id = result["id"]
        print(f"Playlist Created! ID: {self.playlist_id}")

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
            return track['uri']
        else:
            print("Track not found")
            return None

    def add_song_to_playlist(self,tracks):
        result = self.access_token.playlist_add_items(playlist_id=self.playlist_id,items=tracks,position=None)
        print(f"List is added to playlist")