# ejercicio_123.py
FUNCTION_NAME = "suma_lista"

def run_tests(user_function):
    tests = [
        {"input": ([1, 2, 3],), "expected": 6},
        {"input": ([-1, 0, 1],), "expected": 0},
        {"input": ([],), "expected": 0}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]