# ejercicio_130.py
FUNCTION_NAME = "contar_palabras"

def run_tests(user_function):
    tests = [
        {"input": ("hola mundo hola",), "expected": {"hola": 2, "mundo": 1}},
        {"input": ("Python es genial Python",), "expected": {"python": 2, "es": 1, "genial": 1}},
        {"input": ("",), "expected": {}}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]