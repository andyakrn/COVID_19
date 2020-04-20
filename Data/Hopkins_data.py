#!/usr/bin/env python
# coding: utf-8

# <h2><center>
#     Loading In Data
#     </center></h2>

# In[1]:


from github import Github
import os
import pickle
import base64
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# In[2]:


with open("/Users/christyliner/Documents/COVID_19/Data/github.txt") as myfile:
    firstNlines=myfile.readlines()[0:2]
myfile.close()
g = Github(firstNlines[0].strip(), firstNlines[1])


# In[3]:


repo=g.get_repo('CSSEGISandData/COVID-19')
contents = repo.get_contents("")


# In[4]:


def get_sha_for_tag(repository, tag):
    branches = repository.get_branches()
    matched_branches = [match for match in branches if match.name == tag]
    if matched_branches:
        return matched_branches[0].commit.sha

    tags = repository.get_tags()
    matched_tags = [match for match in tags if match.name == tag]
    if not matched_tags:
        raise ValueError('No Tag or Branch exists with that name')
    return matched_tags[0].commit.sha


# In[5]:


def download_directory(repository, sha, server_path, local_path='data_csse/'):
    contents = repository.get_contents(server_path, ref=sha)
    if not os.path.exists(local_path):
        os.makedirs(local_path)
    for content in contents:
        if content.type == 'dir':
            download_directory(repository, sha, content.path)
        else:
            try:
                path = content.path
                file_content = repository.get_contents(path, ref=sha)
                file_data = base64.b64decode(file_content.content).decode('ascii')
                file_out = open(local_path+content.name, "w")
                file_out.write(local_path+file_data)
                file_out.close()
            except:
                pass


# In[6]:


sha = get_sha_for_tag(repo, 'master')


# In[7]:


download_directory(repo, sha, 'csse_covid_19_data/csse_covid_19_time_series/')


# In[8]:


from os import listdir
from os.path import isfile, join
mypath = 'data_csse/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# In[9]:


def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


# In[10]:


timeseries_files = []
for file in onlyfiles:
    if is_non_zero_file(mypath + file) and file[:19]=='time_series_covid19':
        timeseries_files.append(mypath + file)


# In[11]:


def preprocess_df(df, name):
    df.drop(columns=['data_csse/Province/State', 'Lat', 'Long'], inplace=True)
    df = df.groupby(['Country/Region']).agg('sum')
    df = df.transpose().reset_index()
    country_list = list(df.columns)[1:]
    df = pd.melt(df, id_vars='index', value_vars=country_list)
    df = df.rename(columns={'index':'Date', 'value':name})
    return df


# In[12]:


confirmed_df = pd.read_csv('data_csse/time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('data_csse/time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('data_csse/time_series_covid19_recovered_global.csv')


# In[13]:


confirmed_df = preprocess_df(confirmed_df, 'Confirmed')
deaths_df = preprocess_df(deaths_df, 'Deaths')
recovered_df = preprocess_df(recovered_df, 'Recovered')


# <h2><center>
#     Preprocessing Data
#     </center></h2>

# In[14]:


confirmed_and_deaths = pd.merge(confirmed_df, deaths_df, how='inner', on=['Date', 'Country/Region'])


# In[15]:


grouped_df = pd.merge(confirmed_and_deaths, recovered_df, how='inner', on=['Date', 'Country/Region'])


# In[16]:


grouped_df['Active'] = grouped_df['Confirmed']-grouped_df['Deaths']-grouped_df['Recovered']


# In[17]:


grouped_df['Datetime'] = grouped_df['Date'].apply(lambda x: pd.to_datetime(x))


# In[18]:


pop_df = pd.read_csv('/Users/christyliner/Documents/COVID_19/Data/pop_df4.csv')


# In[19]:


pop_df['Country/Region'] = pop_df['Country/Region'].apply(lambda x: x.replace('Mainland China', 'China'))


# In[20]:


pop_df.drop(columns=['Unnamed: 0'], inplace=True)


# In[21]:


grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Mainland China', 'China')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Hong Kong SAR', 'Hong Kong')
grouped_df['Country/Region'] = grouped_df['Country/Region'].replace(['Korea, South', 'Republic of Korea'], 'South Korea')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('United Kingdom', 'UK')
grouped_df['Country/Region'] = grouped_df['Country/Region'].replace(['Taiwan*', 'Taipei and environs'], 'Taiwan')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Iran (Islamic Republic of)', 'Iran')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Viet Nam', 'Vietnam')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Macao SAR', 'Macau')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Republic of Ireland', 'Ireland')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Czechia', 'Czech Republic')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('occupied Palestinian territory', 'Palestine')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Russian Federation', 'Russia')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace(' Azerbaijan', 'Azerbaijan')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Holy See', 'Vatican City')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Republic of Moldova', 'Moldova')
grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('Saint Martin', 'St. Martin')


# In[22]:


grouped_df = pd.merge(grouped_df, pop_df, on='Country/Region')


# In[23]:


grouped_df['Confirmed Cases Per 1M'] = grouped_df['Confirmed']*1000/grouped_df['PopTotal']


# In[24]:


grouped_df['Country/Region'] = grouped_df['Country/Region'].str.replace('US', 'United States')


# In[25]:


grouped_df['New Weekly Cases'] = np.where(grouped_df['Country/Region']==grouped_df['Country/Region'].shift(7),
                                          grouped_df['Confirmed']-grouped_df['Confirmed'].shift(7),grouped_df['Confirmed'])


# <h2><center>
#     Export Dataframe
#     </center></h2>

# In[26]:


pickle_out = open('/Users/christyliner/Documents/COVID_19/Data/COVID_Hopkins_df.pickle', 'wb')
pickle.dump(grouped_df, pickle_out)
pickle_out.close()

