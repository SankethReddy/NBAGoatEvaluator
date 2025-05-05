# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')
from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from goat_evaluator_calculation import calculate_goat_evualation

server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/NBAGoatEvaluator/')

df = pd.read_csv("../raw_data/Goat Evaluator Raw Data.csv")

app.layout = html.Div([
    html.Div([
        html.H1("Build Your Model for the GOAT NBA Player")
        ], style = {'text-align': 'center'}),
    html.Div([
        html.Img(src="./assets/era-banner.png", style={'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'})
        ], style = {'text-align': 'center'}),
    html.Div([
        html.H2("1. Choose Your Era", style = {'font-weight': '600', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Is everyone in the conversation, or should older eras be viewed less favorably?", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        dcc.Slider(id='era-slider', min=1.0, max=7.0, step=0.1, value=1.0, marks={
                                                                                1: {'label': 'Plumbers'},
                                                                                2: {'label': '2.0'},
                                                                                3: {'label': '3.0'},
                                                                                4: {'label': '4.0'},
                                                                                5: {'label': '5.0'},
                                                                                6: {'label': '6.0'},
                                                                                7: {'label': 'Ballers'},
                                                                                },
                    tooltip={'always_visible': True, 'placement': 'top', 'style': {'fontsize': '100px', 'font-weight': 'bold'}})
        ]),
    html.Div([
        html.H2("2. Evaluate Performance", style = {'font-weight': '600', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("This is purely a measure of a player’s production and ability to increase the chances of winning. A win or an MVP does not influence the evaluation of a player’s performance. We don’t have the luxury of the “eye test” in this statistical assessment, so choose which numbers you want to consider.", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        dcc.Slider(id='regular-season-postseason-slider', min = 0, max = 100, step = 1, value = 50, marks = {
                                                                                                             0: {'label': 'Season'},
                                                                                                             100: {'label': 'Playoffs'}
                                                                                                             },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}}),
        html.Div(id='regular-season-postseason-slider-output-container', style = {'text-align': 'center', 'font-weight': 'bold'}),
        dcc.Slider(id='box-score-advanced-analaytics-slider', min = 0, max = 100, step = 1, value = 50, marks = {
                                                                                                             0: {'label': 'Traditional'},
                                                                                                             100: {'label': 'Advanced'}
                                                                                                             },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}}),
        html.Div(id='box-score-advanced-analaytics-slider-output-container', style = {'text-align': 'center', 'font-weight': 'bold'})
        ]),
    html.Div([
        html.H2("3. Build Your Model", style = {'font-weight': '600', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Distribute 100 points across the following criteria:", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'})
        ])
    ])


@app.callback(
    Output('regular-season-postseason-slider-output-container', 'children'),
    [Input('regular-season-postseason-slider', 'value')]
    )
def update_regular_season_postseason_output(playoffs_percentage):
    season = 100 - playoffs_percentage
    return f"Regular Season: {season}% / Playoffs: {playoffs_percentage}%"

@app.callback(
    Output('box-score-advanced-analaytics-slider-output-container', 'children'),
    [Input('box-score-advanced-analaytics-slider', 'value')]
    )
def update_box_score_advanced_analytics_output(advanced_analytics_percentage):
    box_score = 100 - advanced_analytics_percentage
    return f"Traditional Box Score: {box_score}% / Advanced Analytics: {advanced_analytics_percentage}%"



if __name__ == '__main__':
    app.run_server()