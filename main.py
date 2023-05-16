import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = 'Your Client ID'
secret = 'Your Secret ID'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)