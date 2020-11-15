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
        html.H2("Asignador de multiples rutas", style={"color":"#6427B9"}),
        html.P("Seleccione un archivo csv con las columnas IDRECORRIDO, LATITUD, LONGITUD.  Que contenga las coordenadas varios recorridos para asignarle una ruta"),
        html.P(["En el siguiente enlace puede descargar un archivo de ejemplo: ", html.A("Enlace", href="https://drive.google.com/file/d/1RAiYd-NuWKHciFrKBjTnIXSvRVYvVKaI/view?usp=sharing")])

    ]),
    html.Div([
        dcc.Upload(
            id='upload-data2',
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
        html.Div(id='output-data-upload2'),
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

    id_rutas = list(df['IDRECORRIDO'].unique())
    df_predictions = pd.DataFrame(columns=['IDRECORRIDO', "RUTA", "PROBABILIDAD"])
    
    for  i, val in enumerate(id_rutas):
        if (i >= 10):
            break;
        df_route = df[df['IDRECORRIDO']==val]
        predicted, proba = model.predict(df_route)
 
        df_predictions.loc[i] =  [val] + [predicted] + [proba]

    return html.Div([
        
        html.Div([
            html.Div([
                html.H6([html.Span("Nombre del archivo: ", style={"color": "#6427B9"}),filename]),
                          ], className="col-md-6"),          
        ], className="row", style={"border": "1px solid #7cb927", "text-align" : "center", "border-radius":"10px"}),

        html.Hr(),  # horizontal line
        dash_table.DataTable(
                data=df_predictions.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df_predictions.columns]
            ),
        html.Hr(),  # horizontal line

      
        # For debugging, display the raw contents provided by the web browser
   
    ])


@app.callback(Output('output-data-upload2', 'children'),
              [Input('upload-data2', 'contents')],
              [State('upload-data2', 'filename'),
               State('upload-data2', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children