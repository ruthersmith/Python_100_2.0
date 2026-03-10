# SpotifyTimeMachine

**Project:** SpotifyTimeMachine — YouTube Music Playlist Generator

This project is an updated version of an earlier project that used the Billboard Top 100 to create a Spotify playlist for a user-specified date. Due to changes on the Billboard website and Spotify requiring premium accounts, this version now:

- Scrapes the **UK Official Charts Top 100** for a given date using `requests` and `BeautifulSoup`.
- Uses **YouTube Music** via `ytmusicapi` to create playlists with the top songs.
- Uses **browser authentication** for YouTube Music (`browser_auth.json`).

---

## Features

1. Enter a date to get the Top 100 singles chart for that day.
2. Search each song on YouTube Music using `ytmusicapi`.
3. Create a new playlist in your YouTube Music account or reuse an existing one.
4. Add all found songs to the playlist, skipping songs that could not be found or duplicates.

---

## Dependencies

Install the following Python packages:

```bash
pip install requests beautifulsoup4 ytmusicapi
```

- requests — for fetching HTML from the chart website
- beautifulsoup4 — for parsing the HTML and extracting songs
- ytmusicapi — for creating and updating YouTube Music playlists

## YouTube Music Authentication

This project uses browser authentication. <br>
Follow the instructions in the ytmusicapi (https://ytmusicapi.readthedocs.io/en/stable/setup/browser.html) to see How to export your request headers in a file named
`browser.json`. Included is a browser.dist.json file that can be used as a template.

## How to run

`python main.py` <br>
When prompted, Enter a date in the format YYYYMMDD. The program will:<br>

- create (if it doesn't exist) a playlist named Top Songs from {date}
- scrapes the chart
- searches songs
- and adds songs to the playlist

## Notes

- This project references the earlier SpotifyTimeMachine that relied on Spotify and Billboard. Due to API changes and paywalls, this version now uses YouTube Music and the UK Official Charts. The earlier version can be found at https://github.com/ruthersmith/python_100/tree/master/day_46_spotify_time_machine

- Playlist names are unique per date. If a playlist with the same name exists, it will reuse it instead of creating a duplicate.

- Make sure browser.json is valid and up to date; expired headers will cause authentication errors.
