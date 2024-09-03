# ejercicio_117.py
FUNCTION_NAME = "longitud"

def run_tests(user_function):
    tests = [
        {"input": ("Python",), "expected": 6},
        {"input": ("",), "expected": 0},
        {"input": ("OpenAI",), "expected": 6}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]