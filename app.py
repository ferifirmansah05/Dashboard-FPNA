import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Data dengan kolom 'Month'
data = {
    "Month": ["Jan", "Jan", "Jan", "Jan", "Jan", "Jan", "Jan", "Jan", "Jan",
              "Feb", "Feb", "Feb", "Feb", "Feb", "Feb", "Feb", "Feb", "Feb"],
    "Kat_1": ["Penjualan"] * 18,
    "Kat_2": ["Penjualan Bersih"] * 16 + ["Potongan/Return", "Potongan/Return"],
    "Kat_3": ["COGS"] * 4 + ["Gross Profit"] * 4 + [""] + ["COGS"] * 4 + ["Gross Profit"] * 4 + [""] ,
    "Kat_4": ["", "COGM", "COGM", "COGM", "", "Operational Cost", "Operational Cost", "Operational Cost", "",
              "", "COGM", "COGM", "COGM", "", "Operational Cost", "Operational Cost", "Operational Cost", ""],
    "Kat_5": ["FG", "COM", "Conversion Cost", "WIP", "Operational Income", "CK", "HO", "Resto", "",
              "FG", "COM", "Conversion Cost", "WIP", "Operational Income", "CK", "HO", "Resto", ""],
    "Value": [72, 340, 265, 62, 68, 60, 38, 96, 60,
              80, 300, 240, 55, 70, 50, 35, 90, 40],
    "%": ["6.79%", "32.05%", "24.98%", "5.84%", "6.41%", "5.66%", "3.58%", "9.05%", "5.66%",
          "7.5%", "28.1%", "22.5%", "5.2%", "6.5%", "4.7%", "3.3%", "8.4%", "3.7%"]
}

df = pd.DataFrame(data)

# Daftar bulan unik untuk dropdown
available_months = df["Month"].unique()

# Dash App
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Visualisasi Sunburst Penjualan"),
    
    html.Label("Pilih Bulan:"),
    dcc.Dropdown(
        id='month-filter',
        options=[{"label": m, "value": m} for m in available_months],
        value=available_months[0],  # default value
        clearable=False
    ),
    
    dcc.Graph(id='sunburst-chart')
])

# Callback untuk memperbarui chart
@app.callback(
    Output('sunburst-chart', 'figure'),
    Input('month-filter', 'value')
)
def update_sunburst(selected_month):
    filtered_df = df[df["Month"] == selected_month]

    fig = px.sunburst(
        filtered_df,
        path=["Kat_1", "Kat_2", "Kat_3", "Kat_4", "Kat_5"],
        values="Value",
        title=f"Sunburst Penjualan - {selected_month}"
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
