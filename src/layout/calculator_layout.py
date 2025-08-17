# Layout principal da calculadora
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

button_style = {
    "height": "60px",
    "fontSize": "1.5rem",
    "padding": "0.75rem 1rem",
}
def create_button_row(symbols):
    return dbc.Row([
        dbc.Col(dbc.Button(
            symbol,
            id={"type": "button", "value": symbol},
            color="primary" if symbol in "+-*/" else "secondary",
            style=button_style
        ), width=3) for symbol in symbols
    ], className="mb-2 g-2")

def get_layout():
    return dbc.Container(
        dbc.Card(
            dbc.CardBody([
                html.H2("Calculadora", className="text-center mb-4"),

                dcc.Input(
                    id="math_expression",
                    type="text",
                    placeholder="ex: 4+2",
                    style={"width": "100%", "height": "40px", "marginBottom": "20px", "paddingRight": "20px", "borderRadius": "8px","textAlign": "right"},
                ),

                create_button_row(["7", "8", "9", "/"]),
                create_button_row(["4", "5", "6", "*"]),
                create_button_row(["1", "2", "3", "-"]),
                create_button_row(["0", ".", "C", "+"]),

                dbc.Row(
                    dbc.Col(
                        dbc.Button("Calcular", id="calculate_button", color="success", style=button_style),
                        className="d-grid",
                        width=12
                    ),
                    className="mb-3"
                ),    
            ]),
            style={
                "backgroundColor": "#f8f9fa",
                "width": "400px",
                "margin": "auto",
                "padding": "20px",
                "borderRadius": "12px"
            },
        ),
        className="mt-5"
    )