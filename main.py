import requests
from bs4 import BeautifulSoup
from playlist import Playlist

playlist = Playlist()
selected_date = input("Billboard top 100 on which date? (YYYY-MM-DD): ")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

base_url = "https://www.billboard.com/charts/hot-100/"

response = requests.get(f"{base_url}{selected_date}/", headers=header)

site_data = BeautifulSoup(response.text,"html.parser")

titles_data = site_data.select("li ul li h3")

titles = [data.get_text().strip() for data in titles_data]


playlist.create_playlist(name=f"{selected_date} Billboard 100", description=f"Top 100 songs from {selected_date}")

track_uri_list = [playlist.search_song(song_name=songs) for songs in titles]

playlist.add_song_to_playlist(tracks = track_uri_list)
