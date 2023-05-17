import spotipy
import config
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
cid = config.clientIdToken
secret = config.clientSecretToken
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

# Creating Lists
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

def getTrackFeatures(varTrackID):
    track_features_result = sp.audio_features(tracks=['{}'.format(varTrackID)])
    for y, tf in enumerate(track_features_result):
        appendData(danceability,tf['danceability'])
        appendData(energy,tf['energy'])
        appendData(key,tf['key'])
        appendData(loudness,tf['loudness'])
        appendData(mode,tf['mode'])
        appendData(speechiness,tf['speechiness'])
        appendData(acousticness,tf['acousticness'])
        appendData(instrumentalness,tf['instrumentalness'])
        appendData(liveness,tf['liveness'])
        appendData(valence,tf['valence'])
        appendData(tempo,tf['tempo'])
        appendData(time_signature,tf['time_signature'])
    print('Got Track Features \n')

def appendData(varList, varData):
    if varData is None:
        varList.append('')
    else:
        varList.append(varData)

# Querying data from a range of tracks
i = 0
for x in range(0,1000):
    track_results = sp.search(q='year:2023', type='track', limit=1,offset=x+999)
    print('Query done \n')
    for x, t in enumerate(track_results['tracks']['items']):
        appendData(artist_name,t['artists'][0]['name'])
        appendData(track_name,t['name'])
        appendData(track_id,t['id'])
        appendData(album_name,t['album']['name'])
        appendData(popularity,t['popularity'])
        appendData(explicit,t['explicit'])
        appendData(duration_ms,t['duration_ms'])
        trackID = t['id']
        getTrackFeatures(trackID)
        i = i+1
        print('Appending track data {} \n'.format(i))

print('------------------------------ \nAll tracks appended \n')
        
# Generating Dataframe with Pandas
track_dataframe = pd.DataFrame({'track_id' : track_id, 'track_name' : track_name, 'artist_name' : artist_name, 'album_name' : album_name, 'popularity' : popularity,
                                 'duration_ms' : duration_ms, 'explicit' : explicit, 'danceability' : danceability,
                                 'energy' : energy, 'key' : key, 'loudness' : loudness, 'mode' : mode, 'speechiness' : speechiness, 'acousticness' : acousticness,
                                 'instrumentalness' : instrumentalness, 'liveness' : liveness, 'valence' : valence, 'tempo' : tempo, 'time_signature' : time_signature})
print(track_dataframe.shape)
track_dataframe.head()

track_dataframe.to_csv('spotify23-1.csv', encoding='utf-8')
