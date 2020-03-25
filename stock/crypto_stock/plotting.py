import plotly.offline as py
import plotly.graph_objs as go
import numpy as np
from . import api_handling
from datetime import datetime


def prepare_graf(data, graph_name, graph_mode, fig = None):
    x_data = []
    y_data = []

    if fig is None:
        fig = go.Figure()

    for dict in data:
        x_data.append(datetime.fromtimestamp(int(dict['time'])))
        y_data.append(dict['open'])
    fig.add_trace(go.Scatter(x = x_data, y = y_data, mode=graph_mode, name = graph_name))

    return fig
