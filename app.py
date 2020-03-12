#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import plotly_express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import data_handling

#tips = px.data.tips()
tips = data_handling.TradeSpace()
col_options = [dict(label=x, value=x) for x in tips.columns]
dimensions = ["x", "y", "color","size", "facet_col", "facet_row"]

app = dash.Dash(
    __name__, external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"]
)

app.layout = html.Div(
    [
        html.H1("Trade Space Analysis of Offshore Datacenter"),
        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),
        dcc.Graph(id="graph", style={"width": "75%", "display": "inline-block"}),
    ]
)

@app.callback(Output("graph", "figure"), [Input(d, "value") for d in dimensions])
def make_figure(x, y, color,size,facet_col, facet_row):
    return px.scatter(
        tips,
        x=x,
        y=y,
        color=color,
        text="Architecture Name",
        size=size,
        facet_col=facet_col,
        facet_row=facet_row,
        height=700,
    )


if __name__ == '__main__':
#    app.run_server(debug=True, host='0.0.0.0', port='80')
    app.run_server(debug=True)