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


track_id = []
track_name = []
artist_name = []
artist_genres = []

def appendData(varList, varData):
    if varData is None:
        varList.append('')
    else:
        varList.append(varData)

def getArtistGenres(varArtistID):
    artist_data = sp.artist(varArtistID)
    var_artist_genres = artist_data['genres']
    appendData(artist_genres, var_artist_genres)

with open('User Data/top20userCatarine.txt', 'r', encoding='utf8') as file:
    # Read the contents of the file
    file_contents = file.read()

# Parse the JSON data into a Python object
json_data = json.loads(file_contents)


for item in json_data['items']:
    artistID = item['artists'][0]['id']
    appendData(artist_name,item['artists'][0]['name'])
    appendData(track_id,item['id'])
    appendData(track_name,item['name'])
    getArtistGenres(artistID)


# Generating Dataframe with Pandas
a = {'track_id' : track_id, 'track_name' : track_name, 'artist_name' : artist_name, 'artist_genres' : artist_genres}

df = pd.DataFrame.from_dict(a, orient='index')

df = df.transpose()

print(df.shape)

df.to_csv('User Data/userdataCatarine.csv', encoding='utf-8')

