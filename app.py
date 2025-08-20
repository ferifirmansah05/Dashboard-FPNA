import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Contoh data fiktif
data = {
    'Region': ['Asia', 'Asia', 'Europe', 'Europe', 'America', 'America'],
    'Country': ['Japan', 'India', 'Germany', 'France', 'USA', 'Brazil'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture'],
    'Sales': [10000, 7000, 12000, 9000, 15000, 11000],
    'Quantity': [100, 85, 120, 95, 130, 105]
}

df = pd.DataFrame(data)

# Inisialisasi Dash app
app = dash.Dash(__name__)
app.title = "Sales Dashboard"

# Layout
app.layout = html.Div([
    html.H1("🌍 Sales Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.Label("Filter by Category:"),
            dcc.Dropdown(
                id='category-filter',
                options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
                value=None,
                placeholder="Select category",
                clearable=True
            )
        ], style={'width': '30%', 'display': 'inline-block'}),

        html.Div([
            html.H4("💰 Total Sales:"),
            html.Div(id='total-sales', style={'fontSize': 24})
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center'}),

        html.Div([
            html.H4("📦 Total Quantity:"),
            html.Div(id='total-quantity', style={'fontSize': 24})
        ], style={'width': '30%', 'display': 'inline-block', 'textAlign': 'center'})
    ], style={'padding': '20px'}),

    html.Div([
        dcc.Graph(id='sunburst-chart'),
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='bar-chart'),
    ], style={'width': '49%', 'display': 'inline-block'})
])

# Callback
@app.callback(
    Output('sunburst-chart', 'figure'),
    Output('bar-chart', 'figure'),
    Output('total-sales', 'children'),
    Output('total-quantity', 'children'),
    Input('category-filter', 'value')
)
def update_dashboard(selected_category):
    if selected_category:
        filtered_df = df[df['Category'] == selected_category]
    else:
        filtered_df = df

    # Sunburst chart
    sunburst = px.sunburst(
        filtered_df,
        path=['Region', 'Country', 'Category'],
        values='Sales',
        title='Sales Distribution by Region/Country/Category'
    )

    # Bar chart
    bar = px.bar(
        filtered_df,
        x='Country',
        y='Sales',
        color='Country',
        title='Sales per Country'
    )

    # Metrics
    total_sales = f"${filtered_df['Sales'].sum():,.0f}"
    total_quantity = f"{filtered_df['Quantity'].sum():,}"

    return sunburst, bar, total_sales, total_quantity

# Run server
if __name__ == '__main__':
    app.run_server(debug=True)
