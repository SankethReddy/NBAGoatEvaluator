# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')
from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import pandas as pd
from goat_evaluator_calculation import calculate_goat_evualation

server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/NBAGoatEvaluator/')

app.layout = html.Div([
    html.Div([
        html.H1("Build Your Model for the GOAT NBA Player")
        ], style = {'text-align': 'center'}),
    html.Div([
        html.Img(src="./assets/era-banner.png", style={'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'})
        ], style = {'text-align': 'center'}),
    html.Div([
        html.H2("1. Choose Your Era", style = {'font-weight': '600', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Is everyone in the conversation, or should older eras be viewed less favorably?", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'})
        ]),
    html.Div([
        dcc.Slider(id='era-slider', className='era-slider-class', min=1.0, max=7.0, step=0.1, value=1.0, marks={
                                                                                                                1: {'label': "Plumbers"},
                                                                                                                2: {'label': '2.0'},
                                                                                                                3: {'label': '3.0'},
                                                                                                                4: {'label': '4.0'},
                                                                                                                5: {'label': '5.0'},
                                                                                                                6: {'label': '6.0'},
                                                                                                                7: {'label': "Ballers"},
                                                                                                                },
                    tooltip={'always_visible': False, 'placement': 'top', 'style': {'fontsize': '100px', 'font-weight': 'bold'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div(id='era-slider-output-container', style = {'text-align': 'center', 'font-weight': 'bold'}),
    html.Div([
        html.H2("2. Evaluate Performance", style = {'font-weight': '600', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("This is purely a measure of a player’s production and ability to increase the chances of winning. A win or an MVP does not influence the evaluation of a player’s performance. We don’t have the luxury of the “eye test” in this statistical assessment, so choose which numbers you want to consider.", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'})
        ]),
    html.Div([
        dcc.Slider(id='regular-season-postseason-slider', className='regular-season-postseason-slider-class', min = 0, max = 100, step = 1, value = 50, marks = {
                                                                                                                                                                 0: {'label': "Regular Season"},
                                                                                                                                                                 10: {'label': '10'},
                                                                                                                                                                 20: {'label': '20'},
                                                                                                                                                                 30: {'label': '30'},
                                                                                                                                                                 40: {'label': '40'},
                                                                                                                                                                 50: {'label': '50'},
                                                                                                                                                                 60: {'label': '60'},
                                                                                                                                                                 70: {'label': '70'},
                                                                                                                                                                 80: {'label': '80'},
                                                                                                                                                                 90: {'label': '90'},
                                                                                                                                                                 100: {'label': "Postseason"}
                                                                                                                                                                 },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div(id='regular-season-postseason-slider-output-container', style = {'text-align': 'center', 'font-weight': 'bold'}),
    html.Div([
        dcc.Slider(id='box-score-advanced-analaytics-slider', className='box-season-advanced-statistics-slider-class', min = 0, max = 100, step = 1, value = 50, marks = {
                                                                                                                                                                         0: {'label': 'Traditional Box Score'},
                                                                                                                                                                         10: {'label': '10'},
                                                                                                                                                                         20: {'label': '20'},
                                                                                                                                                                         30: {'label': '30'},
                                                                                                                                                                         40: {'label': '40'},
                                                                                                                                                                         50: {'label': '50'},
                                                                                                                                                                         60: {'label': '60'},
                                                                                                                                                                         70: {'label': '70'},
                                                                                                                                                                         80: {'label': '80'},
                                                                                                                                                                         90: {'label': '90'},
                                                                                                                                                                         100: {'label': 'Advanced Statistics'}
                                                                                                                                                                         },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div(id='box-score-advanced-analaytics-slider-output-container', style = {'text-align': 'center', 'font-weight': 'bold'}),
    html.Div([
        html.H2("3. Build Your Model", style = {'font-weight': '600', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Distribute EXACTLY 100 points across the following criteria. Once EXACTLY 100 points are distributed, the SUBMIT Button will appear on the bottom and click it to generate the results:", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'})
        ]),
    html.Div(id='total-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
    html.Div([
        html.Div(id='accolades-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Personal awards (MVPs, FMVPs, All-NBA, Scoring Titles, etc.)", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='accolades-slider', className='accolades-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                                0: {'label': '0'},
                                                                                                                                10: {'label': '10'},
                                                                                                                                20: {'label': '20'},
                                                                                                                                30: {'label': '30'},
                                                                                                                                40: {'label': '40'},
                                                                                                                                50: {'label': '50'},
                                                                                                                                60: {'label': '60'},
                                                                                                                                70: {'label': '70'},
                                                                                                                                80: {'label': '80'},
                                                                                                                                90: {'label': '90'},
                                                                                                                                100: {'label': '100'}
                                                                                                                                },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='prime-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Player performance in all the years he was at an elite level (example: Kobe Bryant 2001-2013)", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='prime-slider', className='prime-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                        0: {'label': '0'},
                                                                                                                        10: {'label': '10'},
                                                                                                                        20: {'label': '20'},
                                                                                                                        30: {'label': '30'},
                                                                                                                        40: {'label': '40'},
                                                                                                                        50: {'label': '50'},
                                                                                                                        60: {'label': '60'},
                                                                                                                        70: {'label': '70'},
                                                                                                                        80: {'label': '80'},
                                                                                                                        90: {'label': '90'},
                                                                                                                        100: {'label': '100'},
                                                                                                                        },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='peak-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Player performance in the 2-3 consecutive seasons where he was at his best (example: Kobe Bryant 2007-2009)", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='peak-slider', className='peak-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                      0: {'label': '0'},
                                                                                                                      10: {'label': '10'},
                                                                                                                      20: {'label': '20'},
                                                                                                                      30: {'label': '30'},
                                                                                                                      40: {'label': '40'},
                                                                                                                      50: {'label': '50'},
                                                                                                                      60: {'label': '60'},
                                                                                                                      70: {'label': '70'},
                                                                                                                      80: {'label': '80'},
                                                                                                                      90: {'label': '90'},
                                                                                                                      100: {'label': '100'},
                                                                                                                      },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='leaderboards-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Placement in career box score stat totals like points, rebounds, and assists", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='leaderboards-slider', className='leaderboards-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                                      0: {'label': '0'},
                                                                                                                                      10: {'label': '10'},
                                                                                                                                      20: {'label': '20'},
                                                                                                                                      30: {'label': '30'},
                                                                                                                                      40: {'label': '40'},
                                                                                                                                      50: {'label': '50'},
                                                                                                                                      60: {'label': '60'},
                                                                                                                                      70: {'label': '70'},
                                                                                                                                      80: {'label': '80'},
                                                                                                                                      90: {'label': '90'},
                                                                                                                                      100: {'label': '100'},
                                                                                                                                      },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='two-way-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Balance of elite-level offense and elite-level defenses", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='two-way-slider', className='two-way-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                            0: {'label': '0'},
                                                                                                                            10: {'label': '10'},
                                                                                                                            20: {'label': '20'},
                                                                                                                            30: {'label': '30'},
                                                                                                                            40: {'label': '40'},
                                                                                                                            50: {'label': '50'},
                                                                                                                            60: {'label': '60'},
                                                                                                                            70: {'label': '70'},
                                                                                                                            80: {'label': '80'},
                                                                                                                            90: {'label': '90'},
                                                                                                                            100: {'label': '100'},
                                                                                                                            },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='playoff-rise-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("The ability to increase performance from the regular season into the postseason", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='playoff-rise-slider', className='playoff-rise-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                                      0: {'label': '0'},
                                                                                                                                      10: {'label': '10'},
                                                                                                                                      20: {'label': '20'},
                                                                                                                                      30: {'label': '30'},
                                                                                                                                      40: {'label': '40'},
                                                                                                                                      50: {'label': '50'},
                                                                                                                                      60: {'label': '60'},
                                                                                                                                      70: {'label': '70'},
                                                                                                                                      80: {'label': '80'},
                                                                                                                                      90: {'label': '90'},
                                                                                                                                      100: {'label': '100'},
                                                                                                                                      },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='regular-season-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Team success during the regular season through the player’s prime years", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='regular-season-slider', className='regular-season-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                                          0: {'label': '0'},
                                                                                                                                          10: {'label': '10'},
                                                                                                                                          20: {'label': '20'},
                                                                                                                                          30: {'label': '30'},
                                                                                                                                          40: {'label': '40'},
                                                                                                                                          50: {'label': '50'},
                                                                                                                                          60: {'label': '60'},
                                                                                                                                          70: {'label': '70'},
                                                                                                                                          80: {'label': '80'},
                                                                                                                                          90: {'label': '90'},
                                                                                                                                          100: {'label': '100'},
                                                                                                                                          },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='postseason-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Team success in the postseason through the player’s career", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='postseason-slider', className='postseason-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                                  0: {'label': '0'},
                                                                                                                                  10: {'label': '10'},
                                                                                                                                  20: {'label': '20'},
                                                                                                                                  30: {'label': '30'},
                                                                                                                                  40: {'label': '40'},
                                                                                                                                  50: {'label': '50'},
                                                                                                                                  60: {'label': '60'},
                                                                                                                                  70: {'label': '70'},
                                                                                                                                  80: {'label': '80'},
                                                                                                                                  90: {'label': '90'},
                                                                                                                                  100: {'label': '100'},
                                                                                                                                  },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='versatility-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Ability to score in multiple ways, rebound, pass, and defend in multiple ways", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='versatility-slider', className='versatility-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                                    0: {'label': '0'},
                                                                                                                                    10: {'label': '10'},
                                                                                                                                    20: {'label': '20'},
                                                                                                                                    30: {'label': '30'},
                                                                                                                                    40: {'label': '40'},
                                                                                                                                    50: {'label': '50'},
                                                                                                                                    60: {'label': '60'},
                                                                                                                                    70: {'label': '70'},
                                                                                                                                    80: {'label': '80'},
                                                                                                                                    90: {'label': '90'},
                                                                                                                                    100: {'label': '100'},
                                                                                                                                    },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='cultural-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Influence on the sport or public", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='cultural-slider', className='cultural-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                              0: {'label': '0'},
                                                                                                                              10: {'label': '10'},
                                                                                                                              20: {'label': '20'},
                                                                                                                              30: {'label': '30'},
                                                                                                                              40: {'label': '40'},
                                                                                                                              50: {'label': '50'},
                                                                                                                              60: {'label': '60'},
                                                                                                                              70: {'label': '70'},
                                                                                                                              80: {'label': '80'},
                                                                                                                              90: {'label': '90'},
                                                                                                                              100: {'label': '100'},
                                                                                                                              },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div(id='artistry-slider-output-container', style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
        html.P("Play style that is exceptionally creative or aesthetically pleasing", style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%', 'font-size': '15px'})
        ]),
    html.Div([
        dcc.Slider(id='artistry-slider', className='artistry-slider-class', min = 0, max = 100, step = 1, value = 0, marks = {
                                                                                                                              0: {'label': '0'},
                                                                                                                              10: {'label': '10'},
                                                                                                                              20: {'label': '20'},
                                                                                                                              30: {'label': '30'},
                                                                                                                              40: {'label': '40'},
                                                                                                                              50: {'label': '50'},
                                                                                                                              60: {'label': '60'},
                                                                                                                              70: {'label': '70'},
                                                                                                                              80: {'label': '80'},
                                                                                                                              90: {'label': '90'},
                                                                                                                              100: {'label': '100'},
                                                                                                                              },
                   tooltip={'always_visible': False, 'placement': 'top', 'style': {'display': 'block', 'fontsize': '100px', 'font-weight': 'bold', 'marginLeft': 'auto', 'marginRight': 'auto'}})
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Button('SUBMIT', id='submit-button', n_clicks=0, style = {'display': 'none'})
        ], style = {'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto', 'height': '50%', 'width': '75%'}),
    html.Div([
        html.Div(id='output-content',
             children=
             [dash_table.DataTable(id='output-table', style_table={'display': 'none'})]
             )
        ], style = {'display': 'flex', 'align-items': 'center', 'justify-content': 'center'})
    ])


@app.callback(
    Output('era-slider-output-container', 'children'),
    [Input('era-slider', 'value')]
    )
def update_era_output(era):
    return f"Era: {era}"

@app.callback(
    Output('regular-season-postseason-slider-output-container', 'children'),
    [Input('regular-season-postseason-slider', 'value')]
    )
def update_regular_season_postseason_output(postseason_percentage):
    season = 100 - postseason_percentage
    return f"Regular Season: {season}% / Postseason: {postseason_percentage}%"

@app.callback(
    Output('box-score-advanced-analaytics-slider-output-container', 'children'),
    [Input('box-score-advanced-analaytics-slider', 'value')]
    )
def update_box_score_advanced_statistics_output(advanced_statistics_percentage):
    box_score = 100 - advanced_statistics_percentage
    return f"Traditional Box Score: {box_score}% / Advanced Statistics: {advanced_statistics_percentage}%"

@app.callback(
    Output('accolades-slider-output-container', 'children'),
    [Input('accolades-slider', 'value')]
    )
def update_accolades_output(accolades_value):
    return html.H4(f"Accolades: {accolades_value}")

@app.callback(
    Output('prime-slider-output-container', 'children'),
    [Input('prime-slider', 'value')]
    )
def update_prime_output(prime_value):
    return html.H4(f"Prime: {prime_value}")

@app.callback(
    Output('peak-slider-output-container', 'children'),
    [Input('peak-slider', 'value')]
    )
def update_peak_output(peak_value):
    return html.H4(f"Peak: {peak_value}")

@app.callback(
    Output('leaderboards-slider-output-container', 'children'),
    [Input('leaderboards-slider', 'value')]
    )
def update_leaderboards_output(leaderboards_value):
    return html.H4(f"Leaderboards: {leaderboards_value}")

@app.callback(
    Output('two-way-slider-output-container', 'children'),
    [Input('two-way-slider', 'value')]
    )
def update_two_way_output(two_way_value):
    return html.H4(f"Two-Way: {two_way_value}")

@app.callback(
    Output('playoff-rise-slider-output-container', 'children'),
    [Input('playoff-rise-slider', 'value')]
    )
def update_playoff_rise_output(playoff_rise_value):
    return html.H4(f"Playoff Rise: {playoff_rise_value}")

@app.callback(
    Output('regular-season-slider-output-container', 'children'),
    [Input('regular-season-slider', 'value')]
    )
def update_regular_season_output(regular_season_value):
    return html.H4(f"Regular Season Winning: {regular_season_value}")

@app.callback(
    Output('postseason-slider-output-container', 'children'),
    [Input('postseason-slider', 'value')]
    )
def update_postseason_output(postseason_value):
    return html.H4(f"Postseason Winning: {postseason_value}")

@app.callback(
    Output('versatility-slider-output-container', 'children'),
    [Input('versatility-slider', 'value')]
    )
def update_versatility_output(versatility_value):
    return html.H4(f"Versatility: {versatility_value}")

@app.callback(
    Output('cultural-slider-output-container', 'children'),
    [Input('cultural-slider', 'value')]
    )
def update_cultural_output(cultural_value):
    return html.H4(f"Cultural Impact: {cultural_value}")

@app.callback(
    Output('artistry-slider-output-container', 'children'),
    [Input('artistry-slider', 'value')]
    )
def update_artistry_output(artistry_value):
    return html.H4(f"Artistry: {artistry_value}")

@app.callback(
    [Output('total-slider-output-container', 'children'),
     Output('submit-button', 'style')],
    [Input('accolades-slider', 'value'),
     Input('prime-slider', 'value'),
     Input('peak-slider', 'value'),
     Input('leaderboards-slider', 'value'),
     Input('two-way-slider', 'value'),
     Input('playoff-rise-slider', 'value'),
     Input('regular-season-slider', 'value'),
     Input('postseason-slider', 'value'),
     Input('versatility-slider', 'value'),
     Input('cultural-slider', 'value'),
     Input('artistry-slider', 'value')]
    )
def update_total_distributed_output(accolades,prime,peak,leaderboards,two_way,playoff_rise,regular_season,postseason,versatility,cultural,artistry):
    total_points_distributed = accolades + prime + peak + leaderboards + two_way + playoff_rise + regular_season + postseason + versatility + cultural + artistry
    if total_points_distributed < 100:
        if total_points_distributed == 99:
            return [html.Div([
                        html.H4(f"Total Points Distributed: {total_points_distributed}"),
                        html.H5(f"Distribute {100- total_points_distributed} more point across the criteria", style={'color': 'red'})
                            ]),
                    {'display': 'none'}]
        else:
            return [html.Div([
                        html.H4(f"Total Points Distributed: {total_points_distributed}"),
                        html.H5(f"Distribute {100- total_points_distributed} more points across the criteria", style={'color': 'red'})
                            ]),
                    {'display': 'none'}]
    elif total_points_distributed == 100:
        return [html.Div([
                    html.H4(f"Total Points Distributed: {total_points_distributed}"),
                    html.H5("Click the SUBMIT button below to generate results", style={'color': 'green'})
                        ]),
                {'display': 'block', 'backgroundColor': '#008000', 'color': 'white', 'padding': '10px', 'border': 'none', 'cursor': 'pointer'}]
    else:
        return [html.Div([
                    html.H4(f"Total Points Distributed: {total_points_distributed}"),
                    html.H5("Exceeded the total. EXACTLY 100 points need to be distributed across the criteria so please re-distribute", style={'color': 'red'})
                        ]),
                {'display': 'none'}]


@app.callback(
    Output('output-content', 'children'),
    [Input('submit-button', 'n_clicks'),
     Input('era-slider', 'value'),
     Input('box-score-advanced-analaytics-slider', 'value'),
     Input('regular-season-postseason-slider', 'value'),
     Input('accolades-slider', 'value'),
     Input('prime-slider', 'value'),
     Input('peak-slider', 'value'),
     Input('leaderboards-slider', 'value'),
     Input('two-way-slider', 'value'),
     Input('playoff-rise-slider', 'value'),
     Input('regular-season-slider', 'value'),
     Input('postseason-slider', 'value'),
     Input('versatility-slider', 'value'),
     Input('cultural-slider', 'value'),
     Input('artistry-slider', 'value')]
    )
def update_table_output(n_clicks,era,box_score_advanced_analytics,regular_season_postseason,accolades,prime,peak,leaderboards,two_way,playoff_rise,regular_season,postseason,versatility,cultural,artistry):
    df = pd.read_csv("../raw_data/Goat Evaluator Raw Data.csv")
    changed_id_list = [p['prop_id'] for p in dash.callback_context.triggered][0]
    total_points_distributed = accolades + prime + peak + leaderboards + two_way + playoff_rise + regular_season + postseason + versatility + cultural + artistry
    if total_points_distributed != 100:
        return dash_table.DataTable(id='output-table', style_table={'display': 'none'})
    if 'submit-button' in changed_id_list:
        if prime + peak > 0:
            output_df = calculate_goat_evualation(df,era,(100-box_score_advanced_analytics)/100,box_score_advanced_analytics/100,(100-regular_season_postseason)/100,regular_season_postseason/100,accolades,prime,peak,
                                                   (prime)/(prime+peak),(peak)/(prime+peak),leaderboards,two_way,playoff_rise,regular_season,postseason,versatility,cultural,artistry)
        else:
            output_df = calculate_goat_evualation(df,era,(100-box_score_advanced_analytics)/100,box_score_advanced_analytics/100,(100-regular_season_postseason)/100,regular_season_postseason/100,accolades,prime,peak,
                                                   0,0,leaderboards,two_way,playoff_rise,regular_season,postseason,versatility,cultural,artistry)
        return dash_table.DataTable(id='output-table',
                                    data = output_df.to_dict('records'),
                                    columns = [{'name': col, 'id': col} for col in output_df.columns],
                                    style_table = {'display': 'block'},
                                    style_header={'font-weight': 'bold', 'backgroundColor': '#eee', 'color': '#900'},
                                    style_data={'color': 'black', 'background-color': 'white'},
                                    style_cell={'textAlign': 'left', 'whiteSpace': 'normal'},
                                    style_cell_conditional=[{'if': {'column_id': 'Goat Score'}, 'text-align': 'right'},
                                                            {'if': {'column_id': 'Rank'}, 'text-align': 'right'}],
                                    style_data_conditional=[{'if': {'row_index': 'odd'}, 'backgroundColor': 'rgb(248,248,248)'}]
                                    )
    else:
        raise PreventUpdate

if __name__ == '__main__':
    app.run_server()