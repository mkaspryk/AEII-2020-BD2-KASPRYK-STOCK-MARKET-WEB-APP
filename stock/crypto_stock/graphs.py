import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from . import api_handling
from datetime import datetime

x_data = []
y_data_box_open = []
y_data_scatter = []
y_data_box_close = []
y_data_box_low = []
y_data_box_high = []

app = None

colors = {
    'background': 'white',
    'text': '#ffffff',
    'crypto-text': '#101010',
}

history_precisions = ['minute', 'hour', 'day']


def refresh_data(crypto_symbol, history_precision):

    data = None
    api_handler = api_handling.ApiHandler()
    try:
        if history_precision == 'minute':
            data = api_handler.get_minute_history(crypto_symbol, 'USD', 200)
        elif history_precision == 'hour':
            data = api_handler.get_hourly_history(crypto_symbol, 'USD', 200)
        elif history_precision == 'day':
            data = api_handler.get_daily_history(crypto_symbol, 'USD', 100)
    except KeyError:
        return
        #     crypto_symbol = "BTC"
        #     data = api_handler.get_hourly_history(crypto_symbol, 'USD', 200)
        # return crypto_symbol

    x_data.clear()
    y_data_box_open.clear()
    y_data_scatter.clear()
    y_data_box_close.clear()
    y_data_box_low.clear()
    y_data_box_high.clear()
    for dictionary in data:
        x_data.append(datetime.fromtimestamp(int(dictionary['time'])))
        y_data_box_open.append(float(dictionary['open']))
        y_data_box_close.append(float(dictionary['close']))
        y_data_box_low.append(float(dictionary['low']))
        y_data_box_high.append(float(dictionary['high']))
        y_data_scatter.append(dictionary['open'])


def return_app(crypto_symbol=None):
    global app
    if(crypto_symbol == '' or crypto_symbol is None):
        crypto_symbol = 'BTC'
    # crypto_symbol = refresh_data(crypto_symbol, 'hour')
    refresh_data(crypto_symbol, 'hour')
    app = DjangoDash('CryptoGraph')

    app.layout = html.Div(style={'backgroundColor': colors['background'], 'margin-left': '0px',
    'margin-top': '0px', 'margin-right': '0px', 'margin-bottom': '0px'}, children=[
        html.H1(children=crypto_symbol + ' history',
                style={
                    'textAlign': 'top',
                    'color': colors['crypto-text'],
                    'margin-top': '0px',
                }
                ),

        dcc.Graph(
            id='slider-graph',
            animate=True,
            style={"backgroundColor": colors['background'], 'color': '#ffffff'},
            figure={
                'data': [],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']

                    }
                }
            }
        ),

        dcc.RadioItems(
            id='mode-radio',
            options=[{'label': value, 'value': value} for value in history_precisions],
            value='hour',
            style={"color": colors['crypto-text'], "padding": "20px"}
        ),
    ])

    @app.callback(Output('slider-graph', 'figure'),
                  [Input('mode-radio', 'value')])
    def change_mode(value):
        refresh_data(crypto_symbol, value)
        global x_data
        global y_data_box_open
        graphs = []

        graphs.append(go.Scatter(
            x=x_data,
            y=y_data_scatter,
            name='Manipulate Graph'
        ))

        graphs.append(go.Ohlc(
            x=x_data,
            open=y_data_box_open,
            high=y_data_box_high,
            low=y_data_box_low,
            close=y_data_box_close
        ))

        layout = go.Layout(
            paper_bgcolor='#27293d',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(range=[min(x_data), max(x_data)]),
            yaxis=dict(range=[min(y_data_box_open), max(y_data_box_open)]),
            font=dict(color='white'),
        )
        return {'data': graphs, 'layout': layout}
