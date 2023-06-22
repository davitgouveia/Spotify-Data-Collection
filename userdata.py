import spotipy
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

with open('User Data/top20userCelio.txt', 'r', encoding='utf8') as file:
    # Read the contents of the file
    file_contents = file.read()

# Parse the JSON data into a Python object
json_data = json.loads(file_contents)


for item in json_data['items']:
    artistID = item['artists'][0]['id']
    trackID = item['id']
    appendData(artist_name,item['artists'][0]['name'])
    appendData(artist_id, item['artists'][0]['id'])
    appendData(track_id,item['id'])
    appendData(track_name,item['name'])
    appendData(album_name,item['album']['name'])
    appendData(album_img, item['album']['images'][1]['url'])
    appendData(popularity, item['popularity'])
    appendData(explicit, item['explicit'])
    appendData(duration_ms, item['duration_ms'])
    getArtistGenres(artistID)
    getTrackFeatures(trackID)



# Generating Dataframe with Pandas
a = {'track_id' : track_id, 'track_name' : track_name, 'artist_name' : artist_name, 'artist_genres' : artist_genres, 'album_name' : album_name, 'artist_id' : artist_id,
        'popularity' : popularity, 'duration_ms' : duration_ms, 'explicit' : explicit, 'danceability' : danceability,
        'energy' : energy, 'key' : key, 'loudness' : loudness, 'mode' : mode, 'speechiness' : speechiness, 'acousticness' : acousticness,
        'instrumentalness' : instrumentalness, 'liveness' : liveness, 'valence' : valence, 'tempo' : tempo, 'time_signature' : time_signature, 'album_img' : album_img}

df = pd.DataFrame.from_dict(a, orient='index')

df = df.transpose()

print(df.shape)

df.to_csv('User Data/userdataCelio.csv', encoding='utf-8')

