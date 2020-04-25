import pickle
import pandas as pd

# grouped_df = pd.read_pickle('../csse_daily_reports/Data/COVID_Hopkins_df.pickle')
# us_df = pd.read_pickle('../csse_daily_reports/data/CSSE_US_df.pickle')

grouped_df = pd.read_pickle('Data/COVID_Hopkins_df.pickle')
us_df = pd.read_pickle('Data/CSSE_US_df.pickle')

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
import plotly.express as px
from ipywidgets import interact

from App_files.style import *
from App_files._1header_buttons_summary import *
from App_files._2world_map import *
from App_files._3new_cases import *
from App_files._4mortality import *
from App_files._5country_comparison import *

from App_files._6us_map import *
from App_files._7us_new_cases import *
from App_files._8footer import *
from App_files.world_tab import *
from App_files.us_tab import *