import dash
# import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    # external_stylesheets=[dbc.themes.BOOTSTRAP]
    external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)
