import pandas as pd

grouped_df = pd.read_pickle('data/COVID_Hopkins_df.pickle')

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
from App_files._3confirmed_active_graphs import *
from App_files._4total_and_cases_per_million import *
from App_files._5country_comparison import *
from App_files._6new_cases import *
