# ejercicio_124.py
FUNCTION_NAME = "factorial"

def run_tests(user_function):
    tests = [
        {"input": (5,), "expected": 120},
        {"input": (0,), "expected": 1},
        {"input": (3,), "expected": 6}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]