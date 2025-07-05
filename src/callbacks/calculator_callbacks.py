# Callbacks do Dash
from dash import html, dcc, callback, Output, Input, State
from layout.calculator_layout import get_layout
from logic.calculator import evaluate_expression

@callback(
    Output('output_result', 'children'),
    Input('calculate_button', 'n_clicks'),
    State('math_expression', 'value')
)
def update_output(n_clicks, expression):
    if not n_clicks or not expression:
        return ""
    return evaluate_expression(expression)