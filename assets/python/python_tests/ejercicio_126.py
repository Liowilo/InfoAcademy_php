# ejercicio_126.py
FUNCTION_NAME = "fibonacci"

def run_tests(user_function):
    tests = [
        {"input": (5,), "expected": [0, 1, 1, 2, 3]},
        {"input": (1,), "expected": [0]},
        {"input": (0,), "expected": []}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]