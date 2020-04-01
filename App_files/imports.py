import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from ipywidgets import interact
import pickle


from dash.dependencies import Input, Output, State
import plotly.express as px
from style import *
from header_buttons_summary import *
from data import *
from world_map import *
from graphs import *
from user_input import *
from new_cases import *

from total_and_cases_per_million import *
import pickle
