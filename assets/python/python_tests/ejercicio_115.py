# ejercicio_115.py
FUNCTION_NAME = "saludar"

def run_tests(user_function):
    tests = [
        {"input": ("María",), "expected": "Hola, María!"},
        {"input": ("Juan",), "expected": "Hola, Juan!"},
        {"input": ("",), "expected": "Hola, !"}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]