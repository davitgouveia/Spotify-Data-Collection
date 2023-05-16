import spotipy
import config.py
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
cid = config.py.clientIdToken
secret = config.py.clientSecretToken
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []
album_name = []
duration_ms = []
explicit = []
danceability = []
energy = []
key = []
loudness = []
mode = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []
time_signature = []


for i in range(0,10000):
    track_results = sp.search(q='year:2023', type='track', limit=50,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        album_name.append(t['album_name'])
        duration_ms.append(t['duration_ms'])
        explicit.append(t['explicit'])
        danceability.append(t['danceability'])
        energy.append(t['energy'])
        key.append(t['key'])
        loudness.append(t['loudness'])
        mode.append(t['mode'])
        speechiness.append(t['speechiness'])
        acousticness.append(t['acousticness'])
        instrumentalness.append(t['instrumentalness'])
        liveness.append(t['liveness'])
        valence.append(t['valence'])
        tempo.append(t['tempo'])
        time_signature.append(t['time_signature'])



track_dataframe = pd.DataFrame({'artist_name' : artist_name, 'track_name' : track_name, 'track_id' : track_id, 'popularity' : popularity,
                                 'album_name' : album_name, 'duration_ms' : duration_ms, 'explicit' : explicit, 'danceability' : danceability,
                                 'energy' : energy, 'key' : key, 'loudness' : loudness, 'mode' : mode, 'speechiness' : speechiness, 'acousticness' : acousticness,
                                 'instrumentalness' : instrumentalness, 'liveness' : liveness, 'valence' : valence, 'tempo' : tempo, 'time_signature' : time_signature})
print(track_dataframe.shape)
track_dataframe.head()

track_dataframe.to_csv('spotify23.csv', encoding='utf-8')
