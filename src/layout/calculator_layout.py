# Layout principal da calculadora
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

def get_layout():
    button_style = {
        "height": "60px",
        "fontSize": "1.5rem",
        "padding": "0.75rem 1rem",
    }

    return dbc.Container(
        dbc.Card(
            dbc.CardBody([
                html.H2("Calculadora", className="text-center mb-4"),

                dcc.Input(
                    id="math_expression",
                    type="text",
                    placeholder="ex: 2+2",
                    style={"width": "100%", "height": "40px", "marginBottom": "20px", "borderRadius": "8px"},
                ),

                dbc.Row([
                    dbc.Col(dbc.Button("7", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("8", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("9", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("/", color="primary", style=button_style), width=3),
                ], className="mb-2 g-2"),

                dbc.Row([
                    dbc.Col(dbc.Button("4", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("5", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("6", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("*", color="primary", style=button_style), width=3),
                ], className="mb-2 g-2"),

                dbc.Row([
                    dbc.Col(dbc.Button("1", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("2", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("3", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("-", color="primary", style=button_style), width=3),
                ], className="mb-2 g-2"),

                dbc.Row([
                    dbc.Col(dbc.Button("0", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button(".", color="secondary", style=button_style), width=3),
                    dbc.Col(dbc.Button("C", color="warning", style=button_style), width=3),
                    dbc.Col(dbc.Button("+", color="primary", style=button_style), width=3),
                ], className="mb-4 g-2"),

                dbc.Row(
                    dbc.Col(
                        dbc.Button("Calcular", id="calculate_button", color="success", style=button_style),
                        className="d-grid",
                        width=12
                    ),
                    className="mb-3"
                ),

                html.Div(id="output_result", className="h4 text-center"),

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