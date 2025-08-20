import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Data
data = {
    "Kat_1": ["Penjualan"] * 9,
    "Kat_2": ["Penjualan Bersih"] * 8 + ["Potongan/Return"],
    "Kat_3": ["COGS"] * 4 + ["Gross Profit"] * 4 + [""],
    "Kat_4": ["", "COGM", "COGM", "COGM", "", "Operational Cost", "Operational Cost", "Operational Cost", ""],
    "Kat_5": ["FG", "COM", "Conversion Cost", "WIP", "Operational Income", "CK", "HO", "Resto", ""],
    "Value": [72, 340, 265, 62, 68, 60, 38, 96, 60],
    "%": ["6.79%", "32.05%", "24.98%", "5.84%", "6.41%", "5.66%", "3.58%", "9.05%", "5.66%"]
}

df = pd.DataFrame(data)

# Sunburst chart
fig = px.sunburst(
    df,
    path=["Kat_1", "Kat_2", "Kat_3", "Kat_4", "Kat_5"],
    values="Value",
    title="Sunburst Penjualan"
)

# Dash app
app = dash.Dash(__name__)
server = app.server  # Ini penting untuk deploy di Render

app.layout = html.Div([
    html.H1("Visualisasi Sunburst Penjualan"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
