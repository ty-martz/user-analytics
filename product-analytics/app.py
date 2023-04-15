from dash import dcc, html, dash
import pandas as pd
import plotly.express as px

# load the data
df = pd.read_csv('./product-analytics/data/WA_Marketing-Campaign.csv')

# init the app
app = dash.Dash(__name__)

app.layout = html.Div([
    
    # location id filter
    html.Div([
        dcc.Dropdown(
            id='location-dropdown',
            options=[{'label': loc, 'value': loc} for loc in ['All'] + sorted(df['LocationID'].unique())],
            value='All'
        ),
        html.Label('Location')
    ], style={'width': '25%', 'display': 'inline-block'}),
    
    # market id filter
    html.Div([
        dcc.Dropdown(
            id='market-dropdown',
            options=[{'label': market, 'value': market} for market in ['All'] + sorted(df['MarketID'].unique())],
            value='All'
        ),
        html.Label('Market')
    ], style={'width': '25%', 'display': 'inline-block'}),
    
    # total sales KPI
    html.Div([
        html.H4(id='total-sales', style={"text-align": "center"})
    ], style={'width': '25%', 'display': 'inline-block', 'border': '2px solid black'}),
    
    # bar chart
    html.Div([
        dcc.Graph(id='promotion-bar-chart')
    ], style={'width': '50%', 'display': 'inline-block'}),
    
    # line chart
    html.Div([
        dcc.Graph(id='sales-line-chart')
    ], style={'width': '50%', 'display': 'inline-block'}),
    
])


@app.callback(
    [dash.Output('total-sales', 'children'),
     dash.Output('promotion-bar-chart', 'figure'),
     dash.Output('sales-line-chart', 'figure')],
    [dash.Input('location-dropdown', 'value'),
     dash.Input('market-dropdown', 'value')]
)
def update_charts(location, market):
    # filters
    if location == 'All' and market == 'All':
        filtered_df = df.copy()
    elif location == 'All':
        filtered_df = df[df['MarketID'] == market]
    elif market == 'All':
        filtered_df = df[df['LocationID'] == location]
    else:
        filtered_df = df[(df['LocationID'] == location) & (df['MarketID'] == market)]
    
    # calculate total sales and update KPI
    total_sales = filtered_df['SalesInThousands'].sum()
    total_sales_kpi = f'Total Sales: ${total_sales:.2f}k'
    
    # bar
    promotion_sales = filtered_df.groupby('Promotion')['SalesInThousands'].sum().reset_index()
    promotion_bar_chart = px.bar(promotion_sales, x='Promotion', y='SalesInThousands', 
                                  color='Promotion', title='Total Sales by Promotion')
    
    # line
    sales_by_week = filtered_df.groupby(['week', 'Promotion'])['SalesInThousands'].sum().reset_index()
    sales_line_chart = px.line(sales_by_week, x='week', y='SalesInThousands', color='Promotion',
                               title='Sales by Week')
    
    return total_sales_kpi, promotion_bar_chart, sales_line_chart


if __name__ == '__main__':
    app.run_server(debug=True)
