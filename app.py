#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from flask import Flask
from flask import request
from flask import render_template

import pandas as pd
import numpy as np
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

# importing functions
from getTrackFeatures import getTrackFeatures
from getRecommendations import getRecommendation
from filterRecommendations import getNeighbors

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

global cid, secret, client_credentials_manager, sp, new_df

cid = '7f2ab65404b64bbc99e22b2efcb17983'
secret = 'aa855c61f03f4077ac50a78fa35c71c6'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
new_df = pd.read_csv('data.csv', encoding='latin-1')


# POST the name of the song
@app.route("/rec/collab", methods=["POST"])
def rec():
    starttime = time.time()
    song = request.form.get("song")
    
    track_id = sp.search(q='track:' + song, type='track')
    id = track_id['tracks']['items'][0]['id']
    song_name = sp.track(id)['name']
    track1, track2 = getTrackFeatures(id, sp)
    
    #CONTENT BASED ------------------------------------------------------------------


    
    # #COLLABORATIVE FILTERING BASED ------------------------------------------------------------------
    tracks = []
    track2.insert(0, id)
    tracks.append(track2)
    
    record = pd.DataFrame(tracks, columns = ['id', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'year'])
    data = new_df[['id', 'popularity', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'year']]
    k=10
    nid = getNeighbors(record, data,k )
    nid.insert(0,id)
    neighbours = []
    prev = ""
        # print("Recommendations based on", col[i])
    for j in nid:
        temp = []
        track = sp.track(j)
        time.sleep(0.2)
        if(track['name']==prev):
            continue
        minutes = str(int((track['duration_ms'] / 1000) / 60))
        seconds = str(int((track['duration_ms']/ 1000) % 60))
        if(len(minutes)==1):
            minutes= '0'+minutes
        if(len(seconds)==1):
            seconds= '0'+seconds
        duration = minutes+":"+seconds

        prev = track['name']
        temp.append(str(track['album']['images'][0]['url']))
        temp.append(track['name'])
        temp.append(duration)
        temp.append(track['album']['artists'][0]['name'])
        temp.append(str(track['preview_url']))
        
        neighbours.append(temp)


    return render_template("index.html", recommendations=neighbours)

@app.route("/rec/content", methods=["POST"])
def content():
    starttime = time.time()
    song = request.form.get("song")
    
    track_id = sp.search(q='track:' + song, type='track')
    id = track_id['tracks']['items'][0]['id']
    song_name = sp.track(id)['name']
    track1, track2 = getTrackFeatures(id, sp)

    tracks = []
    print(time.time() - starttime)
    track1.insert(0, id)
    tracks.append(track1)
    
    # create record
    record = pd.DataFrame(tracks, columns = ['id', 'name', 'album', 'artist', 'release_date'])

    tid = getRecommendation(new_df, record)
    print(time.time() - starttime)

    recommendations = [] #4 list (categories)
    prev = song_name
    col = ['name', 'album', 'artist', 'release_date']
    for i in range(4):
        rec_col = []
        # print("Recommendations based on", col[i])
        for j in tid[i]:
            temp = []
            track = sp.track(j)
            time.sleep(0.2)
            if(track['name']==prev):
                continue

            minutes = str(int((track['duration_ms'] / 1000) / 60))
            seconds = str(int((track['duration_ms']/ 1000) % 60))
            if(len(minutes)==1):
                minutes= '0'+minutes
            if(len(seconds)==1):
                seconds= '0'+seconds
            duration = minutes+":"+seconds

            prev = track['name']
            temp.append(track['name'])
            temp.append(duration)
            temp.append(track['album']['artists'][0]['name'])
            temp.append(str(track['preview_url']))
            temp.append(str(track['album']['images'][0]['url']))
            
            
            rec_col.append(temp)
        recommendations.append(rec_col)
        print(time.time() - starttime)
    return render_template("index.html", recommend = recommendations , col=col)



# MAIN ROUTE ------------------------------------------------------------------------------------------------
@app.route("/", methods=['GET'])
def index():
    return render_template("index.html", msg="NRDY")


if __name__ == "__main__":
  
    app.run(debug=True)
