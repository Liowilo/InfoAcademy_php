# ejercicio_136.py
FUNCTION_NAME = "evaluar_arbol"

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def run_tests(user_function):
    arbol1 = Nodo("-",
                 Nodo("+",
                      Nodo(3),
                      Nodo("*",
                           Nodo(4),
                           Nodo(5))),
                 Nodo(6))
    
    arbol2 = Nodo("*",
                  Nodo(7),
                  Nodo("+",
                       Nodo(3),
                       Nodo(2)))
    
    tests = [
        {"input": (arbol1,), "expected": 17},
        {"input": (arbol2,), "expected": 35}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]