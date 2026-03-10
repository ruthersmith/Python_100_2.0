"""
Spotify Time Machine

A program that allows users to travel back in time musically by generating
a youtube playlist based on the top songs from a specific historical date.

The user provides a date, and the program retrieves the chart data for
that date, extracts the list of top songs, and automatically creates a
Spotify playlist containing those tracks.

Previous Version:
An earlier version of this project scraped the Billboard Hot 100 charts
to obtain the list of songs. However, the Billboard charts are now behind
a paywall, making automated access difficult without a paid subscription.

The original implementation also used the Spotify API to create playlists.
However, Spotify now requires a Premium account for certain API
operations, so this version uses the YouTube  API instead.

Current Version:
This updated version retrieves chart data from the UK Official Charts
website instead:
https://www.officialcharts.com/charts/singles-chart/

Workflow:
1. User enters a date
2. Chart songs are scraped from Official Charts
3. A playlist is created
4. Each song is searched on YouTube
5. Videos are added to the playlist

The application is implemented as a single-file program containing the
`SpotifyTimeMachine` class, which coordinates chart retrieval,
Spotify authentication, and playlist creation.
"""

import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic


class SpotifyTimeMachine:

    def __init__(self):
        self.ytmusic = YTMusic('browser_auth.json')


    def get_chart_songs(self, date: str):
        """
            Retrieves the top songs for a given date from the UK Official Charts website.

            Parameters:
                date (str): Date in the format YYYYMMDD.

            Returns:
                list[dict]: A list of songs with title and artist information.
        """

        url = f"https://www.officialcharts.com/charts/singles-chart/{date}/"

        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        songs = []

        entries = soup.select("div.chart-item-content")

        for entry in entries:
       
            title = entry.select_one(".chart-name").get_text(strip=True)
            artist = entry.select_one(".chart-artist").get_text(strip=True)

            songs.append({
                "title": title,
                "artist": artist
            })

        return songs

    
    def create_playlist(self, date: str):
        """
        Creates a playlist for the given date if one does not already exist.
        If a playlist with the same name exists, its ID is returned instead.

        Parameters:
            date (str): Date used to generate the playlist.

        Returns:
            str: The ID of the newly created playlist.
        """
        title = f"Top Songs from {date}"
        description = f"Generated playlist of chart songs from {date}"

        playlists = self.ytmusic.get_library_playlists()
        for playlist in playlists:
            if playlist["title"] == title:
                print("Playlist already exists, using existing playlist.")
                return playlist["playlistId"]

        print("Creating Playlist...")
        playlist_id = self.ytmusic.create_playlist(
            title,
            description
        )

        return playlist_id

    
    def search_youtube_video(self, title: str, artist: str):
        """
        Searches YouTube Music for the given song and returns the video ID.

        Parameters:
            title (str): Song title
            artist (str): Song artist

        Returns:
            str | None: The video ID if found, otherwise None.
        """

        query = f"{title} {artist}"

        results = self.ytmusic.search(query, filter="songs")

        if not results:
            return None

        song = results[0]

        return song["videoId"]

            
    def add_songs_to_playlist(self, playlist_id: str, video_ids: list):
        """
        Adds a song to a YouTube Music playlist.

        Parameters:
            playlist_id (str): The playlist to add the song to.
            video_id (list): List containing The video ID of the song to add to the playlist
        """

        self.ytmusic.add_playlist_items(playlist_id, videoIds=video_ids)


    def run(self, date : str):
        """
        Entry point for the functionality of the SpotifyTimeMachine class
        :param date: The date in the format (YYYYMMDD)
    
            """
        print("Getting Playlist Ready...")
        playlist_id = self.create_playlist(date)
        
        print("Getting songs from the Chart")
        song_list = self.get_chart_songs(date)

        print("Adding Songs to Playlist")
        for song in song_list:
            print(f"Searching for Song {song['title']} by {song['artist']}")
            video_id = self.search_youtube_video(title=song['title'], artist=song['artist'])
            print(f"Found video ID {video_id}")

            try:
                self.add_songs_to_playlist(playlist_id=playlist_id, video_ids=[video_id])
            except  Exception as e:
                print(f"Failed to add {video_id} for  {song['title']} by {song['artist']} : {e}")
                print('-------------------------------------')


if __name__ == '__main__':
    date_to_use = input("Enter date in format (YYYYMMDD): ")
    print("Using " + date_to_use)
    time_machine = SpotifyTimeMachine()
    time_machine.run(date=date_to_use)
