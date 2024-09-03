# ejercicio_121.py
FUNCTION_NAME = "contar_vocales"

def run_tests(user_function):
    tests = [
        {"input": ("Python",), "expected": 1},
        {"input": ("OpenAI",), "expected": 4},
        {"input": ("xyz",), "expected": 0}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]