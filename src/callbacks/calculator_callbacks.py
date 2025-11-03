# Callbacks do Dash
from dash.exceptions import PreventUpdate
from logic.calculator import evaluate_expression, possible_expression
from dash import Input, Output, State, ALL, ctx, callback
from loguru import logger

OPERATORS = {"+", "-", "*", "/"}

@callback(
    Output("math_expression", "value"),
    Input({"type": "button", "value": ALL}, "n_clicks"),  
    Input("calculate_button", "n_clicks"),
    State("math_expression", "value"),
    prevent_initial_call=True
)
def handle_buttons(_, __, current_value):
    triggered = ctx.triggered_id
    expr = str(current_value or "")
    if triggered == "calculate_button":
        logger.debug(type(expr))
        return str(evaluate_expression(expr))    # se for none, retorna uma string vazia
    if isinstance(triggered, dict) and triggered.get("type") == "button":  # verifica se triggered é um dicionário e se contém o tipo "button"
        value = triggered["value"]
        new_expr = expr + value
        # reseta a calculadora
        if value == "C":
            return ""
        # Impede de ter zero com operador em seguida
        if value in OPERATORS and evaluate_expression(expr) == 0:
            raise PreventUpdate
        # Impede começar com operador (exceto o "-")
        elif not expr and value in OPERATORS - {"-"}:
            raise PreventUpdate
        # Se o último caractere for operador e o novo também for, substitui
        elif expr and expr[-1] in OPERATORS and value in OPERATORS:
            expr = expr[:-1] + value
            return expr
        # Analisa se a expressão é possivel, caso não seja, não adiciona o valor
        else:
            if not possible_expression(new_expr):
                raise PreventUpdate
    return new_expr


