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

# Script Workflow: 
# 1- Searches for artists and save their ID
# 2- Search for artists top tracks and append them
# 3- Query further information from trackes appended

# Creating Lists
artist_name = []
artist_id = []
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

def getTopTracks(varArtistID,varArtistName):
    toptracks_search = sp.artist_top_tracks(varArtistID, country='BR')
    for z, tp in enumerate(toptracks_search['tracks']):
        appendData(artist_name,varArtistName)
        appendData(artist_id,varArtistID)
        appendData(track_id,tp['id'])
        appendData(track_name,tp['name'])
        appendData(album_name,tp['album']['name'])
        appendData(popularity,tp['popularity'])
        appendData(explicit,tp['explicit'])
        appendData(duration_ms,tp['duration_ms'])
        trackID = tp['id']
        getTrackFeatures(trackID)

def getTrackFeatures(varTrackID):
    track_features_result = sp.audio_features(tracks=['{}'.format(varTrackID)])
    for w, tf in enumerate(track_features_result):
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


# Querying data from artists
# Set how much data will be collected in the for loop range. 
# Eg. a range of 100 means 1000 tracks.
i = 0
for x in range(0,2):
    i = i + 1
    print(i)
    artist_search = sp.search(q='year:2023', type='artist', limit=1, market='BR', offset=x)
    print('Query done \n')
    for y, a in enumerate(artist_search['artists']['items']):
        appendData(artist_name,a['name'])
        artistName = a['name']
        appendData(artist_id,a['id'])
        artistID = a['id']
        getTopTracks(artistID,artistName)

print('------------------------------ \nAll tracks appended \n')
        
# Generating Dataframe with Pandas
a = {'track_id' : track_id, 'track_name' : track_name, 'artist_name' : artist_name, 'album_name' : album_name, 'artist_id' : artist_id,
    'popularity' : popularity, 'duration_ms' : duration_ms, 'explicit' : explicit, 'danceability' : danceability,
    'energy' : energy, 'key' : key, 'loudness' : loudness, 'mode' : mode, 'speechiness' : speechiness, 'acousticness' : acousticness,
    'instrumentalness' : instrumentalness, 'liveness' : liveness, 'valence' : valence, 'tempo' : tempo, 'time_signature' : time_signature}

df = pd.DataFrame.from_dict(a, orient='index')

df = df.transpose()

print(df.shape)

df.to_csv('spotify23-final-16.csv', encoding='utf-8')
