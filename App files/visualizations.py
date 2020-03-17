from imports import *


# load in data file
DATA_PATH = '/Users/ChristyLiner/Documents/Corona Virus/COVID_19'
pickle_in = open(DATA_PATH + '/COVID_Hopkins_df.pickle', 'rb')
df_patient = pickle.load(pickle_in)

#border