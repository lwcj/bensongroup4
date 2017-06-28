import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv('http://web.mta.info/developers/data/nyct/subway/Stations.csv')

subset = df[['Line', 'Stop Name', 'GTFS Latitude', 'GTFS Longitude']]
subset2 = subset[(subset['GTFS Latitude'] >= 40.731191) &
                     (subset['GTFS Latitude'] <= 40.753512) &
                     (subset['GTFS Longitude'] >= -74.001387) &
                     (subset['GTFS Longitude'] <= -73.977641)]
# subset3 = subset2.drop_duplicates('Stop Name')

with open('subset2.pkl', 'wb') as f:
    pickle.dump(subset2, f)
