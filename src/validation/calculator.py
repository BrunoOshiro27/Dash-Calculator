# Lógica de cálculo e validação
import re

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
    
def possible_expression(expression: str) -> bool:
    """
    Checks if the math expression could still become valid.
    Examples:
        "7+"   -> True   (could become "7+3")
        "7+."  -> False  (invalid)
        "3*(2" -> True   (unclosed parenthesis)
        "3*/2" -> False  (invalid operator order)
        ""     -> False
    """
    expression = expression.strip()
    print(expression)
    if not expression:
        return False

    # Expression can’t end with an invalid combination like +. or */ or (.
    if re.search(r"[+\-*/]{2,}$", expression):  # double operator at end
        return False
    if re.search(r"[+\-*/]\.$", expression):    # operator followed by dot
        return False
    if re.search(r"\.\D", expression):          # dot followed by non-digit
        return False
    if re.search(r"\d*\.\d*\.", expression):    # multiple dots in number
        return False
    if re.split(r"[+\-x÷%]",expression)[-1] == "00":
        return False

    # Try evaluating with a dummy ending like “0”
    try:
        eval(expression + "0", {"__builtins__": {}})
        return True
    except SyntaxError:
        return False
    except Exception:
        return True  # might be incomplete but still potentially valid