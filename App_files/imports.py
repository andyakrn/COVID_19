import pickle
import pandas as pd

grouped_df = pd.read_pickle('../COVID_19/Data/COVID_Hopkins_df.pickle')

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
from _3confirmed_active_graphs import *
from _4total_and_cases_per_million import *
from _5country_comparison import *
from _6new_cases import *
