# Ponto de entrada do Dash

from dash import Dash
import dash_bootstrap_components as dbc
from dash import html
from layout.calculator_layout import get_layout
import callbacks.calculator_callbacks  # importa os callbacks para registrar

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(
    children=[get_layout()],
    style={
        "backgroundColor": "#1c1f26",  # azul clarinho
        "minHeight": "100vh",          # ocupa altura total da janela
        "padding": "30px"
    }
)

if __name__ == '__main__':
    app.run(debug=True)

