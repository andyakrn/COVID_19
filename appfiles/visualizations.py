from appfiles.imports import *


# load in data file

pickle_in = open('COVID_Hopkins_df.pickle', 'rb')
df_patient = pickle.load(pickle_in)

