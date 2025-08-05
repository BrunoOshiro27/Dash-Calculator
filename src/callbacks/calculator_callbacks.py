# Callbacks do Dash
from layout.calculator_layout import get_layout, app
from logic.calculator import evaluate_expression
from dash import Input, Output, State, MATCH, ALL, ctx

@app.callback(
    Output("math_expression", "value"),
    Output("output_result", "children"),
    Input({"type": "button", "value": ALL}, "n_clicks"),  # <- ✅ Correto
    Input("calculate_button", "n_clicks"),
    State("math_expression", "value"),
    prevent_initial_call=True
)
def handle_buttons(_, __, current_value):
    triggered = ctx.triggered_id

    if triggered == "calculate_button":
        return current_value, evaluate_expression(current_value or "")

    if isinstance(triggered, dict) and triggered.get("type") == "button":
        value = triggered["value"]
        if value == "C":
            return "", ""
        return (current_value or "") + value, ""

    raise dash.exceptions.PreventUpdate