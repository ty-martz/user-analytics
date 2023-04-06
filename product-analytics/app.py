import pandas as pd
import plotly.graph_objs as go
from dash import dash, dcc, html
from helpers import calc_conversion_rate

# Load data
data = pd.read_csv('./product-analytics/data/ab_test_data.csv').sample(10000)

# Calculate conversion rates for each group
control_conversion = calc_conversion_rate(data, 'control')
test_conversion = calc_conversion_rate(data, 'test')
print('Conversion Rates:')
print(f'--Control = {control_conversion}')
print(f'--Test = {test_conversion}')

# Create bar chart to compare conversion rates
bar_chart = go.Bar(
    x=['Control', 'Test'],
    y=[control_conversion, test_conversion],
    text=[f'{control_conversion:.2%}', f'{test_conversion:.2%}'],
    textposition='auto',
    marker=dict(color=['rgb(30,50,11)', 'rgb(213,187,102)']),
    hoverinfo='text',
    name='Conversion Rate'
)

# Create line chart to show number of views and clicks
control_data = data[data['group'] == 'control']
test_data = data[data['group'] == 'test']

control_line = go.Scatter(
    x=control_data.index,
    y=control_data['views'],
    name='Control Views',
    mode='markers'
)

test_line = go.Scatter(
    x=test_data.index,
    y=test_data['views'],
    name='Test Views',
    mode='markers'
)

control_clicks = go.Scatter(
    x=control_data.index,
    y=control_data['clicks'],
    name='Control Clicks',
    mode='markers'
)

test_clicks = go.Scatter(
    x=test_data.index,
    y=test_data['clicks'],
    name='Test Clicks',
    mode='markers'
)

line_chart = go.Figure(
    data=[control_line, test_line, control_clicks, test_clicks],
    layout=go.Layout(title='Views and Clicks Over Time')
)

# Create the dashboard layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='A/B Test Dashboard'),
    html.Div(children=[
        html.Div(children=[
            dcc.Graph(id='conversion-graph', figure=go.Figure(data=bar_chart))
        ], className='six columns'),
        html.Div(children=[
            dcc.Graph(id='line-graph', figure=line_chart)
        ], className='six columns')
    ], className='row')
])

# Run the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
