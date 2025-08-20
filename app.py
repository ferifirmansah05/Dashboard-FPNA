import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_table

# Data dengan kolom 'Month'
data = {
    "Month": ["Jan", "Jan", "Jan", "Jan", "Jan", "Jan", "Jan", "Jan", "Jan",
              "Feb", "Feb", "Feb", "Feb", "Feb", "Feb", "Feb", "Feb", "Feb"],
    "Kat_1": ["Penjualan"] * 18,
    "Kat_2": ["Penjualan Bersih"] * 16 + ["Potongan/Return", "Potongan/Return"],
    "Kat_3": ["COGS"] * 4 + ["Gross Profit"] * 4 + [""] + ["COGS"] * 4 + ["Gross Profit"] * 4 + [""],
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

available_months = df["Month"].unique()

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Label("Pilih Bulan:"),
    dcc.Dropdown(
        id='month-filter',
        options=[{"label": m, "value": m} for m in available_months],
        value=available_months[0],
        clearable=False
    ),
    dcc.Graph(id='sunburst-chart'),

    html.Hr(),

    html.Div(id='detail-table-container')
])

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
        color='Kat_3'
    )
    return fig

@app.callback(
    Output('detail-table-container', 'children'),
    Input('sunburst-chart', 'clickData'),
    Input('month-filter', 'value')
)
def display_click_data(clickData, selected_month):
    if clickData is None:
        return html.Div("Klik sebuah area di sunburst untuk melihat detail data.")

    # Ambil path dari 'id' yang berformat "Penjualan/Penjualan Bersih/COGS/FG"
    path_str = clickData['points'][0].get('id', None)
    if not path_str:
        return html.Div("Data path tidak ditemukan.")
    
    path_list = path_str.split('/')

    filtered_df = df[df["Month"] == selected_month]

    columns_kat = ["Kat_1", "Kat_2", "Kat_3", "Kat_4", "Kat_5"]
    for i, val in enumerate(path_list):
        if i < len(columns_kat) and val != "":
            filtered_df = filtered_df[filtered_df[columns_kat[i]] == val]

    if filtered_df.empty:
        return html.Div("Tidak ada data untuk area yang dipilih.")

    return dash_table.DataTable(
        data=filtered_df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in filtered_df.columns],
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        style_header={
            'backgroundColor': 'lightgrey',
            'fontWeight': 'bold'
        }
    )


if __name__ == '__main__':
    app.run_server(debug=True)
