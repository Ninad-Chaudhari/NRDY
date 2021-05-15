import pandas as pd
import numpy as np

# GET TRACK FEATURES ------------------------------------------------------------------------------------------
def getTrackFeatures(id, sp):
  meta = sp.track(id)
  features = sp.audio_features(id)
  # meta
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  duration_ms = meta['duration_ms']
  popularity = meta['popularity']

  #year
  try:
    year = int(release_date[:4])
    if(year<1900 and year>2021):
      year = 0
  except:
    year = 0

  # features
  if 'acousticness' in features[0]:
    acousticness = features[0]['acousticness']
  else: 
    acousticness = 0 
  danceability = features[0]['danceability'] if features[0]['danceability']!=None else 0
  energy = features[0]['energy'] if features[0]['energy']!=None else 0
  instrumentalness = features[0]['instrumentalness'] if features[0]['instrumentalness']!=None else 0
  liveness = features[0]['liveness'] if features[0]['liveness']!=None else 0
  loudness = features[0]['loudness'] if features[0]['loudness']!=None else 0
  speechiness = features[0]['speechiness'] if features[0]['speechiness']!=None else 0 
  tempo = features[0]['tempo'] if features[0]['tempo']!=None else 0

  track = [name, album, artist, release_date]
  track2 = [ popularity, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, year]
  return track, track2
