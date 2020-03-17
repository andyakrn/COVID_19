from imports import *
import pandas as pd


DATA_PATH1 = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH1 + '/COVID_Hopkins_df.pickle', 'rb')
grouped_df = pickle.load(pickle_in)