# ejercicio_118.py
FUNCTION_NAME = "a_mayusculas"

def run_tests(user_function):
    tests = [
        {"input": ("python",), "expected": "PYTHON"},
        {"input": ("OpenAI",), "expected": "OPENAI"},
        {"input": ("",), "expected": ""}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]