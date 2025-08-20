import dash
from dash import html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_table
import json

# JSON string yang kamu berikan (potong supaya nggak terlalu panjang)
json_str = '{"Kat_1":{"0":"Penjualan","1":"Penjualan","2":"Penjualan","3":"Penjualan","4":"Penjualan","5":"Penjualan","6":"Penjualan","7":"Penjualan","8":"Penjualan","9":"Penjualan","10":"Penjualan","11":"Penjualan","12":"Penjualan","13":"Penjualan","14":"Penjualan","15":"Penjualan","16":"Penjualan","17":"Penjualan","18":"Penjualan","19":"Penjualan","20":"Penjualan","21":"Penjualan","22":"Penjualan","23":"Penjualan","24":"Penjualan","25":"Penjualan","26":"Penjualan","27":"Penjualan","28":"Penjualan","29":"Penjualan","30":"Penjualan","31":"Penjualan","32":"Penjualan","33":"Penjualan","34":"Penjualan","35":"Penjualan","36":"Penjualan","37":"Penjualan","38":"Penjualan","39":"Penjualan","40":"Penjualan","41":"Penjualan","42":"Penjualan","43":"Penjualan","44":"Penjualan","45":"Penjualan","46":"Penjualan","47":"Penjualan","48":"Penjualan","49":"Penjualan","50":"Penjualan","51":"Penjualan","52":"Penjualan","53":"Penjualan","54":"Penjualan","55":"Penjualan","56":"Penjualan","57":"Penjualan","58":"Penjualan","59":"Penjualan","60":"Penjualan","61":"Penjualan","62":"Penjualan"},"Kat_2":{"0":"Penjualan Bersih","1":"Penjualan Bersih","2":"Penjualan Bersih","3":"Penjualan Bersih","4":"Penjualan Bersih","5":"Penjualan Bersih","6":"Penjualan Bersih","7":"Penjualan Bersih","8":"Potongan\\/Return","9":"Penjualan Bersih","10":"Penjualan Bersih","11":"Penjualan Bersih","12":"Penjualan Bersih","13":"Penjualan Bersih","14":"Penjualan Bersih","15":"Penjualan Bersih","16":"Penjualan Bersih","17":"Potongan\\/Return","18":"Penjualan Bersih","19":"Penjualan Bersih","20":"Penjualan Bersih","21":"Penjualan Bersih","22":"Penjualan Bersih","23":"Penjualan Bersih","24":"Penjualan Bersih","25":"Penjualan Bersih","26":"Potongan\\/Return","27":"Penjualan Bersih","28":"Penjualan Bersih","29":"Penjualan Bersih","30":"Penjualan Bersih","31":"Penjualan Bersih","32":"Penjualan Bersih","33":"Penjualan Bersih","34":"Penjualan Bersih","35":"Potongan\\/Return","36":"Penjualan Bersih","37":"Penjualan Bersih","38":"Penjualan Bersih","39":"Penjualan Bersih","40":"Penjualan Bersih","41":"Penjualan Bersih","42":"Penjualan Bersih","43":"Penjualan Bersih","44":"Potongan\\/Return","45":"Penjualan Bersih","46":"Penjualan Bersih","47":"Penjualan Bersih","48":"Penjualan Bersih","49":"Penjualan Bersih","50":"Penjualan Bersih","51":"Penjualan Bersih","52":"Penjualan Bersih","53":"Potongan\\/Return","54":"Penjualan Bersih","55":"Penjualan Bersih","56":"Penjualan Bersih","57":"Penjualan Bersih","58":"Penjualan Bersih","59":"Penjualan Bersih","60":"Penjualan Bersih","61":"Penjualan Bersih","62":"Potongan\\/Return"},"Kat_3":{"0":"COGS","1":"COGS","2":"COGS","3":"COGS","4":"Gross Profit","5":"Gross Profit","6":"Gross Profit","7":"Gross Profit","8":"","9":"COGS","10":"COGS","11":"COGS","12":"COGS","13":"Gross Profit","14":"Gross Profit","15":"Gross Profit","16":"Gross Profit","17":"","18":"COGS","19":"COGS","20":"COGS","21":"COGS","22":"Gross Profit","23":"Gross Profit","24":"Gross Profit","25":"Gross Profit","26":"","27":"COGS","28":"COGS","29":"COGS","30":"COGS","31":"Gross Profit","32":"Gross Profit","33":"Gross Profit","34":"Gross Profit","35":"","36":"COGS","37":"COGS","38":"COGS","39":"COGS","40":"Gross Profit","41":"Gross Profit","42":"Gross Profit","43":"Gross Profit","44":"","45":"COGM","46":"COGM","47":"COGM","48":"","49":"Operational Cost","50":"Operational Cost","51":"Operational Cost","52":"","53":"","54":"COGM","55":"COGM","56":"COGM","57":"","58":"Operational Cost","59":"Operational Cost","60":"Operational Cost","61":"","62":""},"Kat_4":{"0":"COGM","1":"COGM","2":"COGM","3":"","4":"Operational Cost","5":"Operational Cost","6":"Operational Cost","7":"","8":"","9":"COGM","10":"COGM","11":"COGM","12":"","13":"Operational Cost","14":"Operational Cost","15":"Operational Cost","16":"","17":"","18":"COGM","19":"COGM","20":"COGM","21":"","22":"Operational Cost","23":"Operational Cost","24":"Operational Cost","25":"","26":"","27":"COGM","28":"COGM","29":"COGM","30":"","31":"Operational Cost","32":"Operational Cost","33":"Operational Cost","34":"","35":"","36":"COGM","37":"COGM","38":"COGM","39":"","40":"Operational Cost","41":"Operational Cost","42":"Operational Cost","43":"","44":"","45":"COGM","46":"COGM","47":"COGM","48":"","49":"Operational Cost","50":"Operational Cost","51":"Operational Cost","52":"","53":"","54":"COGM","55":"COGM","56":"COGM","57":"","58":"Operational Cost","59":"Operational Cost","60":"Operational Cost","61":"","62":""},"Kat_5":{"0":"COM","1":"Conversion Cost","2":"WIP","3":"FG","4":"Resto","5":"CK","6":"HO","7":"Operational Income","8":"","9":"COM","10":"Conversion Cost","11":"WIP","12":"FG","13":"Resto","14":"CK","15":"HO","16":"Operational Income","17":"","18":"COM","19":"Conversion Cost","20":"WIP","21":"FG","22":"Resto","23":"CK","24":"HO","25":"Operational Income","26":"","27":"COM","28":"Conversion Cost","29":"WIP","30":"FG","31":"Resto","32":"CK","33":"HO","34":"Operational Income","35":"","36":"COM","37":"Conversion Cost","38":"WIP","39":"FG","40":"Resto","41":"CK","42":"HO","43":"Operational Income","44":"","45":"COM","46":"Conversion Cost","47":"WIP","48":"FG","49":"Resto","50":"CK","51":"HO","52":"Operational Income","53":"","54":"COM","55":"Conversion Cost","56":"WIP","57":"FG","58":"Resto","59":"CK","60":"HO","61":"Operational Income","62":""},"Month":{"0":1735689600000,"1":1735689600000,"2":1735689600000,"3":1735689600000,"4":1735689600000,"5":1735689600000,"6":1735689600000,"7":1735689600000,"8":1735689600000,"9":1738368000000,"10":1738368000000,"11":1738368000000,"12":1738368000000,"13":1738368000000,"14":1738368000000,"15":1738368000000,"16":1738368000000,"17":1738368000000,"18":1740787200000,"19":1740787200000,"20":1740787200000,"21":1740787200000,"22":1740787200000,"23":1740787200000,"24":1740787200000,"25":1740787200000,"26":1740787200000,"27":1743465600000,"28":1743465600000,"29":1743465600000,"30":1743465600000,"31":1743465600000,"32":1743465600000,"33":1743465600000,"34":1743465600000,"35":1743465600000,"36":1746057600000,"37":1746057600000,"38":1746057600000,"39":1746057600000,"40":1746057600000,"41":1746057600000,"42":1746057600000,"43":1746057600000,"44":1746057600000,"45":1748736000000,"46":1748736000000,"47":1748736000000,"48":1748736000000,"49":1748736000000,"50":1748736000000,"51":1748736000000,"52":1748736000000,"53":1748736000000,"54":1751328000000,"55":1751328000000,"56":1751328000000,"57":1751328000000,"58":1751328000000,"59":1751328000000,"60":1751328000000,"61":1751328000000,"62":1751328000000},"Value":{"0":40,"1":40,"2":9,"3":10,"4":12,"5":12,"6":5,"7":10,"8":10,"9":50,"10":50,"11":9,"12":10,"13":14,"14":10,"15":5,"16":10,"17":7,"18":45,"19":40,"20":10,"21":7,"22":12,"23":8,"24":5,"25":11,"26":7,"27":55,"28":30,"29":9,"30":15,"31":13,"32":7,"33":5,"34":8,"35":9,"36":60,"37":35,"38":7,"39":12,"40":20,"41":10,"42":5,"43":9,"44":8,"45":40,"46":30,"47":8,"48":8,"49":15,"50":8,"51":8,"52":10,"53":9,"54":50,"55":40,"56":10,"57":10,"58":10,"59":5,"60":5,"61":10,"62":10}}'

# Load JSON ke dict
data_dict = json.loads(json_str)

# Buat DataFrame
df = pd.DataFrame.from_dict(data_dict)

# Convert timestamp 'Month' ke datetime
df['Month'] = pd.to_datetime(df['Month'], unit='ms')

# Buat kolom string format YYYY-MM untuk dropdown pilihan bulan
df['Month_str'] = df['Month'].dt.to_period('M').astype(str)

available_months = df['Month_str'].unique()

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
def update_sunburst(selected_month_str):
    # Filter dataframe berdasarkan string bulan, lalu ambil baris yang sesuai
    filtered_df = df[df['Month_str'] == selected_month_str]

    fig = px.sunburst(
        filtered_df,
        path=["Kat_1", "Kat_2", "Kat_3", "Kat_4", "Kat_5"],
        values="Value",
        color='Kat_3',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    return fig

@app.callback(
    Output('detail-table-container', 'children'),
    Input('sunburst-chart', 'clickData'),
    Input('month-filter', 'value')
)
def display_click_data(clickData, selected_month_str):
    if clickData is None:
        return html.Div("Klik sebuah area di sunburst untuk melihat detail data.")

    path_str = clickData['points'][0].get('id', None)
    if not path_str:
        return html.Div("Data path tidak ditemukan.")
    
    path_list = path_str.split('/')

    filtered_df = df[df['Month_str'] == selected_month_str]

    columns_kat = ["Kat_1", "Kat_2", "Kat_3", "Kat_4", "Kat_5"]
    for i, val in enumerate(path_list):
        if i < len(columns_kat) and val != "":
            filtered_df = filtered_df[filtered_df[columns_kat[i]] == val]

    if filtered_df.empty:
        return html.Div("Tidak ada data untuk area yang dipilih.")

    return dash_table.DataTable(
        data=filtered_df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in filtered_df.columns if i != 'Month_str'],
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
