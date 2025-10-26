# Layout principal da calculadora
from dash import dcc
import dash_bootstrap_components as dbc
from layout import buttons_layout

def get_layout():
    return dbc.Container(
        dbc.Card(
            dbc.CardBody([
                dbc.Label("Calculadora", class_name="h2 d-flex justify-content-center mb-4 text-dark"),
                dcc.Input(
                    id="math_expression",
                    type="text",
                    placeholder="ex: 4+2",
                    className="w-100 mb-3 d-flex justify-content-around rounded text-end"
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Button("=", id="calculate_button", color="success"),
                        class_name="text-end mb-1",
                    ),
                    class_name="d-flex justify-content-center",
                ),
                buttons_layout.create_button_row(["7", "8", "9", "/"]),
                buttons_layout.create_button_row(["4", "5", "6", "*"]),
                buttons_layout.create_button_row(["1", "2", "3", "-"]),
                buttons_layout.create_button_row(["0", ".", "C", "+"]),  
            ]),
            style={"width": "300px"},
            class_name="bg-light p-2 rounded-4"
        ),
        class_name="mt-5 d-flex justify-content-center p-3 text-center"
    )