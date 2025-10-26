#buttons components
import dash_bootstrap_components as dbc

def create_button_row(symbols):
    return dbc.Row([
                dbc.Col(
                    dbc.Button(
                        symbol,
                        id={"type": "button", "value": symbol},
                        color="primary" if symbol in "+-*/" else "secondary",
                        class_name="w-100"
                    )
                ) for symbol in symbols
            ], class_name="mb-2 g-2")
