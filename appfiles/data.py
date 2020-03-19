from appfiles.imports import *
import pandas as pd



pickle_in = open('COVID_Hopkins_df.pickle', 'rb')
grouped_df = pickle.load(pickle_in)