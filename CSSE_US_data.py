#!/usr/bin/env python
# coding: utf-8

# <h2><center>
#     Loading In Data
#     </center></h2>

# In[122]:


from github import Github
import os
import pickle
import base64
import pandas as pd
import datetime as dt
from os import listdir
from os.path import isfile, join
import numpy as np
mypath = 'data_csse/'


# In[123]:


with open("data/github.txt") as myfile:
    firstNlines=myfile.readlines()[0:2]
myfile.close()
g = Github(firstNlines[0].strip(), firstNlines[1])
repo=g.get_repo('CSSEGISandData/COVID-19')
contents = repo.get_contents("")


# In[124]:


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


# In[125]:


def download_directory(repository, sha, server_path, local_path=mypath):
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


# In[126]:


def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


# In[127]:


df_states_codes = pd.read_csv('https://raw.githubusercontent.com/jasonong/List-of-US-States/master/states.csv')
df_states_codes=df_states_codes.rename(columns={'Abbreviation':'State_code'})
df_states_codes=df_states_codes.set_index('State')
state_dict= df_states_codes.to_dict()['State_code']


# In[128]:


def preprocess_df(df1, name):
    df=df1.copy()
    df=df.loc[df['iso2']=='US']
    columns_drop= ['data_csse/UID','iso2', 'iso3', 'code3', 'FIPS', 'Admin2',
                   'Country_Region', 'Lat', 'Long_', 'Combined_Key']
    df.drop(columns=columns_drop, inplace=True)
    if 'Population' in set(df.columns):
        df.drop(columns='Population', inplace=True)
    df = df.groupby(['Province_State']).agg('sum')
    df = df.transpose().reset_index()
    country_list = list(df.columns)[1:]
    df = pd.melt(df, id_vars='index', value_vars=country_list)
    df = df.rename(columns={'index':'Date', 'value':name, 'Province_State':'State'})
    df['State_code']=df['State'].map(state_dict)
    return df


# In[129]:


sha = get_sha_for_tag(repo, 'master')
download_directory(repo, sha, 'csse_covid_19_data/csse_covid_19_time_series/')


# In[ ]:





# In[130]:


confirmed_df_raw = pd.read_csv('data_csse/time_series_covid19_confirmed_US.csv')
deaths_df_raw = pd.read_csv('data_csse/time_series_covid19_deaths_US.csv')
#recovered_df = pd.read_csv('data_csse/time_series_covid19_recovered_global.csv')


# In[ ]:





# In[131]:


confirmed_df = preprocess_df(confirmed_df_raw, 'Confirmed')
deaths_df = preprocess_df(deaths_df_raw, 'Deaths')
#recovered_df = preprocess_df(recovered_df, 'Recovered')


# <h2><center>
#     Preprocessing Data
#     </center></h2>

# In[132]:


grouped_df = pd.merge(confirmed_df, deaths_df, how='inner', on=['Date', 'State', 'State_code'])
#grouped_df = pd.merge(confirmed_and_deaths, recovered_df, how='inner', on=['Date', 'Country/Region'])
#grouped_df['Active'] = grouped_df['Confirmed']-grouped_df['Deaths']-grouped_df['Recovered']
grouped_df['Datetime'] = grouped_df['Date'].apply(lambda x: pd.to_datetime(x))


# In[133]:


grouped_df['New_Weekly_Cases'] = np.where(grouped_df['State']==grouped_df['State'].shift(7),
                                          grouped_df['Confirmed']-grouped_df['Confirmed'].shift(7),grouped_df['Confirmed'])


# # Testing data
# 

# In[134]:


test_df = pd.read_csv('https://covidtracking.com/api/states/daily.csv')
test_df['date'] = test_df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d'))


# In[135]:


col_select = ['date', 'state','totalTestResults']
df_tst_daily = test_df[col_select]


# In[136]:


grouped_df=grouped_df.merge(df_tst_daily,
                            how='inner', 
                            left_on=['Datetime', 'State_code'], 
                            right_on=['date','state'])[['Date','Datetime',
                                                        'State','State_code',
                                                        'Confirmed','Deaths',
                                                        'New_Weekly_Cases',
                                                        'totalTestResults']]


# <h2><center>
#     Export Dataframe
#     </center></h2>

# In[137]:


grouped_df.sort_values(by='Date',inplace=True)


# In[138]:


with open('Data/CSSE_US_df.pickle', 'wb') as pickle_out:
    pickle.dump(grouped_df, pickle_out)


# In[139]:


with open('../CSSE_US_df.pickle', 'wb') as pickle_out:
    pickle.dump(grouped_df, pickle_out)


# # Plots

# In[140]:


import pandas as pd 
import plotly.express as px
from ipywidgets import interact
grouped_df = pd.read_pickle('Data/CSSE_US_df.pickle')


# In[141]:


grouped_df.sort_values(by='Datetime',inplace=True)


# In[142]:


@interact(Type=['Confirmed','Deaths','totalTestResults'])

def viz(Type):

    status = Type
    world_map_fig = px.choropleth(grouped_df,
                                        locations='State_code',
                                        locationmode='USA-states',
                                        scope='usa',
                                        color=status,
                                        hover_name='State', 
                                        title='{} by Sate Over Time<br>(Hover for State Names)'.format(status),
                                        color_continuous_scale=['green', 'yellow','orange', 'orangered', 'red'],
                                        animation_frame='Date',
                                        #range_color=[0, max_cases],
                                        template='plotly_dark')
    #world_map_fig.update_layout(font={'family': font['font'], 'color': colors['text']},
    #                                    paper_bgcolor=colors['graph_background'],
    #                                    plot_bgcolor=colors['graph_background'])


    world_map_fig.show()


# In[143]:


hardest_hit_states = list(grouped_df.groupby('State').agg('max')['Confirmed'].sort_values(ascending=False)[0:15].index)

new_log_cases = grouped_df.loc[grouped_df['State'].isin(hardest_hit_states)]
px.line(new_log_cases,
                        x='Confirmed',
                        y='New_Weekly_Cases',
                        log_x='True',
                        log_y='True',
                        template='plotly_dark',
                        color='State',
                        title='New Cases to Confirmed Cases (Log Scale)',
                        )


# In[144]:


state_list = list(grouped_df.State.unique())


# In[145]:


@interact(Type=state_list)
def viz(Type):
    state = Type
    df_state = grouped_df[grouped_df['State']==state]
    df_melt = pd.melt(df_state, id_vars =['Date'], 
                  value_vars=['Confirmed','Deaths','totalTestResults'],
                 var_name = 'Status', value_name = 'Cases')
    fig = px.line(df_melt,x='Date',y='Cases', color='Status',template='plotly_dark')
    fig.show()


# In[ ]:





# In[ ]:




