# Lógica de cálculo e validação
def evaluate_expression(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}})
        return result
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero."
    except SyntaxError:
        return "Erro: Expressão mal formada. Verifique a sintaxe."
    except Exception:
        return "Erro: Algo deu errado. Tente novamente com uma expressão simples como 2+2."