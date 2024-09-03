# ejercicio_127.py
FUNCTION_NAME = "es_primo"

def run_tests(user_function):
    tests = [
        {"input": (17,), "expected": True},
        {"input": (4,), "expected": False},
        {"input": (2,), "expected": True}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]