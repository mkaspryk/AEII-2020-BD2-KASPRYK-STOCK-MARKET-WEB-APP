import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from . import api_handling, plotting
from datetime import datetime

x_data = []
y_data_scatter = []
y_data_box_open = []
y_data_box_close = []
y_data_box_low = []
y_data_box_high = []

api_handler = api_handling.ApiHandler()
data = api_handler.get_minute_history('BTC', 'USD', 200)

for dictionary in data:
    # average = str((float(dictionary['open']) + float(dictionary['close']) + float(dictionary['low']) + float(dictionary['high']))/ 4)
    x_data.append(datetime.fromtimestamp(int(dictionary['time'])))
    y_data_box_open.append(float(dictionary['open']))
    y_data_box_close.append(float(dictionary['close']))
    y_data_box_low.append(float(dictionary['low']))
    y_data_box_high.append(float(dictionary['high']))
    y_data_scatter.append(dictionary['open'])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1('Square Root Slider Graph'),
    dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    dcc.Slider(
        id='slider-updatemode',
        marks={i: '{}'.format(i) for i in range(20)},
        max=20,
        value=2,
        step=1,
        updatemode='drag',
    ),
])


@app.callback(Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
def display_value(value):
    global x_data
    global y_data_box_open
    graphs = []

    print(y_data_scatter[0])

    graphs.append(go.Scatter(
        x=x_data,
        y=y_data_scatter,
        name='Manipulate Graph'
    ))

    graphs.append(go.Ohlc(
        x = x_data,
        open = y_data_box_open,
        high = y_data_box_high,
        low = y_data_box_low,
        close = y_data_box_close
    ))

    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x_data), max(x_data)]),
        yaxis=dict(range=[min(y_data_box_open), max(y_data_box_open)]),
        font=dict(color='white'),

    )
    return {'data': graphs, 'layout': layout}
