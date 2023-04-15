from dash import dcc, html, dash
import plotly.graph_objs as go
import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset
df = pd.read_csv('./product-analytics/data/WA_Marketing-Campaign.csv')

# Define the app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    # Dashboard component
    html.Div(children=[
        html.H1(children="Sales Dashboard"),
        dcc.Graph(
            id="sales-graph",
            figure={
                "data": [
                    go.Bar(
                        x=df["Promotion"],
                        y=df["SalesInThousands"],
                        name="Sales"
                    )
                ],
                "layout": go.Layout(
                    title="Sales by Promotion",
                    xaxis={"title": "Promotion"},
                    yaxis={"title": "Sales (in thousands)"}
                )
            }
        )
    ], className="six columns"),

    # A/B test component
    html.Div(children=[
        html.H1(children="A/B Test Results"),
        dcc.Dropdown(
            id="promotion-dropdown",
            options=[
                {"label": "Promotion 1", "value": 1},
                {"label": "Promotion 2", "value": 2},
                {"label": "Promotion 3", "value": 3}
            ],
            value=1
        ),
        dcc.Graph(
            id="ab-test-graph",
            figure={
                "data": [
                    go.Bar(
                        x=["Control", "Variant"],
                        y=[df[df["Promotion"] == 1]["SalesInThousands"].mean(),
                           df[df["Promotion"] == 1]["SalesInThousands"].mean()],
                        name="Sales"
                    )
                ],
                "layout": go.Layout(
                    title="A/B Test Results",
                    xaxis={"title": "Group"},
                    yaxis={"title": "Sales (in thousands)"}
                )
            }
        )
    ], className="six columns")
])

# Define the callback functions
@app.callback(
    dash.Output("ab-test-graph", "figure"),
    [dash.Input("promotion-dropdown", "value")]
)
def update_ab_test_graph(promotion):
    control = df[(df["Promotion"] == promotion) & (df["Group"] == "Control")]["SalesInThousands"]
    variant = df[(df["Promotion"] == promotion) & (df["Group"] == "Variant")]["SalesInThousands"]

    # Run the t-test
    t_stat, p_value = ttest_ind(control, variant)

    # Update the figure
    figure = {
        "data": [
            go.Bar(
                x=["Control", "Variant"],
                y=[control.mean(), variant.mean()],
                name="Sales"
            )
        ],
        "layout": go.Layout(
            title=f"A/B Test Results for Promotion {promotion}",
            xaxis={"title": "Group"},
            yaxis={"title": "Sales (in thousands)"},
            annotations=[
                {
                    "x": 0.5,
                    "y": 1.15,
                    "text": f"t-statistic: {round(t_stat, 2)}, p-value: {round(p_value, 4)}",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "font": {"size": 12}
                }
            ]
        )
    }

    return figure

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)