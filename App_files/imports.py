import pickle
import pandas as pd

grouped_df = pd.read_pickle('../Data/COVID_Hopkins_df.pickle')

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
# from _3confirmed_active_graphs import *
# from _4total_and_cases_per_million import *
from _5new_cases import *
from _6country_comparison import *
from _7footer import *
from world_tab import *
from us_tab import *