import base64
import datetime
import io

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table

import pandas as pd

from app import app

from utilities import model



layout = html.Div([
    dbc.Jumbotron(
    [
        html.H2("Asignador de ruta", style={"color":"#6427B9"}),
        html.P("Seleccione un archivo csv que contenga las coordenadas de LATITUD, LONGITUD de un recorrido para asignarle una ruta"),
        html.P(["En el siguiente enlace puede descargar un archivo de ejemplo: ", html.A("Enlace", href="https://drive.google.com/file/d/1sjeMfND4ijUykeNA5mZ3jU8HWd8i-kd2/view")])

    ]),
    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Arrastra o ',
                html.A('Selecciona un archivo')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'borderColor': '#7cb927',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-upload'),
    ], className = 'col-md-10 offset-md-1')
])


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    predicted, proba = model.predict(df)
 
    import plotly.express as px

    map_fig = px.scatter_mapbox(df, lat="LATITUD", lon="LONGITUD",
                        color_discrete_sequence=["fuchsia"], zoom=13, height=300)
    map_fig.update_layout(mapbox_style="open-street-map")
    map_fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return html.Div([
        
        html.Div([
            html.Div([
                html.H6([html.Span("Nombre del archivo: ", style={"color": "#6427B9"}),filename]),
                html.H6([html.Span("Ruta asignada: ", style={"color": "#6427B9"}),predicted]),

                html.H6([html.Span("Seguridad de predicción: ", style={"color": "#6427B9"}),str(proba * 100) + "%"]),
            ], className="col-md-6"),
            html.Div([
                 html.H6([html.Span("Imagen generada: ", style={"color": "#6427B9", "text-align":"center"})]),
                  html.Img(src='assets/route.jpg', height="200px", style={"display": "block", "margin-left": "auto", "margin-right": "auto", "width": "50%"}),

            ], className="col-md-6"),
        ], className="row", style={"border": "1px solid #7cb927", "text-align" : "center", "border-radius":"10px"}),

        html.Hr(),  # horizontal line
        dcc.Graph(
            id='map-fig',
            figure=map_fig
        ),

        html.Hr(),  # horizontal line

      
        # For debugging, display the raw contents provided by the web browser
   
    ])


@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children