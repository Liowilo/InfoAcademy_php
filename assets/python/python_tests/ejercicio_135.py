# ejercicio_135.py
FUNCTION_NAME = "camino_mas_corto"

def run_tests(user_function):
    grafo = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "C": 1, "D": 5},
        "C": {"A": 2, "B": 1, "D": 8, "E": 10},
        "D": {"B": 5, "C": 8, "E": 2, "F": 6},
        "E": {"C": 10, "D": 2, "F": 3},
        "F": {"D": 6, "E": 3}
    }
    tests = [
        {"input": (grafo, "A", "F"), "expected": (11, ["A", "C", "B", "D", "E", "F"])},
        {"input": (grafo, "A", "A"), "expected": (0, ["A"])},
        {"input": (grafo, "A", "G"), "expected": (float("inf"), [])}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]