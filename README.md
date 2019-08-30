# Statify
Statify displays the user's top artists and tracks for various time frames, and generates a playlist of recommended tracks which can be saved to the user's playlists.

## Prerequisites:
1. <a href='https://www.python.org/downloads/'>Python 3.6</a>
2. <a href="http://spotipy.readthedocs.io/en/latest/">Spotipy</a>, a Python library for the <a href="https://developer.spotify.com/documentation/web-api/">Spotify Web API</a>. You can do so with <code>pip install spotipy</code>.
3. API Keys from <a href="https://developer.spotify.com">Spotify for developers</a>.
4. Set appropriate environment variables (<code>SPOTIPY_CLIENT_ID</code>, <code>SPOTIPY_CLIENT_SECRET</code>, <code>SPOTIPY_REDIRECT_URI</code>).

## Usage:  
1. Use the application by calling <code>python statify.py <your_spotify_username></code>
2. Follow instructions in terminal.

## Getting a Spotify API Key:
1. Visit <a href='https://developer.spotify.com/dashboard/applications'>Spotify for developers</a>.
2. Create a new app.
3. Find **Client ID** and **Client Secret**.

## Sample Result
![Result](https://raw.githubusercontent.com/raghavverma2/Statify/master/result.png)
