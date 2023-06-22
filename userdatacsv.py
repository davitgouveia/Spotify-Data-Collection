import spotipy
import csv
import json
import config
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
cid = config.clientIdToken
secret = config.clientSecretToken
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=
client_credentials_manager)

artist_name = []
artist_id = []
artist_genres = []
track_id = []
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
album_img = []

def appendData(varList, varData):
    if varData is None:
        varList.append('')
    else:
        varList.append(varData)

def getArtistGenres(varArtistID):
    artist_data = sp.artist(varArtistID)
    var_artist_genres = artist_data['genres']
    appendData(artist_genres, var_artist_genres)

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

def getTrack(varTrackID):
    track_result = sp.track(varTrackID)
    artistID = track_result['artists'][0]['id']
    trackID = track_result['id']
    appendData(artist_name,track_result['artists'][0]['name'])
    appendData(artist_id, track_result['artists'][0]['id'])
    appendData(track_id,track_result['id'])
    appendData(track_name,track_result['name'])
    appendData(album_name,track_result['album']['name'])
    appendData(album_img, track_result['album']['images'][1]['url'])
    appendData(popularity, track_result['popularity'])
    appendData(explicit, track_result['explicit'])
    appendData(duration_ms, track_result['duration_ms'])
    getArtistGenres(artistID)
    getTrackFeatures(trackID)

with open('User Data/userCSV/thiagoL.csv', 'r') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader, None)

    for row in csv_reader:
        track_ids = row[0]
        getTrack(track_ids)

a = {'track_id' : track_id, 'track_name' : track_name, 'artist_name' : artist_name, 'artist_genres' : artist_genres, 'album_name' : album_name, 'artist_id' : artist_id,
        'popularity' : popularity, 'duration_ms' : duration_ms, 'explicit' : explicit, 'danceability' : danceability,
        'energy' : energy, 'key' : key, 'loudness' : loudness, 'mode' : mode, 'speechiness' : speechiness, 'acousticness' : acousticness,
        'instrumentalness' : instrumentalness, 'liveness' : liveness, 'valence' : valence, 'tempo' : tempo, 'time_signature' : time_signature, 'album_img' : album_img}

df = pd.DataFrame.from_dict(a, orient='index')

df = df.transpose()

print(df.shape)

df.to_csv('User Data/userCSV/userResults/top20userThiagoL.csv', encoding='utf-8')