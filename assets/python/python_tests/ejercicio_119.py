# ejercicio_119.py
FUNCTION_NAME = "area_rectangulo"

def run_tests(user_function):
    tests = [
        {"input": (5, 3), "expected": 15},
        {"input": (2, 2), "expected": 4},
        {"input": (0, 5), "expected": 0}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]