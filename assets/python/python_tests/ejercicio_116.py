# ejercicio_116.py
FUNCTION_NAME = "es_par"

def run_tests(user_function):
    tests = [
        {"input": (2,), "expected": True},
        {"input": (3,), "expected": False},
        {"input": (0,), "expected": True}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]