from appfiles.imports import *
import pandas as pd

#pickle_in = open('COVID_Hopkins_df.pickle', 'rb')
#grouped_df = pickle.load(pickle_in)
grouped_df = pd.read_pickle('COVID_Hopkins_df.pickle')
df_pdv_1_0_1.pickle