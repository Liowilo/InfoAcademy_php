#ejercicio_114.py
FUNCTION_NAME = "sumar"

def run_tests(user_function):
    tests = [
        {"input": (2, 3), "expected": 5},
        {"input": (-1, 1), "expected": 0},
        {"input": (0, 0), "expected": 0}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]