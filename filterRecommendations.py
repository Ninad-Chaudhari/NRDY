import numpy as np
from sklearn.preprocessing import MinMaxScaler

def euclid(a, b):
  distance = np.linalg.norm(a - b)
  return distance

def getNeighbors(record, data, K):
    distances = []
    for i in range(data.shape[0]):
      if data.iloc[i,0] != record.iloc[0,0]:
        dist = euclid(record.iloc[0, 1:].values, data.iloc[i, 1:].values)
        distances.append((data.iloc[i,0], dist))

    distances.sort(key=lambda x : x[1])
    neighbors = []
    for x in range(K):
        neighbors.append(distances[x][0])
    return neighbors
