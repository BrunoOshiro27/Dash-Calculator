# Callbacks do Dash
from dash.exceptions import PreventUpdate
from logic.calculator import evaluate_expression
from dash import Input, Output, State, ALL, ctx, callback


operands = {"+", "-", "*", "/"}
numbers = list()
for i in range(11):
    numbers.append(str(i))

@callback(
    Output("math_expression", "value"),
    Input({"type": "button", "value": ALL}, "n_clicks"),  
    Input("calculate_button", "n_clicks"),
    State("math_expression", "value"),
    prevent_initial_call=True
)
def handle_buttons(_, __, current_value):
    triggered = ctx.triggered_id
    dot_count = 0
    expr = str(current_value or "")
    if triggered == "calculate_button":
        return str(evaluate_expression(expr))    # se for none, retorna uma string vazia
    if isinstance(triggered, dict) and triggered.get("type") == "button":  # verifica se triggered é um dicionário e se contém o tipo "button"
        value = triggered["value"]
        if value == "C":
            return ""
        for s in expr:
            if s in operands:
                dot_count = 0
            elif s in ".":
                dot_count = 1
        # 1. Impede começar com operador (exceto o "-")
        if not expr and value in operands - {"-"}:
            raise PreventUpdate
        # 2. Se o último caractere for operador e o novo também for, substitui
        if len(expr) > 2 and expr[-1] in operands and value in operands: # short-circuit evaluation, se expr for none ja retorna false, se for true ai ele ve o expr[-1]
            print(expr, expr[-1], value)
            expr = expr[:-1] + value              # pega tudo menos o último caractere e concatena com o novo valor, funciona porque é uma string
            return expr  
        elif value in "." and expr[-1] in operands or value in "." and dot_count == 1:
            raise PreventUpdate
        elif len(expr) < 2 and value in operands - {"-"}:
            raise PreventUpdate
            
        return expr + value

    raise PreventUpdate