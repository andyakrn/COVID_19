import pickle
import pandas as pd

# grouped_df = pd.read_pickle('../csse_daily_reports/Data/COVID_Hopkins_df.pickle')
# us_df = pd.read_pickle('../csse_daily_reports/data/CSSE_US_df.pickle')

grouped_df = pd.read_pickle('../Data/COVID_Hopkins_df.pickle')
us_df = pd.read_pickle('../Data/CSSE_US_df.pickle')

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
import plotly.express as px
from ipywidgets import interact

from style import *
from _1header_buttons_summary import *
from _2world_map import *
from _3new_cases import *
from _4mortality import *
from _5country_comparison import *

from _6us_map import *
from _7us_new_cases import *
from _8footer import *
from world_tab import *
from us_tab import *