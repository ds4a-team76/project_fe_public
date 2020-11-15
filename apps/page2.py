import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
from sqlalchemy import create_engine, text
import seaborn as sns
import datetime
import plotly.figure_factory as ff



# Conexión - Area
engine=create_engine('postgresql://postgres:T76ds4a.@teamds4a.cjznerjuma3r.us-east-1.rds.amazonaws.com/postgres', max_overflow=20)
def runQuery(sql):
    result = engine.connect().execution_options(isolation_level="AUTOCOMMIT").execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())
ruta = 'postgresql://postgres:T76ds4a.@teamds4a.cjznerjuma3r.us-east-1.rds.amazonaws.com/postgres'
ids_recorridos = pd.read_sql("""
SELECT secuenciarecorrido, COUNT(*) AS Conteo
FROM recorrido
GROUP BY secuenciarecorrido;
""",con = ruta)
ids_recorridos["conteo"].mean()


df8 = pd.read_sql("""
select count( distinct  g.secuenciarecorrido), g.idempresa, g.nombres from
 (select r.secuenciarecorrido, r.codigoruta, (r.subendelantera+r.subentrasera) as suben, r.velocidad, v.idempresa , v.nombres  
    from recorrido r, vehiculos v, empresas e where r.idvehiculo  = v.idvehiculo and r.velocidad > 60) g
group by g.idempresa, g.nombres order by count desc
""",con = ruta)

df9 = pd.read_sql("""
with speed_dist as (select r.secuenciarecorrido, r.idruta,  r.velocidad, v.idempresa , v.nombres  
    from detalles_recorrido r
  left join vehiculos v on r.idvehiculo  = v.idvehiculo
where r.velocidad > 60) 
select nombres as nombre_empresa, count(distinct secuenciarecorrido) as num_recorridos,avg(velocidad) as vel_promedio
from speed_dist
group by 1
order by vel_promedio desc
""",con = ruta)




# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfv = pd.read_csv(DATA_PATH.joinpath("vgsales.csv"))  # GregorySmith Kaggle
sales_list = ["North American Sales", "EU Sales", "Japan Sales", "Other Sales",	"World Sales"]


layout = html.Div(
    html.Div([
        # Adding one extar Div
        html.Div([
            html.H1(children='Area Metropolitana - Dashboard transporte inteligente'),
        ], className = 'row-md-9'),

        html.Div(
                    [
                        html.P(
                                    """
                                    En esta página se visualizan algunos gráficos importantes para el AMVA.
                    
                                    """, 
                                    className='lead font-weight-normal text-dark font-home-m'
                                ),

                        
                    ],
                    className = 'container pt-5 mt-2'
                ),






        html.Div([
            dcc.Graph(
                id='bar-chart',
                figure={
            'data': [
                {'x': df9['nombre_empresa'], 'y': df9['num_recorridos'], 'type': 'bar', 'name': 'Rutas mayores a 60'},
            ],
            'layout': {
                'title': 'Velocidad mayor a 60',
                'xaxis':{'title':'Rutas'},
                'yaxis':{'title':'Cantidad de recorridos por encima de 60'}

            }

        }
                ),
            ], className = 'col-md-7 p-lg-7 mx-auto my-7'),

            # Adding one more app/component
            html.Div([
                dcc.Graph(
                    id='line-chart',
                    figure={
            'data': [
                {'x': df8['nombres'], 'y': df8['count'], 'type': 'bar', 'name': 'Recorridos'},
            ],
            'layout': {
                'title': 'Recorrido por rutas', 
                'xaxis':{'title':'Rutas'},
                'yaxis':{'title':'Cantidad de recorridos'}

            }
        }
                )
                
            ], className = 'col-md-7 p-lg-7 mx-auto my-7')

        ], className = 'position-relative overflow-hidden text-center back-home'),



)

