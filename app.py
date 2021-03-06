import dash
import dash_bootstrap_components as dbc
# meta_tags are required for the app layout to be mobile responsive
external_stylesheets = [dbc.themes.BOOTSTRAP, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}],
                            external_stylesheets=external_stylesheets,
                )
server = app.server
