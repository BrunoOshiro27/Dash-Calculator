# Callbacks do Dash
from layout.calculator_layout import app
from logic.calculator import evaluate_expression
from dash import Input, Output, State, ALL, ctx

@app.callback(
    Output("math_expression", "value"),
    Input({"type": "button", "value": ALL}, "n_clicks"),  
    Input("calculate_button", "n_clicks"),
    State("math_expression", "value"),
    prevent_initial_call=True
)
def handle_buttons(_, __, current_value):
    triggered = ctx.triggered_id
    if triggered == "calculate_button":
        return str(evaluate_expression(current_value or ""))    # se for none, retorna uma string vazia

    if isinstance(triggered, dict) and triggered.get("type") == "button":  # verifica se triggered é um dicionário e se contém o tipo "button"
        value = triggered["value"]
        
        if value == "C":
            return ""
        
        expr = str(current_value or "")
        operadores = {"+", "-", "*", "/"}
        
        # 1. Impede começar com operador (exceto o "-")
        if not expr and value in operadores - {"-"}:
            raise dash.exceptions.PreventUpdate
        
        # 2. Se o último caractere for operador e o novo também for, substitui
        if expr and expr[-1] in operadores and value in operadores: # short-circuit evaluation, se expr for none ja retorna false, se for true ai ele ve o expr[-1]
            expr = expr[:-1] + value              # pega tudo menos o último caractere e concatena com o novo valor, funciona porque é uma string
            return expr
        
        return expr + value

    raise dash.exceptions.PreventUpdate