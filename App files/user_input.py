from imports import *

app=dash.Dash()
user_age = dcc.Input(
            id="age",
            type="number",
            debounce=True, 
            placeholder="Please enter your age")
user_gender = dcc.Dropdown(
            id="gender", 
            options = [
                {'label': 'Male', 'value' : 'male' },
                {'label' : 'Female', 'value' : 'female'},
                {'label' : 'I prefer not to specify', 'value' : 'person'}],
            placeholder = 'Please select your gender')
user_health = dcc.Input(
            id="pre_cond",
            type="number",
            debounce=True, 
            placeholder="Number of pre-existing health conditions")