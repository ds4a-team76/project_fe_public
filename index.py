

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from importlib import import_module
import warnings



from app import app
from apps import home, demo, page2, demo2

server = app.server


LOGO = "/assets/navbar_logo2.png"
app.title = "Awank_AI"
warnings.filterwarnings("ignore")

navbar_children = dbc.Nav(
    [
        html.Div(
            [       
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    html.Div(
                        [
                            html.Img(src=LOGO, height="60px"),
                        ],
                        style={"padding-left":"30px"},
                    ),
                    href="/",
                ),
                html.Div(
                    [
                        dbc.NavItem(
                            [
                                dbc.NavLink(
                                    "Inicio", 
                                    href="/", 
                                    className='text-uppercase btn-link font-weight-bold font-bold px-2'
                                )
                            ],
                            active=True
                        ),
               
                        dbc.NavLink(
                            "Demo 1", 
                            href="/demo", 
                            className='text-uppercase btn-link font-weight-bold font-bold px-2'
                        ),
                        dbc.NavLink(
                            "Demo 2", 
                            href="/demo2", 
                            className='text-uppercase btn-link font-weight-bold font-bold px-2'
                        ),
                        dbc.NavLink(
                            "Estadisticas", 
                            href="/estadisticas", 
                            className='text-uppercase btn-link font-weight-bold font-bold px-2'
                        ),
                    ],
                    className='row ml-5 pt-3'
                ),
            ],
            className='row'
        )
    ],
    className='mx-auto'
)


navbar = dbc.Navbar(
    navbar_children, 
    id='navbar',
    sticky="top"
)


footer = html.Footer(
    [
        html.Div(
            [
                html.Div(
                    [
                        'Copyright © 2020 Team 76 - Area Metropolitana.'
                    ],
                    className='copyright'
                )
            ],
            className = 'container py-4'
        )
    ],
    style = {'background-color': '#343a40', 'color': '#aaaaaa'}
)




# define page layout
app.layout = html.Div(
    [
        html.Div(id='blank-output'), # only for the name in the tab
        dcc.Location(id="url", refresh=False),
        navbar,
        # Column for user controls (SIDE BAR) 
        dcc.Loading(  
            id="loading-1",
            type="circle",
            fullscreen=True,
            children=[
                html.Div(
                    id="content"
                ),
            ],
        ),
        footer
    ]
)



# create callback for modifying page layout
@app.callback(
    Output("content", "children"),
    [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/apps":
        return home.layout
    if pathname == "/demo2":
      return demo2.layout
    if pathname == "/estadisticas":
        return page2.layout
    if pathname == "/demo":
     
        return demo.layout
  
        
    # if not recognised, return home page
    return home.layout




if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8050, debug=True, dev_tools_hot_reload = False)


