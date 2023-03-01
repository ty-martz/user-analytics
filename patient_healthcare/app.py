# Patient Chart/Dashboard

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime as dt

# Load patient data
df = pd.read_csv('patient_data.csv')

# Create app
app = dash.Dash(__name__)

# Styling colors
colors = {
    'background': '#FCFBF8',
    'text': '#0E497A',
    'primary': '#007F79',
    'secondary': '#8BCAEA',
    'accent': '#EFA53A'
}

# Define layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    
    # General patient info section
    html.Div([
        html.H2('Patient Information', style={'color': colors['primary']}),
        html.Table([
            html.Tr([html.Td('Name:'), html.Td(df['Name'].iloc[0])], style={'color': colors['text']}),
            html.Tr([html.Td('Age:'), html.Td(df['Age'].iloc[0])], style={'color': colors['text']}),
            html.Tr([html.Td('Last Visit:'), html.Td(df['Last Visit'].iloc[0])], style={'color': colors['text']})
        ])
    ]),
    
    # Line graph section
    html.Div([
        html.H2(children='Changes in Vitals Over Time', style={'color': colors['secondary']}),
        dcc.Dropdown(
            id='vital-sign',
            options=[
                {'label': 'Blood Pressure', 'value': 'Blood Pressure'},
                {'label': 'Heart Rate', 'value': 'Heart Rate'},
                {'label': 'Body Temperature', 'value': 'Body Temperature'}
            ],
            value='Blood Pressure'
        ),
        dcc.Graph(
            id='vital-sign-graph'
        )
    ]),
    
    # Indicator card section
    html.Div([
        html.H2(children='General Health', style={'color': colors['accent']}),
        html.Div([
            html.Div([
                html.H3('Overall Score', style={'color': colors['text']}),
                html.H2(id='overall-score', className='indicator-value', style={'color': colors['text']})
            ], className='indicator-card'),
            html.Div([
                html.H3('Risk Level', style={'color': colors['text']}),
                html.H2(id='risk-level', className='indicator-value', style={'color': colors['text']})
            ], className='indicator-card')
        ], className='indicator-container')
    ])
])

# Define callbacks
@app.callback(
    dash.dependencies.Output('vital-sign-graph', 'figure'),
    [dash.dependencies.Input('vital-sign', 'value')])
def update_vital_sign_graph(vital_sign):
    trace = go.Scatter(
        x = df['Date'],
        y = df[vital_sign],
        mode = 'lines',
        name = vital_sign
    )
    layout = go.Layout(
        title = vital_sign + ' Over Time',
        xaxis = {'title': 'Date'},
        yaxis = {'title': vital_sign}
    )
    return {'data': [trace], 'layout': layout}

@app.callback(
    [dash.dependencies.Output('overall-score', 'children'),
     dash.dependencies.Output('risk-level', 'children')],
    [dash.dependencies.Input('vital-sign', 'value')])
def update_indicator_cards(vital_sign):
    # Calculate overall score and risk level based on selected vital sign
    overall_score = df[vital_sign].mean()
    if overall_score > 80:
        risk_level = 'High'
    elif overall_score > 60:
        risk_level = 'Medium'
    else:
        risk_level = 'Low'
    return round(overall_score, 2), risk_level

if __name__ == '__main__':
    app.run_server(debug=True)
